#!/usr/bin/env python3
"""Build the static QCM apps.

Usage:
    python3 build.py            # build every UE folder (one containing ue.json) + the landing page
    python3 build.py 304 301    # build only the given UEs (+ the landing page)

Each UE folder (e.g. 304/) holds only its own content:
    ue.json                  identity: code, title, short_title, level
    data/questions_database.json, data/open_questions.json, data/embedded_ai_bank.json
    allowed_emails.json      access list (local only, never committed)
The shared HTML/JS lives in template/app.html. The output is <UE>/index.html, and a landing
page linking to all UEs is written to ./index.html (served by GitHub Pages).
"""
import hashlib
import html as html_lib
import json
import os
import subprocess
import sys
import tempfile
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH = os.path.join(ROOT, "template", "app.html")
CDN_TAG = '<script src="https://cdn.tailwindcss.com"></script>'


def load_json(path, default=None):
    if not os.path.exists(path):
        if default is not None:
            return default
        sys.exit(f"❌ Missing file: {os.path.relpath(path, ROOT)}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def discover_ues():
    return sorted(
        d for d in os.listdir(ROOT)
        if os.path.isfile(os.path.join(ROOT, d, "ue.json"))
    )


# --------------------------------------------------------------------------
# Dark mode (generated from a palette map; kept outside Tailwind's purge)
# --------------------------------------------------------------------------
def build_dark_css():
    P = "html.dark "
    rules = []

    def add(selector, decl):
        rules.append(f"{P}{selector}{{{decl}}}")

    def tok(t):
        return f'[class~="{t}"]'

    surfaces = {
        "bg-white": "#1e293b", "bg-slate-50": "#0f172a", "bg-slate-100": "#1e293b",
        "bg-slate-200": "#334155", "bg-slate-300": "#475569",
        "bg-white/95": "rgba(30,41,59,.95)",
    }
    for t, c in surfaces.items():
        add(tok(t), f"background-color:{c}")
    for t, c in {"hover:bg-slate-50": "#273449", "hover:bg-slate-100": "#273449",
                 "hover:bg-slate-200": "#3b4a61"}.items():
        add(tok(t) + ":hover", f"background-color:{c}")
    for t in ("bg-slate-50/40", "bg-slate-50/50", "bg-slate-50/70", "hover:bg-slate-50/70", "hover:bg-slate-50/80"):
        add(tok(t) + (":hover" if t.startswith("hover:") else ""), "background-color:rgba(15,23,42,.55)")
    for t in ("bg-slate-200/70", "bg-slate-200/80"):
        add(tok(t), "background-color:rgba(51,65,85,.8)")

    hues = {"amber": "245,158,11", "emerald": "16,185,129", "indigo": "99,102,241",
            "purple": "168,85,247", "rose": "244,63,94", "blue": "59,130,246"}
    for hue, rgb in hues.items():
        for shade, alpha in (("50", .12), ("100", .2), ("200", .3)):
            names = [f"bg-{hue}-{shade}"] + [f"bg-{hue}-{shade}/{a}" for a in (20, 40, 50, 60, 70, 80)]
            for n in names:
                add(tok(n), f"background-color:rgba({rgb},{alpha})")
                add(tok("hover:" + n) + ":hover", f"background-color:rgba({rgb},{alpha + .08})")
    for hue in hues:
        for n in (f"from-{hue}-50", f"from-{hue}-50/40", f"from-{hue}-50/70", f"from-{hue}-50/80",
                  f"to-{hue}-50", f"to-{hue}-50/20", f"to-{hue}-50/50", f"to-{hue}-50/80", f"via-{hue}-50"):
            add(tok(n), "background-image:none;background-color:rgba(30,41,59,.9)")
    add(tok("via-white"), "background-image:none;background-color:rgba(30,41,59,.9)")

    texts = {"text-slate-900": "#f1f5f9", "text-slate-800": "#e2e8f0", "text-slate-700": "#cbd5e1",
             "text-slate-600": "#cbd5e1", "text-slate-500": "#94a3b8", "text-slate-400": "#94a3b8",
             "hover:text-slate-900": "#f8fafc", "hover:text-slate-800": "#f8fafc"}
    for t, c in texts.items():
        add(tok(t) + (":hover" if t.startswith("hover:") else ""), f"color:{c}")
    light = {"amber": "#fcd34d", "emerald": "#6ee7b7", "indigo": "#a5b4fc",
             "purple": "#d8b4fe", "rose": "#fda4af"}
    for hue, c in light.items():
        for shade in ("600", "700", "800", "900", "950"):
            add(tok(f"text-{hue}-{shade}"), f"color:{c}")
    for n in ("hover:text-indigo-800", "hover:text-rose-800"):
        add(tok(n) + ":hover", "color:#e0e7ff")

    for t, c in {"border-slate-100": "#273449", "border-slate-200": "#334155", "border-slate-200/70": "#334155",
                 "border-slate-200/80": "#334155", "border-slate-300": "#475569", "divide-slate-200": "#334155"}.items():
        if t.startswith("divide"):
            add(tok(t) + " > * + *", f"border-color:{c}")
        else:
            add(tok(t), f"border-color:{c}")
    for hue, rgb in hues.items():
        for shade in ("100", "200", "300"):
            for n in (f"border-{hue}-{shade}", f"border-{hue}-{shade}/60"):
                add(tok(n), f"border-color:rgba({rgb},.4)")

    return (
        "html.dark{color-scheme:dark;}"
        "html.dark body{background-color:#0b1220 !important;color:#e2e8f0 !important}"
        "html.dark .card-white{background-color:#1e293b !important;border-color:#334155 !important;color:#e2e8f0 !important;box-shadow:none}"
        "html.dark textarea,html.dark input,html.dark select{background-color:#0f172a;color:#e2e8f0;border-color:#475569}"
        "html.dark ::placeholder{color:#64748b}"
        "html.dark .custom-scrollbar::-webkit-scrollbar-track{background:#0f172a}"
        "html.dark .custom-scrollbar::-webkit-scrollbar-thumb{background:#475569}"
        + "\n".join(rules)
    )


# --------------------------------------------------------------------------
# Tailwind precompilation (replaces the Play CDN <script>)
# --------------------------------------------------------------------------
def inline_tailwind(page):
    tw_bin = os.path.join(ROOT, "node_modules", ".bin", "tailwindcss")
    tw_source = os.path.join(ROOT, "template", ".tw_source.html")
    if not os.path.exists(tw_bin):
        print("⚠️  Tailwind CLI not found (run 'npm install' at the project root). Using the CDN script instead.")
        return page
    try:
        with open(tw_source, "w", encoding="utf-8") as f:
            f.write(page)
        with tempfile.TemporaryDirectory() as tmp:
            css_in = os.path.join(tmp, "in.css")
            css_out = os.path.join(tmp, "out.css")
            with open(css_in, "w", encoding="utf-8") as f:
                f.write("@tailwind base;\n@tailwind components;\n@tailwind utilities;\n")
            subprocess.run(
                [tw_bin, "-c", os.path.join(ROOT, "tailwind.config.js"), "-i", css_in, "-o", css_out, "--minify"],
                cwd=ROOT, check=True, capture_output=True, text=True,
            )
            with open(css_out, "r", encoding="utf-8") as f:
                css = f.read()
        print(f"   Tailwind precompiled and inlined ({len(css)} bytes of CSS).")
        return page.replace(CDN_TAG, "<style>" + css + "</style>")
    except (subprocess.CalledProcessError, OSError) as exc:
        print(f"⚠️  Tailwind precompilation failed, falling back to the CDN script: {getattr(exc, 'stderr', exc)}")
        return page
    finally:
        if os.path.exists(tw_source):
            os.remove(tw_source)


# --------------------------------------------------------------------------
# Per-UE build
# --------------------------------------------------------------------------
def read_allowed_users(ue_dir):
    raw_users = load_json(os.path.join(ue_dir, "allowed_emails.json"), default=[])
    users = []
    for item in raw_users:
        if isinstance(item, dict):
            email = str(item.get("email", "")).strip().lower()
            pin = str(item.get("pin", "")).strip()
            if email and pin:
                users.append({"email": email, "pin": pin})
        elif isinstance(item, str) and item.strip():
            parts = item.strip().split(":")
            email = parts[0].strip().lower()
            pin = parts[1].strip() if len(parts) > 1 else "1234"
            if email:
                users.append({"email": email, "pin": pin})
    return users


def build_ue(code):
    ue_dir = os.path.join(ROOT, code)
    cfg = load_json(os.path.join(ue_dir, "ue.json"))
    course_cfg = load_json(os.path.join(ue_dir, "config.json"), default={})
    data_dir = os.path.join(ue_dir, "data")

    qcm = load_json(os.path.join(data_dir, "questions_database.json"))
    for q in qcm:
        q["type"] = "qcm"
    open_q = load_json(os.path.join(data_dir, "open_questions.json"))
    for q in open_q:
        q["type"] = "open"
    ai_bank = load_json(os.path.join(data_dir, "embedded_ai_bank.json"))
    for q in ai_bank:
        if not q.get("type"):
            q["type"] = "qcm" if q.get("options") else "open"

    users = read_allowed_users(ue_dir)
    hashes = [hashlib.sha256(f"{u['email']}:{u['pin']}".encode("utf-8")).hexdigest() for u in users]

    parts_cfg = course_cfg.get("parts", {})
    categories = course_cfg.get("categories", [])
    official_docs = course_cfg.get("official_documents", [])
    ai_cfg = course_cfg.get("ai", {})

    part1_title = parts_cfg.get("part1", {}).get("title", "Partie 1")
    part1_icon = parts_cfg.get("part1", {}).get("icon", "🧠")
    part2_title = parts_cfg.get("part2", {}).get("title", "Partie 2")
    part2_icon = parts_cfg.get("part2", {}).get("icon", "📊")

    # Format CHAPTER_CATEGORIES JavaScript code
    cat_js_entries = []
    for c in categories:
        filter_js = c.get("filter_js")
        if not filter_js and "filter_contains" in c:
            conds = " || ".join([f"t.includes({json.dumps(x)})" for x in c["filter_contains"]])
            filter_js = f"(t) => {conds}"
        elif filter_js and not filter_js.startswith("("):
            filter_js = f"(t) => {filter_js}"
        entry = (
            f"      {{\n"
            f"        id: {json.dumps(c['id'])},\n"
            f"        partNum: {c.get('partNum', 1)},\n"
            f"        title: {json.dumps(c.get('title', ''))},\n"
            f"        description: {json.dumps(c.get('description', ''))},\n"
            f"        filterFn: {filter_js}\n"
            f"      }}"
        )
        cat_js_entries.append(entry)
    categories_js = "[\n" + ",\n".join(cat_js_entries) + "\n    ]"

    # Format dynamic category pills HTML
    pills = []
    current_part = None
    for cat in categories:
        if current_part is not None and cat.get("partNum") != current_part:
            pills.append('<span class="text-slate-300 font-light px-0.5">|</span>')
        current_part = cat.get("partNum")
        cid = cat['id']
        pill_label = cat.get("short_pill", cat.get("title", ""))
        pills.append(
            f'<button type="button" onclick="filterCategoryPill(\'{cid}\')" data-cat-id="{cid}" '
            f'class="cat-pill px-2.5 py-1 rounded-lg font-semibold bg-white text-slate-700 border border-slate-200 hover:bg-slate-50 transition whitespace-nowrap">\n'
            f'                  {html_lib.escape(pill_label)}\n'
            f'                </button>'
        )
    dynamic_pills_html = '\n                '.join(pills)
    if dynamic_pills_html:
        dynamic_pills_html = '<span class="text-slate-300 font-light px-0.5">|</span>\n                ' + dynamic_pills_html

    total_qcm_count = len(qcm)
    total_open_count = len(open_q)
    total_questions_count = total_qcm_count + total_open_count
    total_sessions_count = len(official_docs)
    total_qcm_sessions = len(set(q.get("document") for q in qcm if q.get("document")))
    total_open_sessions = len(set(q.get("document") for q in open_q if q.get("document")))

    years = []
    for d in official_docs:
        years.extend([int(y) for y in re.findall(r'\b(20\d\d)\b', d.get("name", ""))])
    years_range = f"{min(years)} - {max(years)}" if years else "2018 - 2025"

    ai_discipline = ai_cfg.get("discipline", cfg.get("title", f"UE {code}"))
    ai_instructions = ai_cfg.get("prompt_instructions", "")

    print(f"\n=== UE {code} ===")
    print(f"   Loaded {len(qcm)} QCM, {len(open_q)} Open, {len(ai_bank)} AI bank items, {len(users)} authorized user(s).")
    print(f"   Structure: {len(categories)} categories, {total_sessions_count} official documents ({total_qcm_sessions} QCM, {total_open_sessions} Open).")

    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        page = f.read()

    def esc(s):
        return html_lib.escape(str(s), quote=False)

    def js_json(value):
        # json.dumps output is embedded in <script>: neutralise "</" so it can't close the tag.
        return json.dumps(value, ensure_ascii=False).replace("</", "<\\/")

    substitutions = {
        "{{QCM_DATA}}": js_json(qcm),
        "{{OPEN_DATA}}": js_json(open_q),
        "{{AI_BANK_DATA}}": js_json(ai_bank),
        "{{ALLOWED_HASHES}}": js_json(hashes),
        "{{DARK_CSS}}": build_dark_css(),
        "{{UE_CODE}}": esc(code),
        "{{UE_TITLE}}": esc(cfg.get("title", f"UE {code}")),
        "{{UE_SHORT_TITLE}}": esc(cfg.get("short_title", cfg.get("title", ""))),
        "{{PART1_TITLE}}": esc(part1_title),
        "{{PART1_ICON}}": esc(part1_icon),
        "{{PART2_TITLE}}": esc(part2_title),
        "{{PART2_ICON}}": esc(part2_icon),
        "{{CHAPTER_CATEGORIES_JS}}": categories_js,
        "{{OFFICIAL_DOCUMENTS_JS}}": js_json(official_docs),
        "{{DYNAMIC_PILLS_HTML}}": dynamic_pills_html,
        "{{TOTAL_QUESTIONS}}": str(total_questions_count),
        "{{TOTAL_QCM}}": str(total_qcm_count),
        "{{TOTAL_OPEN}}": str(total_open_count),
        "{{TOTAL_SESSIONS}}": str(total_sessions_count),
        "{{TOTAL_QCM_SESSIONS}}": str(total_qcm_sessions),
        "{{TOTAL_OPEN_SESSIONS}}": str(total_open_sessions),
        "{{ANNALES_YEARS_RANGE}}": years_range,
        "{{AI_DISCIPLINE}}": esc(ai_discipline),
        "{{AI_PROMPT_INSTRUCTIONS}}": esc(ai_instructions),
    }
    for token, value in substitutions.items():
        page = page.replace(token, value)

    page = inline_tailwind(page)

    out_path = os.path.join(ue_dir, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"   Generated {os.path.relpath(out_path, ROOT)} ({len(page)} characters).")

    if users:
        print(f"   🔒 Access restricted to {len(users)} user(s). Magic links (relative to the site root):")
        for u in users:
            print(f"      - {u['email']} | PIN: {u['pin']}  →  {code}/?email={u['email']}&pin={u['pin']}")
    else:
        print(f"   ⚠️  No user configured in {code}/allowed_emails.json: access is currently open.")
    return cfg


# --------------------------------------------------------------------------
# Landing page
# --------------------------------------------------------------------------
def build_landing(ues):
    cards = []
    for code in ues:
        cfg = load_json(os.path.join(ROOT, code, "ue.json"))
        title = html_lib.escape(cfg.get("title", f"UE {code}"))
        level = html_lib.escape(cfg.get("level", ""))
        cards.append(
            f'<a class="card" href="./{html_lib.escape(code)}/index.html">'
            f'<span class="badge">UE {html_lib.escape(code)}</span>'
            f'<span class="title">{title}</span>'
            f'<span class="level">{level}</span></a>'
        )
    page = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="noindex, nofollow, noarchive">
  <title>Révisions QCM • UT2J</title>
  <script>
    // Backward compatibility: old magic links pointed at the site root.
    if (/[?&]email=/.test(location.search)) location.replace('./{html_lib.escape(ues[0])}/index.html' + location.search);
  </script>
  <style>
    :root {{ color-scheme: light dark; --bg:#f8fafc; --fg:#0f172a; --muted:#64748b; --card:#ffffff; --border:#e2e8f0; --accent:#4f46e5; }}
    @media (prefers-color-scheme: dark) {{ :root {{ --bg:#0b1220; --fg:#e2e8f0; --muted:#94a3b8; --card:#1e293b; --border:#334155; --accent:#a5b4fc; }} }}
    * {{ box-sizing: border-box; }}
    body {{ margin:0; min-height:100vh; background:var(--bg); color:var(--fg); font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif; padding:2rem 1rem; }}
    main {{ max-width: 42rem; margin: 0 auto; }}
    h1 {{ font-size:1.6rem; margin:0 0 .25rem; }}
    p.sub {{ color:var(--muted); margin:0 0 1.5rem; }}
    .grid {{ display:grid; gap:.9rem; }}
    .card {{ display:flex; flex-direction:column; gap:.3rem; padding:1.1rem 1.25rem; background:var(--card); border:1px solid var(--border); border-radius:1rem; text-decoration:none; color:inherit; transition:transform .12s, border-color .12s; }}
    .card:hover, .card:focus-visible {{ transform:translateY(-2px); border-color:var(--accent); outline:none; }}
    .badge {{ align-self:flex-start; font-size:.72rem; font-weight:700; padding:.15rem .6rem; border-radius:999px; background:var(--accent); color:#fff; }}
    @media (prefers-color-scheme: dark) {{ .badge {{ color:#0b1220; }} }}
    .title {{ font-weight:700; font-size:1.05rem; }}
    .level {{ color:var(--muted); font-size:.85rem; }}
  </style>
</head>
<body>
  <main>
    <h1>📚 Révisions QCM</h1>
    <p class="sub">Choisissez votre unité d'enseignement.</p>
    <div class="grid">
      {chr(10).join('      ' + c for c in cards).strip()}
    </div>
  </main>
</body>
</html>
"""
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(page)
    print(f"\nGenerated landing page index.html listing: {', '.join(ues)}")


def main():
    available = discover_ues()
    if not available:
        sys.exit("❌ No UE folder found (a UE folder contains a ue.json).")
    requested = [a for a in sys.argv[1:] if a != "all"]
    for code in requested:
        if code not in available:
            sys.exit(f"❌ Unknown UE '{code}'. Available: {', '.join(available)}")
    for code in (requested or available):
        build_ue(code)
    build_landing(requested or available)


if __name__ == "__main__":
    main()
