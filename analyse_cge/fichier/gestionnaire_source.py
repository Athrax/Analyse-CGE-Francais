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
from analyse_cge.tracabilite.traces import *


def detection_en_tete(fichier_source):
    """
    Détecte les colonnes utiles du fichier source selon celles qui nous intéressent.
    Celles ci sont décrites dans le fichier de configuration/liste en_tete_utiles

    Args:
        fichier_source (file): Chemin vers le fichier source.
    Returns:
        colonnes (dict): Dictionnaire de colonnes utiles
    """
    # Lecture de la première ligne du fichier source
    # Traduction en minuscule
    # Découpage
    en_tete_source = fichier_source.readline().lower().split(',')

    # On précise les colonne du fichier qui nous intéressent
    en_tete_utiles = ["postes", "sous-postes", "ministère", "2022", "2012"]
    colonnes = dict()  # Création d'un dictionnaire des colonnes utiles

    info("Détection des colonnes du fichier source ...")

    for en_tete_recherchee in en_tete_utiles:
        for i in range(len(en_tete_source)):
            if en_tete_recherchee in en_tete_source[i]:
                colonnes[en_tete_recherchee] = i
                break

    info(f"Colonnes: {colonnes}")  # On affiches les colonnes et leur indices

    return colonnes
