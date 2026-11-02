# -*- coding: utf-8 -*-
"""
Exams Data Part 1:
1. Exemple de sujet d'examen (Christine Sorsana) - 20 Q
2. 2016-2017 – Session 1 - 20 Q
3. 2016-2017 – Session 2 - 20 Q
4. 2018-2019 – Session 2 - 9 Q
"""

EXAMS_PART1 = [
    # =========================================================================
    # 1. Exemple de sujet d'examen (Christine Sorsana)
    # =========================================================================
    {
        "document": "Exemple de sujet d'examen (C. Sorsana)",
        "source": "Exemple_sujet_examen_QCM.docx (+ .pdf, UE301_Corrige_Sujet_Examen.docx)",
        "questions": [
            {
                "q_num": 1,
                "theme": "Ch. 1 (1.2) Débats endogène / social : nativisme, empirisme, constructivisme",
                "question": "Selon cette conception psychologique, « nous n'avons pas besoin des ruses et des menaces de pédagogues tour à tour sévères et caressants pour apprendre à parler. C'est donc que l'esprit est de lui-même organisé selon des structures modulaires et fonctionnelles qui prédisposent à certaines acquisitions fondamentales ». Il s'agit de la conception :",
                "options": {
                    "A": "behavioriste",
                    "B": "constructiviste",
                    "C": "historico-culturelle",
                    "D": "nativiste",
                    "E": "socioconstructiviste"
                },
                "answer": "D"
            },
            {
                "q_num": 2,
                "theme": "Ch. 2 (2.2) Perceptions fœtales et mémoire prénatale",
                "question": "Dans un contexte expérimental, que peut traduire une modification du rythme cardiaque du fœtus ?",
                "options": {
                    "A": "Ses rythmes circadiens.",
                    "B": "Des biais dans le recueil de données perçus grâce au progrès des outils de mesure.",
                    "C": "Des capacités d'apprentissage.",
                    "D": "Un seuil perceptif, par exemple sa perception auditive.",
                    "E": "Une variation de son niveau attentionnel."
                },
                "answer": "C, D, E"
            },
            {
                "q_num": 3,
                "theme": "Ch. 3 (3.2) Techniques d'étude du nourrisson : habituation et réaction à la nouveauté",
                "question": "Qu'est-ce que le phénomène d'habituation ?",
                "options": {
                    "A": "Cela désigne généralement un comportement acquis, ayant atteint un certain niveau d'automaticité, et dans le registre des conduites motrices plutôt que psychophysiques.",
                    "B": "C'est un mode d'apprentissage dominant chez le bébé qui repose sur les perceptions.",
                    "C": "C'est l'atténuation, pouvant aller jusqu'à la disparition d'une réponse par répétition du stimulus qui la provoque.",
                    "D": "Le conditionnement est un exemple de phénomène d'habituation."
                },
                "answer": "B, C"
            },
            {
                "q_num": 4,
                "theme": "Ch. 3 (3.2) Techniques d'étude du nourrisson : préférence visuelle",
                "question": "Un chercheur souhaite déterminer à partir de quel âge les enfants sont capables de reconnaître les peluches qui sont présentes dans leur quotidien. Il cherche pour cela à mesurer chez les enfants le temps de fixation relatif d'une peluche familière et d'une peluche nouvelle. Le premier enfant (4 mois) regarde aussi longtemps les deux peluches. Que peut-on en conclure ?",
                "options": {
                    "A": "Le développement socio-affectif est trop limité à 4 mois pour que l'enfant investisse la peluche comme un objet d'intérêt, voire comme un objet transitionnel.",
                    "B": "Seule la réalisation de mesures physiologiques (i.e., rythme cardiaque) permettra d'établir des conclusions fiables.",
                    "C": "On ne peut rien conclure : il se peut que l'enfant ne reconnaisse pas la peluche familière ou qu'il la reconnaisse sans avoir de préférence visuelle manifeste.",
                    "D": "Le bébé a des problèmes de vision qui ne lui permettent pas de discriminer les deux peluches."
                },
                "answer": "C"
            },
            {
                "q_num": 5,
                "theme": "Ch. 4 (4.4) Développement du langage : étapes chronologiques",
                "question": "Dans l'organisation chronologique du développement du langage proposée ci-dessous, toutes les erreurs sont à cocher :",
                "options": {
                    "A": "A la naissance, le bébé discrimine tous les phonèmes qui forment les mots des langues humaines, quelles que soient les paroles qu'il entend.",
                    "B": "La compétence à discriminer des sons proches (comme « b » et « p », « l » et « r », ...) des langages humains, quelles que soient les paroles qu'il entend, augmente avec l'âge.",
                    "C": "Vers l'âge d'un an, il pointe les objets de l'index pour inciter l'adulte à les nommer.",
                    "D": "Ensuite, vers 14 mois, il se met à babiller pour se mémoriser ces nouveaux mots.",
                    "E": "A partir de 20 mois, le bébé accroit considérablement son vocabulaire."
                },
                "answer": "B, D"
            },
            {
                "q_num": 6,
                "theme": "Ch. 1 (1.3) Méthodologies d'étude des transformations : longitudinale, transversale",
                "question": "Un chercheur étudie l'âge d'apparition et les manifestations de la prise d'initiative d'offrir et de demander. Huit enfants ont été observés pendant six mois tous les quinze jours. Lors de la première observation, le plus jeune avait 7 mois et le plus âgé 10 mois. Les principaux résultats montrent que la réponse à l'offre est plus précoce que la réponse à la demande. La méthode utilisée est :",
                "options": {
                    "A": "catégorielle.",
                    "B": "longitudinale.",
                    "C": "mixte (ou trans-séquentielle).",
                    "D": "psychométrique.",
                    "E": "transversale."
                },
                "answer": "B"
            },
            {
                "q_num": 7,
                "theme": "Ch. 3 (3.5) Intelligence sensori-motrice : permanence de l'objet et erreur A-non-B",
                "question": "Voici l'observation suivante de Piaget (1937, p. 48) : « Jacqueline regarde son perroquet posé sur ses genoux. Je pose ma main sur l'objet : elle la soulève et saisit le perroquet. Je le lui reprends, et, sous ses yeux, je l'éloigne très lentement pour le mettre sous un tapis, à 40 cm de là. Pendant ce temps je remets ma main sur ses genoux. Dès que Jacqueline cesse de voir le perroquet, elle reporte son regard sur ses genoux, soulève ma main et cherche dessous. La réaction est la même durant trois essais consécutifs ». Cette observation illustre :",
                "options": {
                    "A": "Le fait que Jacqueline ne semble pas tenir compte des déplacements de l'objet puisqu'elle continue de rechercher son jouet à l'endroit initial où il se trouvait.",
                    "B": "Ce que Piaget a appelé « l'erreur A non B ».",
                    "C": "La réaction typique du sous-stade 4 du stade de l'intelligence sensorimotrice lors de la recherche de l'objet caché.",
                    "D": "Les conduites d'un enfant âgé d'environ 24 mois."
                },
                "answer": "A, B, C"
            },
            {
                "q_num": 8,
                "theme": "Ch. 4 (4.2) Pensée préopératoire : fonction sémiotique",
                "question": "A un moment donné de leur développement psychologique, les enfants sont capables d'imiter un modèle en différé, de jouer à des jeux de « faire semblant », de construire des images mentales, de dessiner et d'user du langage. Selon la théorie piagétienne, vers quel âge cet ensemble de conduites se développe-t-il ?",
                "options": {
                    "A": "8-12 mois",
                    "B": "12-18 mois",
                    "C": "18-24 mois",
                    "D": "24-36 mois"
                },
                "answer": "C"
            },
            {
                "q_num": 9,
                "theme": "Ch. 4 (4.2) Pensée préopératoire : fonction sémiotique / symbolique",
                "question": "Comment cet ensemble de conduites (imitation différée, jeu symbolique, dessin, image mentale, langage) est-il appelé ?",
                "options": {
                    "A": "Le modèle interne opérant",
                    "B": "L'égocentrisme",
                    "C": "La fonction sémiotique",
                    "D": "Le système de support à l'acquisition du langage (ou LASS)",
                    "E": "La fonction symbolique",
                    "F": "La fonction exécutive"
                },
                "answer": "C, E"
            },
            {
                "q_num": 10,
                "theme": "Ch. 4 (4.4) Développement du langage : approches théoriques (Bruner, Vygotski)",
                "question": "Quels sont les chercheurs qui affirment que la première fonction du langage qui se met en place au cours du développement humain est la fonction communicative ?",
                "options": {
                    "A": "Jérôme Bruner",
                    "B": "Noam Chomsky",
                    "C": "Jean Piaget",
                    "D": "Lev Vygotski",
                    "E": "John Watson"
                },
                "answer": "A, D"
            },
            {
                "q_num": 11,
                "theme": "Ch. 3 (3.6) Imitation et communication précoce : Nadel et Baudonnière",
                "question": "Des dyades ou des trios d'enfants de même âge se trouvent dans une pièce de la crèche ou de l'école maternelle, sous le regard discret des adultes loin des yeux. Des objets existent en autant d'exemplaires qu'il y a d'enfants présents dans la pièce : ballons, chaises, mobiles, lunettes, chapeaux, serviettes, poupées, voitures, etc. Vous observez les conduites réalisées spontanément par les enfants qui sont libres de quitter la pièce quand ils le souhaitent. Ces enfants sont âgés de 3 ans. Qu'observez-vous ?",
                "options": {
                    "A": "Les enfants jouent côte à côte, chacun dans son coin.",
                    "B": "Les enfants utilisent simultanément les mêmes objets en s'imitant.",
                    "C": "Un enfant observe attentivement l'autre produire une action avec un objet puis, de manière différée, il va imiter la conduite observée.",
                    "D": "Les conduites des enfants indiquent qu'ils ne sont pas totalement différenciés d'autrui.",
                    "E": "Les conduites des enfants illustrent la période du syncrétisme différencié selon la théorie wallonienne."
                },
                "answer": "B, E"
            },
            {
                "q_num": 12,
                "theme": "Ch. 4 (4.4) Langage égocentrique et langage pour soi : Piaget vs Vygotski",
                "question": "Vous observez, à son insu, un enfant seul dans sa chambre en train de construire une maison en bois coloré. Il est âgé d'environ 3 ans et demi et, en même temps qu'il pose les différents morceaux de bois, il parle à voix haute : « je prends maintenant le vert et je le pose sur le rouge... non, sur le bleu ». Etc. Sa conduite témoigne de :",
                "options": {
                    "A": "l'artificialisme de la description de ses actions.",
                    "B": "son besoin inné de communiquer, notamment avec sa mère qui n'est pas très loin de lui, dans la pièce à côté.",
                    "C": "la nécessité de s'appuyer sur un outil externe pour résoudre cette tâche complexe pour lui, selon la perspective vygotskienne.",
                    "D": "son égocentrisme."
                },
                "answer": "C, D"
            },
            {
                "q_num": 13,
                "theme": "Ch. 4 (4.1) & Ch. 5 (5.1) Conception wallonienne du développement",
                "question": "Cochez toutes les notions qui se rapportent à la conception wallonienne du développement psychologique :",
                "options": {
                    "A": "Autrui",
                    "B": "Catégories",
                    "C": "Construction de la personne",
                    "D": "Emotions",
                    "E": "Milieux"
                },
                "answer": "A, B, C, D, E"
            },
            {
                "q_num": 14,
                "theme": "Ch. 5 (5.3) & (5.4) Tutelle, étayage et ZPD (Bruner, Vygotski)",
                "question": "Lorsqu'un chercheur conçoit le développement psychologique comme un processus d'assistance et d'interactions asymétriques, les concepts précis qui lui sont utiles à la théorisation d'une telle conception sont :",
                "options": {
                    "A": "L'équilibration",
                    "B": "L'imitation",
                    "C": "La modularité",
                    "D": "La relation de tutelle.",
                    "E": "La zone proximale de développement."
                },
                "answer": "D, E"
            },
            {
                "q_num": 15,
                "theme": "Ch. 1 (1.4) Niveaux d'explication de Doise",
                "question": "Pour expliquer le raisonnement d'un enfant qui essaie de résoudre une tâche, le chercheur étudie les représentations sociales de l'intelligence, du savoir, de l'école, etc. partagées au sein de la famille de l'enfant ainsi que leurs liens avec les pratiques éducatives. Du point de vue de la classification de Doise (1982), le niveau d'analyse retenu par ce chercheur est :",
                "options": {
                    "A": "le niveau 1 ou intra-individuel.",
                    "B": "le niveau 2 ou interindividuel.",
                    "C": "le niveau 3 ou positionnel.",
                    "D": "le niveau 4 ou idéologique."
                },
                "answer": "D"
            },
            {
                "q_num": 16,
                "theme": "Ch. 4 (4.5) Le dessin enfantin : les stades de Luquet",
                "question": "Un chercheur a décrit le développement de l'activité graphique de l'enfant en plusieurs stades. L'un d'entre eux est appelé « réalisme intellectuel ». Quelle est la conduite enfantine caractéristique de ce stade ?",
                "options": {
                    "A": "L'enfant dessine ce qu'il voit et non ce qu'il sait de l'objet.",
                    "B": "L'enfant dessine ce qu'il sait et non ce qu'il voit de l'objet.",
                    "C": "L'enfant ne parvient pas à dessiner le thème qu'il a annoncé avant de dessiner.",
                    "D": "L'enfant dessine la perspective."
                },
                "answer": "B"
            },
            {
                "q_num": 17,
                "theme": "Ch. 4 (4.5) Le dessin enfantin : Luquet",
                "question": "Quel est le chercheur en question ayant décrit le développement de l'activité graphique (réalisme fortuit, manqué, intellectuel, visuel) ?",
                "options": {
                    "A": "Elisabeth Spelke.",
                    "B": "Florence Laura Goodenough.",
                    "C": "George-Henri Luquet.",
                    "D": "Henri Wallon."
                },
                "answer": "C"
            },
            {
                "q_num": 18,
                "theme": "Ch. 5 (5.3) Zone proximale de développement (Vygotski)",
                "question": "Cochez toutes les propositions correctes qui définissent la notion de « zone proximale de développement » :",
                "options": {
                    "A": "Cette notion rend compte du fait que le jeune enfant construit progressivement un modèle interne des personnes proches de lui et avec lesquelles il a construit un lien privilégié.",
                    "B": "Cette notion se définit comme l'écart entre ce que l'enfant sait faire seul et ce qu'il sait faire avec l'aide d'une personne plus compétente que lui.",
                    "C": "Cette notion se définit comme la proximité physique requise entre la mère et l'enfant afin que tous les deux puissent prêter attention au même objet.",
                    "D": "C'est une notion proposée par John Bowlby.",
                    "E": "C'est une notion proposée par Lev Vygotski."
                },
                "answer": "B, E"
            },
            {
                "q_num": 19,
                "theme": "Ch. 5 (5.2) Opérations concrètes : inclusion et quantification des classes (Piaget)",
                "question": "On présente à un enfant de 6 ans un bracelet composé de 8 grosses perles en plastique rouge et de 3 grosses perles en plastique jaune et on lui demande : « Y a-t-il plus de perles rouges ou plus de perles en plastique ? ». Il répond « Plus de perles rouges parce que celles en plastique, il n'y en a que trois ». On l'interroge : « Mais les rouges ne sont-elles pas aussi en plastique ? » L'enfant précise : « Ah ! oui ». On demande : « Alors, est-ce qu'il y a plus de perles rouges ou plus de perles en plastique ? » et l'enfant conclut : « Plus de rouges ». Que peut-on en conclure ?",
                "options": {
                    "A": "L'enfant est certainement capable de manier correctement les quantificateurs « tous » et « quelques ».",
                    "B": "L'enfant ne comprend pas la composition additive des classes.",
                    "C": "L'enfant perçoit le bracelet de manière finaliste.",
                    "D": "L'enfant reste prisonnier des données perceptives.",
                    "E": "L'enfant raisonne de manière opératoire."
                },
                "answer": "B, D"
            },
            {
                "q_num": 20,
                "theme": "Ch. 5 (5.3) Concepts spontanés et concepts scientifiques (Vygotski)",
                "question": "Au cours du développement de sa pensée, l'enfant construit des concepts du type (« soeur », « mère », ...) puis des concepts du type (« atome », « triangle isocèle », ...). Comment les chercheurs expliquent-ils cette progression conceptuelle ?",
                "options": {
                    "A": "Piaget considère que les enfants construisent ces deux types de concepts grâce à leurs actions sur le monde physique, leur maturation biologique, leurs interactions sociales et le processus interne d'équilibration.",
                    "B": "Pour expliquer la construction des concepts scientifiques, Vygotski et Piaget s'accordent pour affirmer que les enfants ont besoin des apprentissages scolaires.",
                    "C": "Selon Vygotski, le développement conceptuel, quel que soit le type de concepts, s'élabore grâce aux contextes sociaux d'apprentissage.",
                    "D": "Concernant l'interaction entre ces deux types de concepts, Vygotski précise qu'il faut un certain niveau de développement des concepts spontanés pour que les concepts scientifiques se développent également ; en retour, l'apparition des concepts scientifiques influe sur le niveau des concepts spontanés déjà formés."
                },
                "answer": "D"
            }
        ]
    },

    # =========================================================================
    # 2. 2016-2017 – Session 1
    # =========================================================================
    {
        "document": "2016-2017 – Session 1",
        "source": "Annale 301 - 2016-2017 Session 1.pdf",
        "questions": [
            {
                "q_num": 1,
                "theme": "Ch. 1 (1.2) Relations apprentissage et développement : Skinner",
                "question": "Quand on s’intéresse aux relations entre développement et apprentissage, il existe un type de théories fondé sur le présupposé selon lequel l’apprentissage « est » le développement. Il s’agit de la théorie :",
                "options": {
                    "A": "behavioriste de Burrhus Skinner",
                    "B": "personnalité d’Henri Wallon",
                    "C": "historico-culturelle de Lev Vygotsky",
                    "D": "innéiste de Noam Chomsky",
                    "E": "opératoire de Jean Piaget"
                },
                "answer": "A"
            },
            {
                "q_num": 2,
                "theme": "Ch. 2 (2.2) Perceptions et mémoire fœtales",
                "question": "Des recherches récentes sur le fœtus ont montré que :",
                "options": {
                    "A": "le fœtus perçoit des caractéristiques de son environnement mais ne peut pas les mémoriser",
                    "B": "le fœtus perçoit, mémorise et apprend uniquement ce qu’il préfère",
                    "C": "le fœtus perçoit et mémorise des caractéristiques de son environnement ; par exemple il discrimine la voix masculine et la voix féminine",
                    "D": "le fœtus perçoit, mémorise et apprend uniquement ce qui provient de sa mère"
                },
                "answer": "C"
            },
            {
                "q_num": 3,
                "theme": "Ch. 3 (3.2) Phénomène d'habituation",
                "question": "Qu’est-ce que le phénomène d’habituation ?",
                "options": {
                    "A": "on peut y voir une forme élémentaire d’apprentissage non associatif qui désencombre l’organisme de réponses qui se révèlent inutiles tout en préservant sa réactivité initiale à l’apparition du stimulus",
                    "B": "cela désigne généralement un comportement acquis, ayant atteint un certain niveau d’automaticité et dans le registre des conduites motrices plutôt que psychophysiques",
                    "C": "c’est un mode d’apprentissage dominant chez le bébé qui repose sur les perceptions",
                    "D": "c’est l’atténuation, pouvant aller jusqu’à la disparition d’une réponse par répétition du stimulus qui la provoque",
                    "E": "le conditionnement est un exemple e phénomène d’habituation"
                },
                "answer": "C, D"
            },
            {
                "q_num": 4,
                "theme": "Ch. 3 (3.3) Perception visuelle chez le nourrisson",
                "question": "Concernant la perception visuelle chez le nourrisson, celui-ci préfère regarder :",
                "options": {
                    "A": "le visage humain plutôt que d’autres types de figures",
                    "B": "un objet en mouvement plutôt que statique",
                    "C": "le visage de sa mère plutôt que celui d’un autre individu",
                    "D": "une image extrêmement simple plutôt qu’extrêmement complexe",
                    "E": "un être humain plutôt qu'un objet physique"
                },
                "answer": "B, C, E"
            },
            {
                "q_num": 5,
                "theme": "Ch. 3 (3.2) Préférence visuelle et temps de fixation relatif",
                "question": "Un chercheur souhaite déterminer à partir de quel âge les enfants sont capables de reconnaître les peluches qui sont présentes dans leur quotidien. Il cherche pour cela à mesurer chez les enfants le temps de fixation relatif d’une peluche familière et d’une peluche nouvelle. Le premier enfant (4 mois) regarde aussi longtemps les deux peluches. Que peut-on en déduire ?",
                "options": {
                    "A": "le développement socioaffectif est trop limité à 4 mois pour que l’enfant investisse la peluche comme un objet d’intérêt, voire comme un objet transitionnel",
                    "B": "on ne peut rien conclure : il se peut que l’enfant ne reconnaisse pas la peluche familière ou qu’il la reconnaisse sans avoir de préférence visuelle manifeste",
                    "C": "seule la réalisation de mesures physiologiques (rythme cardiaque) permettra d’établir des conclusions fiables",
                    "D": "le bébé a des problèmes de vision qui ne lui permettent pas de discriminer les deux peluches"
                },
                "answer": "B"
            },
            {
                "q_num": 6,
                "theme": "Ch. 3 (3.2) Événement impossible et permanence de l'objet : Baillargeon",
                "question": "Renée Baillargeon a montré en utilisant un paradigme schématisé que l’enfant de 5 mois regarde plus longtemps l’événement impossible que l’événement possible. Que peut-on dire du résultat ?",
                "options": {
                    "A": "l’enfant de 5 mois connait certaines propriétés du monde physique dans lequel il se développe.",
                    "B": "les indices perceptifs sont importants lorsqu’on étudie le jeune enfant",
                    "C": "tant que l’enfant ne dispose pas du langage, on ne peut rien conclure",
                    "D": "on ne peut pas évacuer l’hypothèse selon laquelle c’est uniquement le mouvement de l’objet qui intéresse l’enfant à cet âge."
                },
                "answer": "A, B"
            },
            {
                "q_num": 7,
                "theme": "Ch. 3 (3.4) Théorie de l'attachement : situation étrange (Ainsworth)",
                "question": "En recréant la situation étrange de Mary Ainsworth à son domicile, un étudiant en psychologie cherche à évaluer la nature de l’attachement dont fait preuve son enfant de 12 mois envers lui. Lorsqu’il quitte la pièce et laisse l’enfant en présence d’une personne familière, l’enfant ne pleure pas et continue à explorer ses jouets. Que peut-on en penser ?",
                "options": {
                    "A": "l’enfant a un attachement de type anxieux-évitant avec son père car il ne montre pas de signe de tristesse ou de détresse à son départ",
                    "B": "on ne peut guère conclure car l’enfant est dans un environnement familier (à son domicile, avec ses jouets)",
                    "C": "tous les enfants de cet âge auraient réagi de la même manière avec leur père ; il fait réessayer avec la mère pour pouvoir conclure parce qu’elle est la seule figure d’attachement privilégiée à cet âge",
                    "D": "le dispositif expérimental de la situation étrange n’est pas approprié pour étudier la qualité du lien d’attachement à cet âge"
                },
                "answer": "B"
            },
            {
                "q_num": 8,
                "theme": "Ch. 4 (4.4) Développement du langage : erreurs chronologiques",
                "question": "Dans l’organisation chronologique du développement du langage proposée ci-dessous, toutes les erreurs sont à cocher :",
                "options": {
                    "A": "à la naissance, le bébé distingue la parole humaine des autres sons",
                    "B": "vers l’âge d’un an, il pointe les objets de l’index pour inciter les adultes à les nommer",
                    "C": "ensuite il se met à babiller pour se mémoriser ces nouveaux mots",
                    "D": "vers 19 mois le bébé sait dire plus d’une centaine de mots différents",
                    "E": "les toutes premières phrases de l’enfant sont construites à partir d’une succession hasardeuse des mots entendus"
                },
                "answer": "C, E"
            },
            {
                "q_num": 9,
                "theme": "Ch. 1 (1.3) Méthodologies de recueil de données : méthode mixte",
                "question": "Des chercheurs ont décidé d’étudier le développement de l’humour chez des enfants entre 3 et 6 ans. Pour ce faire, ils ont suivi pendant 6 mois deux classes de 25 élèves d’une école de maternelles lors de la lecture d’ouvrages humoristiques par les maîtresses. Comment s’appelle ce type de méthode en psychologie ?",
                "options": {
                    "A": "la méthode catégorielle",
                    "B": "la méthode clinique",
                    "C": "la méthode longitudinale",
                    "D": "la méthode mixte (ou trans-séquentielle)",
                    "E": "la méthode transversale"
                },
                "answer": "D"
            },
            {
                "q_num": 10,
                "theme": "Ch. 3 (3.5) Notions piagétiennes : le schème",
                "question": "Qu’est-ce qu’un schème au sens piagétien ?",
                "options": {
                    "A": "ce sont des organisations sous tendant les actions permettant à la fois la répétition de ces actions dans des situations analogues, leur généralisation par application à des objets de plus en plus variés et la structuration des connaissances par attribution de significations fonctionnelles aux objets manipulés.",
                    "B": "c’est ce qui structure la conduite à tous les niveaux du développement cognitif",
                    "C": "le schème s’élabore par imitation, d'abord immédiate, puis différée des modèles humains importants pour l’enfant",
                    "D": "c’est en quelque sorte le canevas des actions susceptibles d’être répétées activement"
                },
                "answer": "A, B, D"
            },
            {
                "q_num": 11,
                "theme": "Ch. 4 (4.3) Théorie de l'esprit",
                "question": "Comment s’appelle la capacité à attribuer des désirs, des intentions, des croyances à autrui, à différencier ses propres états mentaux de ceux des autres et à inférer les comportements d’autrui à partir de la connaissance de leurs états mentaux. Il s’agit de :",
                "options": {
                    "A": "l'équilibration",
                    "B": "l'égocentrisme",
                    "C": "la théorie de l'esprit",
                    "D": "la réversibilité",
                    "E": "l'animisme"
                },
                "answer": "C"
            },
            {
                "q_num": 12,
                "theme": "Ch. 1 (1.2) Épistémologie génétique de Piaget",
                "question": "Cocher toutes les propositions correctes définissant l’épistémologie génétique :",
                "options": {
                    "A": "c’est l’étude des conditions de possibilité et de la formation, de la connaissance",
                    "B": "c’est l’étude du rôle des gènes dans le développement de l’intelligence",
                    "C": "c’une théorie de l’accroissement des connaissances depuis les formes élémentaires jusqu’aux formes supérieures",
                    "D": "c’est l’étude de la connaissance humaine en tant qu’elle est performée dans les objets ainsi que dans les individus",
                    "E": "c’est en terme biologique que Piaget décrit l’intelligence dans son fonctionnement et en terme logique qu’il caractérise ses structures"
                },
                "answer": "A, C, E"
            },
            {
                "q_num": 13,
                "theme": "Ch. 3 (3.5) Processus d'adaptation : accommodation",
                "question": "Le même terme à trouver s’applique aux conduites suivantes : l’... est le processus par lequel l’organisme se modifie pour s’adapter ; l’enfant, obligé de s’adapter à une situation nouvelle, transforme ses schèmes antérieurs et en élabore de nouveaux, plus adéquats, d'abord par tâtonnement, puis par invention spontanée grâce à l’... de même, le chercheur qui abandonne une première hypothèse contredite par l’expérience et qui, guidé par les résultats de cette dernière, se met en quête d’une nouvelle hypothèse, procède encore par...",
                "options": {
                    "A": "accommodation",
                    "B": "tentionnalité",
                    "C": "assimilation",
                    "D": "équilibration",
                    "E": "imitation"
                },
                "answer": "A"
            },
            {
                "q_num": 14,
                "theme": "Ch. 1 (1.3) Méthode clinique piagétienne / exploration critique",
                "question": "La méthode d’entretien clinique (ou d’exploration critique) élaborée par Piaget consiste à :",
                "options": {
                    "A": "questionner l'enfant dans le but de recueillir son raisonnement spontané",
                    "B": "poser à l'enfant des questions standardisées",
                    "C": "formuler des contre-suggestions pour tenter de saisir la structure de la pensée de l'enfant",
                    "D": "questionner l'enfant en lui demandant systématiquement de justifier sa réponse",
                    "E": "formuler après chaque réponse de l'enfant une contre suggestion de façon systématique"
                },
                "answer": "A, C, D"
            },
            {
                "q_num": 15,
                "theme": "Ch. 4 (4.4) Le langage égocentrique",
                "question": "Cochez toutes les propositions correctes qui caractérisent le langage égocentrique :",
                "options": {
                    "A": "la répétition de syllabes ou de mots pour le plaisir et sans s'adresser à quelqu'un est une forme de langage égocentrique",
                    "B": "dans le langage égocentrique, il n'y a pas de fonction sociale des mots",
                    "C": "pour Vygotsky, le langage égocentrique s'intériorise et devient une sorte d'intermédiaire entre le langage social et le langage intérieur",
                    "D": "pour Piaget, le langage égocentrique disparaît au cours du développement psychologique",
                    "E": "pour Vygotski, le langage égocentrique a une fonction d'orientation et de planification de l'action"
                },
                "answer": "A, B, D, E"
            },
            {
                "q_num": 16,
                "theme": "Ch. 5 (5.3) Zone proximale de développement (Vygotski)",
                "question": "Cochez toutes les propositions correctes qui définissent la notion de « zone proximale de développement » :",
                "options": {
                    "A": "cette notion rend compte du fait que le jeune enfant construit progressivement un modèle interne des personnes proches de lui et avec lesquelles il a construit un lien d'attachement",
                    "B": "cette notion se définit comme l'écart entre ce que l'enfant sait faire seul et ce qu'il sait faire avec l'aide d'une personne plus compétente que lui",
                    "C": "cette notion se définit comme la proximité physique requise entre la mère et l'enfant afin que tous les deux puissent prêter attention au même objet",
                    "D": "c'est une notion proposée par John Bolwby",
                    "E": "c'est une notion proposée par Lev Vygotsky"
                },
                "answer": "B, E"
            },
            {
                "q_num": 17,
                "theme": "Ch. 5 (5.2) Épreuve d'inclusion piagétienne",
                "question": "On présente à un enfant de 6 ans un bracelet composé de 8 grosses perles en plastique rouge et de 2 grosses perles en plastique jaune. On lui demande : « Y a-t-il plus de perles rouges ou plus de perles plastique ? ». Il répond « plus de perles rouges parce qu’elle celles en plastique, il n’y en a que 2 ». On l’interroge : « Mais les rouges ne sont-elles pas aussi en plastique ? ». L’enfant précise : « Ah oui ! ». On demande : « Alors, est-ce qu’il y a plus de rouges ou plus de perles en plastique ? ». L’enfant conclut : « plus de rouge ». Que peut-on en conclure ?",
                "options": {
                    "A": "l'enfant est certainement capable de manier correctement les quantificateurs « tous » et « quelques »",
                    "B": "l'enfant ne comprend pas la composition additive des classes",
                    "C": "l'enfant reste prisonnier des données perceptives",
                    "D": "l'enfant raisonne de manière opératoire par réversibilité"
                },
                "answer": "B, C"
            },
            {
                "q_num": 18,
                "theme": "Ch. 5 (5.5) Développement moral selon Piaget",
                "question": "Quelles sont les propositions correctes relatives à la conception piagétienne du développement moral ?",
                "options": {
                    "A": "l’enfant conçoit d’abord les normes comme relevant d’un choix personnel avant de considérer comme venant de l’extérieur et auxquelles on doit obéir.",
                    "B": "le réalisme moral s'oppose aux jugement qui prennent en compte l’intention du protagoniste de l’histoire",
                    "C": "les jeunes enfants (dès 6 ans) peuvent faire des choix moraux corrects mais l’explication de leurs jugements est postérieure et évolue",
                    "D": "l’hétéronomie signifie que l'enfant considère qu'il peut choisir de respecter ou de ne pas respecter les règles ou les normes",
                    "E": "en moyenne, les enfants âgés de 10-11 ans fondent leurs jugements sur la gravité matérielle de l’action (ou responsabilité objective)"
                },
                "answer": "B, C"
            },
            {
                "q_num": 19,
                "theme": "Ch. 5 (5.4) Conflit sociocognitif (Doise, Mugny)",
                "question": "La notion de conflit sociocognitif se définit par les propositions suivantes :",
                "options": {
                    "A": "il s'agit d'une conflit social caractérisé par la compétition des partenaires.",
                    "B": "il s'agit de la thèse selon laquelle les interactions sociales peuvent accélérer la genèse des structures de la pensée.",
                    "C": "ce sont des études qui analysent exclusivement les interactions asymétriques enfant/adulte.",
                    "D": "la complaisance vis-à-vis du partenaire fait partie des caractéristiques interactionnelles favorables aux progrès cognitifs.",
                    "E": "les progrès cognitifs s'expliquent par le dépassement à la fois d’un déséquilibre interindividuel et d’un déséquilibre intra-individuel."
                },
                "answer": "B, E"
            },
            {
                "q_num": 20,
                "theme": "Ch. 5 (5.4) Marquage social (Doise, Mugny)",
                "question": "Cochez toutes les propositions correctes qui définissent la notion de « marquage social » :",
                "options": {
                    "A": "il s'agit d’une situation de raisonnement à propos d’une tâche qui repose sur des normes ou des règles ou des conventions sociales.",
                    "B": "il s’agit d’une sorte de pacte, explicite ou implicite, qui règle les attentes mutuelles et spécifiques des partenaires dans un contexte social précis.",
                    "C": "placé dans une situation marquée socialement, l'enfant va produire une réponse correcte parce qu'il respecte une règle sociale qu'il connaît bien alors que ses schèmes cognitifs ne lui permettent pas de résoudre la même tâche présentée de manière abstraite.",
                    "D": "il s’agit d'un processus adaptatif qui s’observe au cours d’une période sensible du développement psychologique"
                },
                "answer": "A, B, C"
            }
        ]
    },

    # =========================================================================
    # 3. 2016-2017 – Session 2 (Annale 301 - 2016-2017.pdf)
    # =========================================================================
    {
        "document": "2016-2017 – Session 2",
        "source": "Annale 301 - 2016-2017.pdf",
        "questions": [
            {
                "q_num": 1,
                "theme": "Ch. 1 (1.2) Nativisme et modularité de l'esprit",
                "question": "Cette conception du développement humain s’intéresse aux caractéristiques de l’espèce (humaine) et aux lois générales qui gouvernent son fonctionnement ; les « organes » mentaux sont déterminés génétiquement et sont propres à l’espèce de telle sorte que le nourrisson possède des connaissances de base du monde. Il s’agit de la conception :",
                "options": {
                    "A": "associationniste",
                    "B": "constructiviste",
                    "C": "historico-culturelle",
                    "D": "nativiste",
                    "E": "structuraliste"
                },
                "answer": "D"
            },
            {
                "q_num": 2,
                "theme": "Ch. 1 (1.3) Méthodologies : méthode mixte (trans-séquentielle)",
                "question": "Cette méthode utilisée en psychologie du développement permet de vérifier que les évolutions observées au niveau des groupes transversaux se retrouvent bien au niveau des individus. Une de ces limites concerne la « fonte » de l’échantillon. Il s’agit de la méthode :",
                "options": {
                    "A": "catégorielle",
                    "B": "longitudinale",
                    "C": "mixte (ou trans-séquentielle)",
                    "D": "psychométrique",
                    "E": "transversale"
                },
                "answer": "C"
            },
            {
                "q_num": 3,
                "theme": "Ch. 2 (2.1) & Ch. 1 (1.2) Développement cérébral et néoténie",
                "question": "Concernant le développement cérébral chez l’être humain, cochez toutes les propositions correctes :",
                "options": {
                    "A": "La croissance cérébrale va nécessiter au moins vingt années pour s’« achever » (contre deux années chez le chimpanzé).",
                    "B": "Vers l’âge de 9-10 ans, le cerveau représente 90% du volume du cerveau adulte.",
                    "C": "La construction du cerveau n’est jamais totalement achevée, même à l’âge adulte.",
                    "D": "Ce développement cérébral très lent fait partie des caractéristiques néoténiques chez l’être humain."
                },
                "answer": "A, C, D"
            },
            {
                "q_num": 4,
                "theme": "Ch. 3 (3.5) Processus d'adaptation : assimilation",
                "question": "Le même terme à trouver s’applique aux conduites suivantes : Lorsqu’un bébé applique au mamelon du sein, puis à son pouce ou à une tétine le schème de succion, il y a .................... ; l’enfant qui, en jouant, applique un schème pratique de la « chevauchée » en se mettant à califourchon sur un manche à balai supposé représenter un cheval constitue un autre exemple d’.................... de caractère symbolique ; le chercheur qui va au devant de données empiriques armé d’une hypothèse procède encore, à un niveau supérieur, par .................... :",
                "options": {
                    "A": "accommodation",
                    "B": "intentionnalité",
                    "C": "assimilation",
                    "D": "équilibration",
                    "E": "imitation"
                },
                "answer": "C"
            },
            {
                "q_num": 5,
                "theme": "Ch. 3 (3.5) Réactions circulaires primaires (sous-stade 2)",
                "question": "Voici un extrait des observations réalisées par Piaget : « Laurent est tenu par sa garde, peu avant le repas, en position presque verticale. Il a très faim et cherche à téter, la bouche ouverte, avec des rotations continuelles de la tête. Ses bras décrivent des grands mouvements rapides et viennent sans cesse heurter son visage. A deux reprises, sa main étant appliquée un instant contre la joue droite, Laurent tourne la tête et tend à saisir ses doigts avec sa bouche. Il échouera la première fois et réussit la seconde. Mais les mouvements du bras ne sont pas coordonnés par rapport à ceux de la tête : la main s’échappe tandis que la bouche essaie de maintenir le contact. Dans la suite cependant, il parvient à attraper son pouce ». Cet exemple illustre pour Piaget les réactions circulaires primaires. Qu’est-ce que cela implique ?",
                "options": {
                    "A": "Laurent a nécessairement plus de 6 mois dans cet exemple.",
                    "B": "Cette conduite est observée au stade sensori-moteur.",
                    "C": "Laurent répète des schèmes qu’il a découverts par hasard sur son corps.",
                    "D": "Laurent découvre ce qu’on appelle l’erreur A non-B.",
                    "E": "Laurent devient capable de trouver des moyens nouveaux par combinaisons intériorisées qui aboutissent à une compréhension soudaine ou insight."
                },
                "answer": "B, C"
            },
            {
                "q_num": 6,
                "theme": "Ch. 4 (4.2) Fonction sémiotique",
                "question": "Vers l’âge de 18-24 mois apparaissent en même temps le langage, le jeu symbolique, les images mentales, le dessin et l’imitation différée. Toutes ces activités mentales ont en commun de représenter une chose en son absence par le moyen d’un symbole ou d’un signe au sens strict. Comment désigne-t-on ce type de nouvelles compétences en psychologie du développement ?",
                "options": {
                    "A": "La centration cognitive",
                    "B": "La fonction sémiotique",
                    "C": "Le langage égocentrique",
                    "D": "Le signifiant",
                    "E": "La fonction exécutive"
                },
                "answer": "B"
            },
            {
                "q_num": 7,
                "theme": "Ch. 3 (3.4) Théorie de l'attachement (Bowlby)",
                "question": "Cochez toutes les propositions correctes qui définissent la notion d’« attachement » :",
                "options": {
                    "A": "C’est un besoin dérivé de la nécessité de se nourrir.",
                    "B": "C’est un besoin inné.",
                    "C": "L’attachement a une fonction de protection.",
                    "D": "Le bébé recherche le contact physique avec autrui.",
                    "E": "Plus l’attachement est sécurisé, plus l’enfant part explorer le monde environnant."
                },
                "answer": "B, C, D, E"
            },
            {
                "q_num": 8,
                "theme": "Ch. 4 (4.1) & Ch. 5 (5.1) Théorie wallonienne : stades et lois",
                "question": "Cochez toutes les propositions correctes caractérisant la théorie wallonienne du développement psychologique :",
                "options": {
                    "A": "Chaque stade wallonien est caractérisé par une orientation qui permet alternativement soit l’édification du sujet lui-même (centripète) soit l’établissement de ses relations avec l’extérieur (centrifuge).",
                    "B": "Selon Wallon, les émotions ne constituent que l’énergétique du développement psychologique et n’ont qu’un impact secondaire sur la construction des structures de la personnalité.",
                    "C": "Wallon a mis l’accent sur le rôle du mouvement dans le développement psychologique, en insistant sur deux fonctions différentes du mouvement : l’effection et l’expression.",
                    "D": "Wallon défend la thèse de la continuité du développement psychologique et de la recherche de l’équilibre interne de la personne, chaque stade intégrant de manière hiérarchique les caractéristiques du stade précédent.",
                    "E": "Wallon distingue trois types de milieux - le milieu humain, le milieu physique et le milieu symbolique (ou sémiotique) qui participent à la construction (de 0 à 3 ans) et à l’achèvement de la personne (de 6 ans à l’adolescence)."
                },
                "answer": "A, C, E"
            },
            {
                "q_num": 9,
                "theme": "Ch. 4 (4.3) Théorie de l'esprit : tâche de fausse croyance",
                "question": "Un psychologue développementaliste montre à un enfant de 3 ans une boîte de chocolats et lui demande ce qu’il pense y trouver. Sa réponse spontanée est « Des chocolats ! » L’enfant ouvre la boîte et, à sa grande surprise, constate qu’elle contient une balle de tennis. L’expérimentateur lui demande alors : « Que va penser ta sœur du contenu de la boîte si elle n’a pas regardé à l’intérieur ? ». Quelle réponse va certainement donner cet enfant ?",
                "options": {
                    "A": "Cet enfant va répondre : « Ma sœur va penser qu'il y a des chocolats ».",
                    "B": "Cet enfant va répondre : « Ma sœur va penser qu'il y a une balle de tennis ».",
                    "C": "Cet enfant va répondre : « Ma sœur va penser que cette boîte est vide ».",
                    "D": "Cet enfant va répondre : « je ne sais pas »."
                },
                "answer": "B"
            },
            {
                "q_num": 10,
                "theme": "Ch. 4 (4.3) Théorie de l'esprit : conclusion de l'expérimentateur",
                "question": "Que va alors conclure l’expérimentateur ?",
                "options": {
                    "A": "L’expérimentateur va conclure que cet enfant se situe au stade sensorimoteur du point de vue cognitif.",
                    "B": "L’expérimentateur va conclure que cet enfant comprend que les représentations mentales peuvent différer de la réalité.",
                    "C": "L’expérimentateur va conclure que cet enfant ne semble pas concevoir que lui-même ou les autres puissent avoir des fausses croyances.",
                    "D": "L’expérimentateur va conclure que l’enfant a construit une pensée formelle."
                },
                "answer": "C"
            },
            {
                "q_num": 11,
                "theme": "Ch. 4 (4.1) Wallon : stade du personnalisme",
                "question": "Selon Wallon, une période d’opposition suivie d’une phase dite « âge de grâce » puis d’une période dite « âge de l’imitation » caractérise les conduites de l’enfant entre 3 et 6 ans, il s’agit du :",
                "options": {
                    "A": "stade émotionnel",
                    "B": "stade catégoriel",
                    "C": "stade du personnalisme",
                    "D": "stade de l’impulsivité motrice",
                    "E": "stade sensorimoteur et projectif"
                },
                "answer": "C"
            },
            {
                "q_num": 12,
                "theme": "Ch. 4 (4.4) Formats d'interaction et routines (Bruner)",
                "question": "Les savoir-faire communicatifs s’élaborent dans le cadre de routines interactives qui constituent des formes de proto-dialogues précurseurs de l’entrée dans l’acte de parole. Cette notion a été proposée par Garvey (1974) puis reprise par Bruner. Il s’agit de la notion de :",
                "options": {
                    "A": "contexte d'interaction",
                    "B": "contre-suggestion",
                    "C": "croyances déclenchées",
                    "D": "format d'interaction",
                    "E": "modalité d'interaction"
                },
                "answer": "D"
            },
            {
                "q_num": 13,
                "theme": "Ch. 4 (4.4) Fonction première du langage selon Vygotski",
                "question": "Selon Vygotsky, quelle est la première fonction du langage qui se met en place au cours du développement psychologique ?",
                "options": {
                    "A": "La fonction adaptative",
                    "B": "La fonction communicative",
                    "C": "La fonction exécutive",
                    "D": "La fonction représentative",
                    "E": "La fonction de planification"
                },
                "answer": "B"
            },
            {
                "q_num": 14,
                "theme": "Ch. 4 (4.5) Dessin : réalisme intellectuel (Luquet)",
                "question": "Un chercheur a décrit le développement de l’activité graphique de l’enfant en plusieurs stades. L’un d’entre eux est appelé « réalisme intellectuel ». Quelle est la conduite enfantine caractéristique de ce stade ?",
                "options": {
                    "A": "L’enfant dessine ce qu’il voit et non ce qu’il sait de l’objet.",
                    "B": "L’enfant dessine ce qu’il sait et non ce qu’il voit de l’objet.",
                    "C": "L’enfant ne parvient pas à dessiner le thème qu’il a annoncé avant de dessiner.",
                    "D": "L’enfant dessine la perspective."
                },
                "answer": "B"
            },
            {
                "q_num": 15,
                "theme": "Ch. 4 (4.5) Dessin : Luquet",
                "question": "Quel est le chercheur en question ?",
                "options": {
                    "A": "Le chercheur est Elisabeth Spelke",
                    "B": "Le chercheur est Florence Laura Goodenough",
                    "C": "Le chercheur est George-Henri Luquet",
                    "D": "Le chercheur est Jacqueline Royer"
                },
                "answer": "C"
            },
            {
                "q_num": 16,
                "theme": "Ch. 5 (5.2) Opération mentale selon Piaget",
                "question": "Cochez toutes les propositions correctes qui caractérisent ce qu’est l’« opération mentale » selon Piaget : l’opération mentale correspond à :",
                "options": {
                    "A": "des croyances déclenchées.",
                    "B": "des actions intériorisées non réversibles.",
                    "C": "des actions intériorisées isolées.",
                    "D": "des actions intériorisées qui sont comprises comme pouvant s'opérer dans les deux sens.",
                    "E": "des actions intériorisées groupées en systèmes cohérents."
                },
                "answer": "D, E"
            },
            {
                "q_num": 17,
                "theme": "Ch. 1 (1.4) Niveaux d'analyse de Doise : niveau positionnel",
                "question": "Imaginez un enfant en train de résoudre un problème de division. Pour expliquer les conduites de cet enfant, le chercheur va invoquer le fait qu’il s’agit d’un élève en échec scolaire et notamment dans la discipline mathématique. Du point de vue de la classification de Doise (1982), le niveau d'analyse retenu par ce chercheur est :",
                "options": {
                    "A": "le niveau 1 ou intra-individuel",
                    "B": "le niveau 2 ou interindividuel",
                    "C": "le niveau 3 ou positionnel",
                    "D": "le niveau 4 ou idéologique"
                },
                "answer": "C"
            },
            {
                "q_num": 18,
                "theme": "Ch. 5 (5.3) Désaccord Piaget et Vygotski",
                "question": "Cochez toutes les propositions sur lesquelles Piaget et Vygotski sont en désaccord :",
                "options": {
                    "A": "Les capacités psychologiques humaines se construisent.",
                    "B": "C’est à partir d’un ensemble d’adaptations culturelles artificielles qui visent à contrôler les processus psychiques que se construisent les conduites humaines.",
                    "C": "L’enfant est capable de construire des concepts à partir de ses expériences quotidiennes.",
                    "D": "Il est fondamental de distinguer les concepts spontanés et les concepts scientifiques pour expliquer le développement cognitif.",
                    "E": "L’apprentissage précède le développement."
                },
                "answer": "B, D, E"
            },
            {
                "q_num": 19,
                "theme": "Ch. 5 (5.4) Conflit sociocognitif : rôle du partenaire",
                "question": "Quand un enfant donne une réponse incorrecte à un problème de logique, il a été montré qu’un conflit sociocognitif peut lui permettre de progresser dans son raisonnement en construisant une solution plus élaborée avec un pair que tout seul. Pour cela, il faut que le partenaire de l’enfant :",
                "options": {
                    "A": "propose une réponse incorrecte et contradictoire à celle de l’enfant, du type : « tu dis qu’il y a plus de pâte à modeler dans la galette que dans la boule ; je ne suis pas d’accord : il y a plus de pâte dans la boule que dans la galette parce que... ».",
                    "B": "propose une réponse différente en précisant : « je connais la réponse parce que je suis plus grand que toi ».",
                    "C": "propose une réponse différente en précisant : « c'est mon papa qui me l'a dit ».",
                    "D": "propose la réponse correcte en justifiant celle-ci."
                },
                "answer": "A, D"
            },
            {
                "q_num": 20,
                "theme": "Ch. 1 (1.1) Définitions de la psychologie du développement",
                "question": "Cochez toutes les définitions correctes de la « psychologie du développement » :",
                "options": {
                    "A": "Il existe deux ensembles définitionnels de la psychologie du développement : le premier réfère à des transformations endogènes qui relèvent de la maturation du système nerveux central tandis que le second se rapporte à des transformations également internes mais qui relèvent de l’appropriation puis de l’intériorisation d’instruments de pensée produits par autrui.",
                    "B": "Il s'agit d'une notion très générale qui désigne l'ensemble des processus de transformation qui affectent soit les organismes vivants, soit les institutions humaines, soit encore leurs différentes propriétés.",
                    "C": "La psychologie du développement est essentiellement une psychologie comparative.",
                    "D": "La psychologie du développement prescrit des règles éducatives.",
                    "E": "Les changements étudiés par le psychologue du développement relèvent uniquement de l’échelle de temps long."
                },
                "answer": "A, B, C"
            }
        ]
    },

    # =========================================================================
    # 4. 2018-2019 – Session 2
    # =========================================================================
    {
        "document": "2018-2019 – Session 2",
        "source": "Annale 301 - 2018-2019 Session 2.pdf",
        "questions": [
            {
                "q_num": 1,
                "theme": "Ch. 1 (1.2) Épistémologie : constructivisme piagétien",
                "question": "Selon cette conception psychologique, les connaissances ne peuvent ni résulter d’une simple copie de l’organisation du monde extérieur comme le soutient l’empirisme, ni se trouver déposées dans notre esprit par une forme quelconque de la transcendance ou de l’immanence comme le prétendait l’innéisme. Il s’agit de la conception :",
                "options": {
                    "A": "associationniste",
                    "B": "nativiste",
                    "C": "behavioriste",
                    "D": "constructiviste",
                    "E": "préformiste"
                },
                "answer": "D"
            },
            {
                "q_num": 2,
                "theme": "Ch. 3 (3.5) Schème, assimilation et accommodation",
                "question": "Le même terme à trouver s’applique aux conduites suivantes : Le passage du réflexe au ............. se fait par intégration au réflexe d’éléments sensorimoteurs nouveaux et jusque-là indépendants, grâce au processus d’assimilation. En s’appliquant à des objets nouveaux, le ............. tend à s’enrichir de nouvelles structures d’action. Lorsque l’enfant entre en contact avec des objets auxquels les .......... dont ils disposent ne parviennent pas à s’appliquer, il est conduit à les modifier et les diversifier de façon plus fine, grâce au processus d’accommodation.",
                "options": {
                    "A": "Comportement",
                    "B": "Schème",
                    "C": "Concept",
                    "D": "Schéma",
                    "E": "Format"
                },
                "answer": "B"
            },
            {
                "q_num": 3,
                "theme": "Ch. 3 (3.3) Perception de la parole chez le nourrisson",
                "question": "Cochez toutes les propositions correctes qui caractérisent la perception de la parole chez le nourrisson :",
                "options": {
                    "A": "Le nourrisson de 1 à 2 mois est capable de discriminer des sons proches (comme « b » et « p ») des langages humains, quelles que soient les paroles qu’il entend.",
                    "B": "Le nourrisson préfère les paroles prononcées par sa mère à celles prononcées par une autre femme.",
                    "C": "La compétence à discriminer des sons proches (comme « b » et « p ») des langages humains, quelles que soient les paroles qu’il entend, augmente avec l’âge."
                },
                "answer": "A, B"
            },
            {
                "q_num": 4,
                "theme": "Ch. 3 (3.4) Théorie de l'attachement (Bowlby)",
                "question": "Cochez toutes les propositions correctes qui définissent la notion d’attachement :",
                "options": {
                    "A": "L’attachement est défini comme un équilibre entre les comportements d’attachement envers les figures parentales et les comportements d’exploration du milieu.",
                    "B": "C’est une assimilation entre les comportements d’attachement envers la mère uniquement et les comportements de protection.",
                    "C": "Le lien d’attachement constitue un lien affectif stable qui tend à s’intérioriser et à servir de modèle comportemental dans les relations sociales de l’enfant.",
                    "D": "L’attachement est un besoin construit à partir du besoin fondamental d’être nourri."
                },
                "answer": "A, C"
            },
            {
                "q_num": 5,
                "theme": "Ch. 4 (4.4) Acquisition du langage : LAD de Chomsky",
                "question": "Pour rendre compte du développement langagier, un chercheur a proposé l’idée qu’une structure appelée LAD (Language Acquisition Device) permet à l’individu de produire des phrases qu’il n’a jamais entendues et de commettre des erreurs jamais entendues mais qui suivent des règles générales de dérivation de sa langue. Quel est le chercheur qui a proposé ce type d’explication ?",
                "options": {
                    "A": "Jérôme Bruner",
                    "B": "Noam Chomsky",
                    "C": "Lev Vygotski",
                    "D": "John Bowlby",
                    "E": "Jean Piaget"
                },
                "answer": "B"
            },
            {
                "q_num": 6,
                "theme": "Ch. 1 (1.2) & Ch. 4 (4.4) Innéisme linguistique",
                "question": "De quel type d’explication s’agit-il (concernant la théorie du LAD de Chomsky) ?",
                "options": {
                    "A": "l’explication empiriste",
                    "B": "l’explication innéiste",
                    "C": "l’explication constructiviste",
                    "D": "l’explication socio-pragmatique"
                },
                "answer": "B"
            },
            {
                "q_num": 7,
                "theme": "Ch. 4 (4.2) & (4.4) Égocentrisme intellectuel et verbal (Piaget vs Vygotski)",
                "question": "Quelles sont les propositions correctes qui caractérisent la notion d’« égocentrisme » ?",
                "options": {
                    "A": "Il s’agit de la disposition à parler de soi et à rechercher exclusivement son plaisir et son intérêt personnels.",
                    "B": "C’est une conduite qui se traduit par une indifférenciation entre le moi et autrui, entre le sujet et l’objet, ainsi que par une utilisation du langage non dominée par la visée communicative.",
                    "C": "Au sens large, ce terme se réfère à la personnalité de l’enfant et à l’ensemble des représentations conscientes qu’il s’en donne.",
                    "D": "Les manifestations verbales de l’égocentrisme ont fait l’objet d’interprétations très différentes entre Piaget et Vygotski."
                },
                "answer": "B, D"
            },
            {
                "q_num": 8,
                "theme": "Ch. 5 (5.3) Loi générale du développement culturel de Vygotski",
                "question": "Vygotski a énoncé une loi fondamentale du développement psychologique. Quelles sont ses caractéristiques ?",
                "options": {
                    "A": "Cette loi énonce que le développement psychologique va de l’individuel vers le social.",
                    "B": "Selon cette loi, chaque fonction psychologique supérieure apparaît deux fois au cours du développement, d’abord au niveau intra-individuel puis au niveau interindividuel.",
                    "C": "Selon cette loi, chaque fonction psychologique supérieure apparaît deux fois au cours du développement, d’abord au niveau interpsychique puis au niveau intrapsychique.",
                    "D": "Cette loi souligne la nécessaire médiation des interactions humaines pour le développement psychologique de l’enfant."
                },
                "answer": "C, D"
            },
            {
                "q_num": 9,
                "theme": "Ch. 5 (5.3) Développement conceptuel : Piaget vs Vygotski",
                "question": "Au cours de son développement cognitif, l’enfant construit des concepts du type (« frère », « famille », ...) puis des concepts du type (« angle droit », « hypoténuse », ...). Comment les chercheurs expliquent-ils cette progression conceptuelle ?",
                "options": {
                    "A": "Piaget considère que les enfants construisent ces deux types de concepts grâce à leurs actions sur le monde physique, leur maturation biologique, leurs interactions sociales et le processus interne d’équilibration.",
                    "B": "Piaget considère que les enfants construisent ces deux types de concepts grâce à leurs apprentissages scolaires.",
                    "C": "Vygotski considère qu’il y a une rupture développementale dans la construction de ces deux types de concepts.",
                    "D": "Selon Piaget et Vygotski, ces deux types de concepts partent du concret et se transforment progressivement.",
                    "E": "Selon Vygotski, le développement conceptuel, quel que soit le type de concepts, s’élabore grâce aux contextes sociaux d’apprentissage."
                },
                "answer": "A, C, E"
            }
        ]
    }
]

print("Exams Part 1 ready:", len(EXAMS_PART1), "exams.")

