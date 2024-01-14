#  ==============================================================================
#   Copyright (c) 2023 Aymeric Schaeffer et Lise Renaud
#
#   Permission vous est accordée de copier, distribuer et/ou modifier ce code
#   sous les termes de la licence open source.
#
#   Ce programme est distribué dans l'espoir qu'il sera utile, mais SANS
#   AUCUNE GARANTIE ; sans même la garantie implicite de COMMERCIALISATION
#   ou D'ADAPTATION À UN OBJET PARTICULIER. Voir la licence pour plus de détails.
#
#   Vous devriez avoir reçu une copie de la licence avec ce programme. Sinon,
#   consultez.
#  ==============================================================================
import json
import os
from analyse_cge.journalisation.traces import *


def sauvegarder_json(dictionnaire, chemin_json):  # Sauvegarder en fichier json un dictionnaire
    if ".json" not in chemin_json:
        chemin_json += ".json"
        debug(f"Le nom du fichier json à sauvegarder à été modifier en {chemin_json}")

    try:
        with open(chemin_json, 'w') as json_file:
            json.dump(dictionnaire, json_file, indent=4)
            json_file.flush()  # On force a sauvegarder le fichier
            debug(f"Le fichier json à été sauvegardé : {chemin_json}")

    except IOError as err:
        erreur(f"Impossible de créer le fichier {chemin_json}", f"{err}")


def importer_json(chemin_json):
    try:
        with open(chemin_json, 'r') as json_file:
            debug(f"Le fichier {chemin_json} json à été importé")
            return json.load(json_file)

    except IOError as err:
        erreur(f"Impossible d'ouvrir le fichier {chemin_json}", err, f"Fichier de ce répertoire : {os.listdir()}")
        return 1


