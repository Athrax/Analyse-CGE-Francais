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
- Python
- Bibliothèques Python pour le traitement de données (pandas, matplotlib, etc.)
- Poetry pour la gestion des dépendances
- Gliffy pour la rédaction d'algorithme

## Bibliothèques Utilisées
- matplotlib.pyplot
- os
- sys
- io
- datetime
- json

## Comment Utiliser dans PyCharm
1. Clônez le dépôt vers votre machine locale.
2. Les dépendances et l'interpréteur s'installent automatiquement. Le cas échéant, assurez-vous d'avoir les dépendances Python installées
3. Exécutez le script principal pour traiter les données du bilan comptable (`analyse-cge/main.py`) en utilisant les options nécessaires

## Comment Utiliser dans un terminal
1. Clônez le dépôt vers votre machine locale.
   ```bash
   git clone https://github.com/Athrax/Analyse-CGE-Francais.git
   ```
2. Placez vous dans le dossier du projet
   ```bash
   cd [votre chemin]/Analyse-CGE-Francais
   ```
3. Créez un environnement virtuel pour le projet
   ```bash
   python -m venv .venv
   ```
4. Activez l'environnement virtuel
   ```bash
   source .venv/bin/activate && export PYTHONPATH=./:$PYTHONPATH
   ```
5. Installez les dépendances
   ```bash
   python -m pip install matplotlib
   
   ```
6. Lancer le programme
   ```bash
   python analyse-cge/main.py -nogui
   ```

Vous pouvez recréer la base de donnée a partir du fichier source avec l'option -source suivi du chemin vers le fichier source.csv
Exemple : `python analyse-cge/main.py -nogui -source analyse-cge/source/source.csv`
> **command not found: python**
En fonction de votre système d'exploitation, il se pourrait que la commande pour lancer python puisse être ```python3```, ```python3.9``` ou ```pyhton3.11``` par exemple.


## Remarques
Ce projet est destiné à des fins éducatives dans le cadre de la formation universitaire. N'hésitez pas à explorer le code source, à suggérer des améliorations ou à poser des questions.

## Auteurs
- Lise Renaud
- Aymeric Schaeffer

## Sources
https://www.budget.gouv.fr

## Licence
Ce projet est sous licence open source - voir le fichier [LICENSE](LICENSE) pour plus de détails.