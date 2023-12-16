import json
import os

from analyse_cge.journalisation.traces import *


def sauvegarder_json(dictionnaire, chemin_json):  # Sauvegarder en fichier json un dictionnaire
    if ".json" not in chemin_json:
        chemin_json += ".json"
        info(f"Le nom du fichier json à sauvegarder à été modifier en {chemin_json}")

    try:
        with open(chemin_json, 'w') as json_file:
            json.dump(dictionnaire, json_file, indent=4)
            info(f"Le fichier json à été sauvegardé : {chemin_json}")

    except IOError as err:
        erreur(f"Impossible de créer le fichier {chemin_json}", f"{err}")


def importer_json(chemin_json):
    try:
        with open(chemin_json, 'r') as json_file:
            info(f"Le fichier {chemin_json} json à été importé")
            return json.load(json_file)

    except IOError as err:
        print(os.listdir())
        erreur(f"Impossible d'ouvrir le fichier {chemin_json}", f"{err}")
        return 1


