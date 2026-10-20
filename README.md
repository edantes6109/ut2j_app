# QCM — Annales d'examens & simulateur (UT2J, L2 Psychologie)

Applications web statiques d'entraînement aux examens universitaires (Université Toulouse Jean Jaurès, L2 Psychologie). Le code HTML/JS est partagé et généré par un script de build modulaire.

## 🚀 Fonctionnalités
- **Annales officielles exhaustives** : QCM et questions ouvertes d'examen avec repères de correction et corrigés modèles rédigés.
- **Origine précise des corrections** : distinction visuelle entre corrigé officiel, validation par le polycopié de cours (syllabus) ou générateur IA.
- **Modes d'entraînement flexibles** : révision pas-à-pas (avec feedback immédiat et auto-évaluation) ou simulation d'examen chronométrée.
- **Filtrage par thématique de cours** ou par document d'annale source.
- **Observatoire statistique des récurrences** : détection automatique des questions récurrentes tombées sur plusieurs sessions d'examen.
- **Générateur IA intégré** : banque d'entraînement complémentaire et génération de nouvelles questions d'examen inédites (Gemini / OpenAI).
- **Navigation inter-UE** : bascule directe d'un enseignement à l'autre depuis le portail d'accueil et les en-têtes d'épreuves.
- **Mode sombre**, raccourcis clavier, accessibilité et design responsive.

## 📂 Structure du projet
```
qcm_project/
├── build.py                 # Script de compilation unique (python3 build.py [UE...])
├── template/app.html        # Gabarit HTML/JS partagé (source de vérité de l'interface)
├── index.html               # Page d'accueil du portail (choix de l'UE)
├── package.json             # Outil de build : CLI Tailwind CSS
├── tailwind.config.js
├── 301/                     # UE 301 — Psychologie du Développement
│   ├── ue.json              # Métadonnées de l'UE (code, titre, niveau)
│   ├── config.json          # Configuration des chapitres et documents officiels
│   ├── data/                # Bases de données JSON (questions_database.json, open_questions.json)
│   ├── docs/                # Documents de cours, corrigés officiels et bases Excel
│   ├── scripts/             # Scripts de génération et maintenance de la base
│   └── index.html           # Application web générée pour l'UE 301
└── 304/                     # UE 304 — Psychologie Clinique & Psychopathologie
    ├── ue.json              # Métadonnées de l'UE
    ├── config.json          # Configuration des chapitres et documents officiels
    ├── data/                # Bases de données JSON
    ├── docs/                # Documents de cours et base Excel
    ├── scripts/             # Scripts de maintenance
    └── index.html           # Application web générée pour l'UE 304
```

> **Note** : Ne modifiez jamais les fichiers `<UE>/index.html` à la main : ils sont générés automatiquement par le script de build. Pour modifier l'interface, éditez `template/app.html` ; pour modifier les questions, éditez les fichiers du dossier `data/`.

## 🛠️ Utilisation locale & Compilation

### Compilation des applications
```bash
npm install            # une seule fois (installe Tailwind CSS pour la compilation locale)
python3 build.py       # compile toutes les UE et la page d'accueil
python3 build.py 301   # compile uniquement l'UE 301
python3 build.py 304   # compile uniquement l'UE 304
```

Le script précompile et inline le CSS Tailwind (aucun appel externe ni CDN requis en production) et assemble les données dans les fichiers `index.html` statiques autonomes.

## ⌨️ Raccourcis clavier (Session Quiz)
- `←` / `→` : question précédente / suivante
- `A` – `G` : cocher / décocher une proposition
- `Entrée` : valider la réponse (mode révision)
- `Échap` : fermer les fenêtres modales (générateur IA)

## 🌐 Déploiement GitHub Pages
1. Dans le dépôt GitHub : **Settings** > **Pages** > **Build and deployment**.
2. Sélectionnez la branche `main` et le dossier `/ (root)`.
3. Le site est servi directement :
   - Portail d'accueil : `https://<username>.github.io/<repo>/`
   - UE 301 : `https://<username>.github.io/<repo>/301/index.html`
   - UE 304 : `https://<username>.github.io/<repo>/304/index.html`
