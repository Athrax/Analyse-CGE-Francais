#  ==============================================================================
#   Copyright (c) 2023 Lise Renaud et Aymeric Schaeffer
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

import matplotlib.pyplot as plt  # graphiques
import numpy as np  # outils mathématiques
from sys import exit  # système
from cli.gestionnaire_arguments import arguments # arguments
from journalisation.traces import info, debug, erreur  # logs
from fichier.gestionnaire_arborescence import parent, grand_parent, chemin
from fichier.detection_donnees import detection_en_tete  # traitement du fichier source
from fichier.gestionnaire_source import regroupe_donnees_ministere
from fichier.gestionnaire_json import sauvegarder_json, importer_json
from cli.menu import cli


def run():
    """
    Fonction principale du logic.
    Executée si main.py n'est pas appelée comme un module
    """

    # On récupère les valeurs passées en arguments

    if not arguments():
        info("Utilisation : main.py -parametres")
        info("Paramètres :",
             "Fichier source : -source \"chemin_vers_fichier_csv\"",
             "Interface en ligne de commande : -nogui",
             "Mode verbeux : -v")
        info("Exemple: main.py -source ../docs/source.csv -nogui")

    # Traitement du fichier source :
    # Si un fichier a été passé en argument lors de l'execution du code,
    # alors on met à jour la base de donnée json
    # sinon, on créer un fichier json avec les données du fichier.

    # Si un argument est donné (fichier source)
    # Alors on créer le dictionnaire des ministères

    elif "-source" in arguments():
        chemin_fichier_source = str(arguments()["-source"])  # On enregistre le chemin du fichier csv
        info("Recherche du fichier passé en argument : {0}".format(chemin_fichier_source))

        try:  # On essaye de charger le fichier de donnees
            fichier_source = open(chemin_fichier_source, "r")
            info("Fichier ouvert avec succès", "Création de la base de donnée à partir de la source ...")

            # On traite le fichier source donné
            colonnes_a_traiter = detection_en_tete(fichier_source)  # On cherche l'indice des colonnes à traiter

            # On regroupe les données par ministère
            db_ministere = regroupe_donnees_ministere(fichier_source, colonnes_a_traiter)  # On créer un dictionnaire
            # On enregistre la base de donnée créée
            sauvegarder_json(db_ministere, chemin(grand_parent(__file__), "docs", "db_ministere.json"))

        except FileNotFoundError:  # Si le fichier n'est pas trouvé
            erreur("Le fichier {0} est introuvable".format(chemin_fichier_source))
            return 2  # Mauvaise utilisation du programme ou erreur d'entrée de l'utilisateur

        except IOError:
            erreur("Le fichier {0} n'est pas lisible".format(chemin_fichier_source))
            return 2  # Erreur générique (non spécifiée)

    # Si aucun chemin vers un fichier source n'a été donné
    # Alors on importe le dictionnaire déja créé

    else:
        try:  # On vérifie si la base de donnée éxiste déja (donnees.json)
            db_ministere = importer_json(chemin_json=chemin(grand_parent(__file__), "docs", "db_ministere.json"))  # On essaye d'ouvrir la base de données (qu'on nommera db)
            debug("Base de donnée json importée")

        except FileNotFoundError:
            erreur("Aucune base de donnée n'existe",
                   "Veuillez executer le logiciel en précisant le chemin vers une source",
                   "Elle doit être au format csv, séparé par des virgules")
            return 2  # Erreur générique (non spécifiée)

    # La base de donnée ministère a été créée ou a été importée
    # On peut maintenant exploiter les données
    # print(arguments())

    # On différencie l'execution en ligne de commande ou par interface graphique
    if "-nogui" in arguments(): # Si l'utilisateur lance le programme en ligne de commande
        cli()
    else:
        #gui()
        pass

    info("Fin du programme")
    return 0  # Fin du programme

if __name__ == '__main__':  # On vérifie si on execute bien le fichier directement et non comme un module
    info("Le programme démarre ...")
    exit(run())  # Si on ne l'execute pas comme un module, alors on démarre notre programme

else:
    erreur("Impossible de démarrer le logiciel en tant que module", "Veuillez executer main.py directement.")
