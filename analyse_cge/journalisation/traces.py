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
from datetime import datetime
import os.path

def log(niveau, message, temps_actuel):
    """
    Fonction permettant d'enregistrer les informations du déroulement du logiciel et de les afficher en console

    Args:
        niveau (string): Niveau de log
        message (tuple): Information à enregistrer
        temps_actuel (datetime): info : 1, avertissement : 2, erreur : 3
    """

    timestamp = int(datetime.timestamp(temps_actuel) * 1000)  # Créer un identifiant unique pour chaque entrée
    date_heure = temps_actuel.strftime("%d-%m-%Y %H:%M:%S")  # Heure et date
    entree = f"{date_heure} [{timestamp}]: {niveau} - {message}"  # On préfère f"" à "".format(), plus facile à lire
    print(entree)  # On affiche dans la console l'info

    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "journalisation", "latest.log"), 'a+') as fichier_log:  # On ouvre le dernier fichier de journalisation ou le créer
        fichier_log.write(entree + "\n")


def info(*message):
    temps_actuel = datetime.now()  # On récupère les données de temps actuel
    for ligne in message:
        log("INFO", ligne, temps_actuel)  # Pour chaque ligne envoyée, on affiche un message


def avert(*message):
    temps_actuel = datetime.now()  # On récupère les données de temps actuel
    for ligne in message:
        log("AVERTISSEMENT", ligne, temps_actuel)


def erreur(*message):
    temps_actuel = datetime.now()  # On récupère les données de temps actuel
    for ligne in message:
        log("ERREUR", ligne, temps_actuel)