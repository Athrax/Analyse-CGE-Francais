from source.gestionnaire_json import importer_json
from source.gestionnaire_arborescence import *
from journalisation.traces import erreur
from sys import exit

chemin_vers_json = chemin("donnees", "db_ministere.json")  # Le chemin est relatif pa rapport à main.py
try:
    db = importer_json(chemin_vers_json)
except FileNotFoundError as err:
    erreur(f"Impossible d'ouvrir la base de donnée", f"Fichier introuvable", err)
    exit(1)