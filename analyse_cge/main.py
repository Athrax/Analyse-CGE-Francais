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
import sys  # système

import fichier.gestionnaire_source  # traitement du fichier source
import affichage.gestionnaire_affichage  # gestion de l'affichage
from tracabilite.traces import info  # logs de niveau 1
from tracabilite.traces import erreur  # logs de niveau 2


def run():
    """
    Fonction principale du logiciel.
    Executée si main.py n'est pas appelée comme un module
    """

    # Traitement du fichier source :
    # Si un fichier a été passé en argument lors de l'execution du code,
    # alors on met à jour la base de donnée json
    # sinon, on créer un fichier json avec les données du fichier.

    # Si un argument est donné (fichier source)

    if len(sys.argv) > 1:
        chemin_fichier_source = str(sys.argv[1])  # On enregistre le chemin du fichier csv

        info("Recherche du fichier passé en argument : {0}".format(chemin_fichier_source))
        try:  # On essaye de charger le fichier de donnes
            fichier_source = open(chemin_fichier_source, "r")
            info("Fichier ouvert avec succès", "Création de la base de donnée à partir de la source ...")

            # On traite le fichier source donné


        except FileNotFoundError:  # Si le fichier n'est pas trouvé
            erreur("Le fichier {0} est introuvable".format(chemin_fichier_source))
            return 2  # Mauvaise utilisation du programme ou erreur d'entrée de l'utilisateur

        except IOError:
            erreur("Le fichier {0} n'est pas lisible".format(chemin_fichier_source))
            return 2  # Erreur générique (non spécifiée)

    # Si aucun chemin vers un fichier source n'a été donné

    else:
        try:  # On vérifie si la base de donnée existe déja (donnees.json)
            db = open("donnees.json", "r")  # On essaye d'ouvrir la base de données (qu'on nommera db)

        except FileNotFoundError:
            erreur("Aucune base de donnée n'existe",
                   "Veuillez executer le logiciel en précisant le chemin vers une source",
                   "Elle doit être au format csv, séparé par des virgules")
            return 2  # Erreur générique (non spécifiée)

    info("Fin du programme")
    return 0  # Fin du programme


if __name__ == '__main__':  # On vérifie si on execute bien le fichier directement et non comme un module
    info("Le programme démarre ...")
    sys.exit(run())  # Si on ne l'execute pas comme un module, alors on démarre notre programme

else:
    erreur("Impossible de démarrer le logiciel en tant que module", "Veuillez executer main.py directement.")
