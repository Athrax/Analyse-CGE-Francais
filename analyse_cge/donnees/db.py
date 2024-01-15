from source.gestionnaire_json import importer_json
from source.gestionnaire_arborescence import *
from journalisation.traces import erreur
from sys import exit

chemin_vers_json_ministere = chemin(parent(__file__), "db_ministere.json")  # Chemin absolu
try:
    db = importer_json(chemin_vers_json_ministere)
except FileNotFoundError as err:
    erreur(f"Impossible d'ouvrir la base de donnée", f"Fichier introuvable", err)
    exit(1)


chemin_vers_json_etat = chemin(parent(__file__), "db_etat.json") # Chemin absolu
try:
    db_etat = importer_json(chemin_vers_json_etat)
except FileNotFoundError as err:
    erreur(f"Impossible d'ouvrir la base de donnée", f"Fichier introuvable", err)
    exit(1)