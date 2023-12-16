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
from analyse_cge.journalisation.traces import *


def detection_en_tete(fichier_source):
    """
    Détecte les colonnes utiles du fichier source selon celles qui nous intéressent.
    Celles ci sont décrites dans le fichier de configuration/liste en_tete_utiles

    Args:
        fichier_source (file): Fichier source.
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


def regroupe_donnees_ministere(fichier_source, colonnes):
    """
    Regroupes les donnees du fichier source par ministère dans un dictionnaire

    Args:
        fichier_source (file): Fichier source à traiter
        colonnes (dict): Colonnes à traiter

    Returns:
         dictionnaire_ministere (dict): Dictionnaire des données regroupées par ministère
    """
    dictionnaire_ministere = dict

    info("Regroupement du contenu du fichier source par ministère...")
    for ligne in fichier_source:  # On lit ligne après ligne le fichier source
        cellules = ligne.strip().split(',')  # Supprime caractère de nouvelle ligne et recupère une liste des cellules
        cellule_ministere = cellules[colonnes["ministère"]] # Ministère concerné la ligne

        if cellule_ministere not in dictionnaire_ministere: # Si le ministère n'existe pas encore dans le dictionnaire
            dictionnaire_ministere

        # On somme la dépense de la ligne sur les années 2022 et 2012
        dictionnaire_ministere[cellule_ministere]["depense"][colonnes[-2]] += cellules[colonnes["2022"]]
        dictionnaire_ministere[cellule_ministere]["depense"][colonnes[-1]] += cellules[colonnes["2012"]]


