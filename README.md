# Traitement des Données du Bilan Comptable du Compte Général de l'Etat Français

## Description
Ce projet universitaire a été réalisé dans le cadre d'une Situation d'Apprentissage et d'Évaluation (SAÉ) de la formation BUT Réseaux et Télécom, première année. L'objectif principal était de traiter les données du bilan comptable du compte général de l'État, en utilisant des compétences acquises dans le domaine de la programmation et de l'analyse de données.

## Objectif
L'objectif de ce projet était de manipuler et d'exploiter les données d'un fichier CSV contenant toutes les entrées du compte général de l'État. Nous avons choisi le bilan comptable comme sujet d'étude, et notre démarche consistait à trier et à analyser ces données en utilisant des outils informatiques.

## Fonctionnalités
- **Importation des données :** Chargement des données à partir d'un fichier CSV.
- **Traitement et tri des données :** Analyse des entrées du bilan comptable et tri en fonction de différents critères.
- **Exploitation des résultats :** Génération de statistiques, graphiques ou rapports basés sur les données triées.

## Technologies Utilisées
- Python 3.11
- Bibliothèques Python pour le traitement de données (**matplotlib**, numpy, etc.)
- **Flit** pour la gestion des dépendances
- **Gliffy** pour la rédaction d'algorithme

## Bibliothèques Utilisées
- matplotlib.pyplot
- os
- sys
- io
- datetime
- json

## Comment Utiliser
### Avec PyCharm
1. Clônez le dépôt vers votre machine locale.
2. Les dépendances et l'interpréteur s'installent automatiquement. Le cas échéant, assurez-vous d'avoir les dépendances Python installées
3. Exécutez le script principal pour traiter les données du bilan comptable (`analyse-cge/main.py`)
### Depuis un shell macOS ou Linux
1. Clônez le dépôt vers votre machine locale. `git clone https://github.com/Athrax/Analyse-CGE-Francais.git`
2. Déplacez vous a la racine du projet. `cd Analyse-CGE-Francais`
3. Créez l'environnement virtuel de développement. `python3.11 -m venv .venv`
4. Activez le. `source .venv/bin/activate`
5. Installez le gestionnaire de dépendances. `pip install flit `
6. Installez les dépendances. `python -m flit install`
7. Lancez le script. `python3.11 analyse_cge/main.py -nogui`

## Remarques
Ce projet est destiné à des fins éducatives dans le cadre de la formation universitaire. N'hésitez pas à explorer le code source, à suggérer des améliorations ou à poser des questions.

## Auteurs
- Lise Renaud
- Aymeric Schaeffer

## Sources
https://www.budget.gouv.fr

## Licence
Ce projet est sous licence open source - voir le fichier [LICENSE](LICENSE) pour plus de détails.