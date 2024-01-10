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
import csv
from sys import exit
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
    try:
        en_tete_source = fichier_source.readline().lower().split(',')
    except UnicodeDecodeError:
        erreur("Impossible de lire le fichier source", "Seul le codec UTF-8 est autorisé")
        exit(2)

    # On précise les colonne du fichier qui nous intéressent
    en_tete_utiles = ["postes", "sous-postes", "ministère", "2022", "2021", "2020", "2019", "2018", "2017", "2016",
                      "2015", "2014", "2013", "2012"]
    colonnes = dict()  # Création d'un dictionnaire des colonnes utiles

    # On recherche les index colonnes qui nous intéressent
    # On lit chaque valeur de l'entete et si une en-tête utile précisée ci dessous est comprise dedans,
    # alors on enregistre son index dans un dictionnaire avec pour correspondance: nom de l'en-tête = index
    # On ne reprend pas l'analyse du début a chaque fois,
    # on repart de la dernière occurence trouvée (index_debut_analyse)
    debug("Détection des colonnes du fichier source ...")
    index_debut_analyse = 0
    for en_tete_recherchee in en_tete_utiles:   # Pour chaque en-tête que nous cherchons
        for i in range(index_debut_analyse, len(en_tete_source)):     # On vérifie si l'entete du fichier
            if en_tete_recherchee in en_tete_source[i]:  # est recherchée
                colonnes[en_tete_recherchee] = int(i)  # Si oui, on enregistre son indice
                index_debut_analyse = i+1  # Permet de continuer l'analyser à partir de là où on s'est arreté
                break

    avert(f"Colonnes: {colonnes}")  # On affiches les colonnes et leur indices
    return colonnes


def detection_cellules(ligne):
    """
    Cette fonction répond à un problème d'interpétation du fichier csv
    Chaque cellule d'une ligne du fichier csv est séparée par une virgule.
    Or, il arrive qu'une virgule existe à l'intérieur d'une cellule.
    Ainsi, la-dite cellule est entourée de guillements.
    L'objectif de cette fonction est de traiter correctement le decoupage de cellule
    afin de ne pas séparer en deux l'une d'elles.
    Nous utilisons un module de traitement de fichier csv appelé StringIO,
    importé depuis la biliothèque io de python.

    Args:
        ligne (str): La ligne du fichier à découper en cellules
    Returns:
        cellules (list): Les cellules sous forme de liste
    """
    from io import StringIO

    # On considère notre ligne comme un fichier csv d'une seule ligne
    try:
        with StringIO(ligne) as ligne_fichier:
            # On lit le fichier csv d'une ligne et on découpe les cellules
            # en précisant le délimiteur et les caractère de jalons de cellule
            # Rappel : next() est une fonction qui permet d'obtenir le prochain élément d'un itérable

            lecture_ligne = next(csv.reader(ligne_fichier, delimiter=",", quotechar='"'))
            debug(f"Données détectées dans la ligne : {lecture_ligne}")
            return lecture_ligne  # On renvoit la première ligne du fichier-ligne csv

    except IOError as err:  # Si on n'arrive pas à lire la ligne
        erreur("Echec de la détection des données dans la ligne",
               "Impossible de lire la ligne fichier",
               "Veuillez verifier les caractères delimiteur et jalons de cellule",
               err)
        return 1
