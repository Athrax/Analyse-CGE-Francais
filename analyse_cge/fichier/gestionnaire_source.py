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

from analyse_cge.donnees.nettoyage_valeur import savon
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


def detection_cellules(ligne):
    """
    Cette fonction répond à un problème d'interpétation du fichier csv
    Chaque cellule d'une ligne du fichier csv est séparée par une virgule.
    Or, il arrive qu'une virgule existe à l'intérieur d'une cellule.
    Ainsi, la-dite cellule est entourée de guillements.
    L'objectif de cette fonction est de traiter correctement le decoupage de cellule
    afin de ne pas séparer en deux l'une d'elles.
    Nous utilisons un module de traitement de fichier csv appelé StringIO,
    de la biliothèque io de python.

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
            info(f"Données détectées dans la ligne : {lecture_ligne}")
            return lecture_ligne # On renvoit la première ligne du fichier-ligne csv

    except IOError as err: # Si on n'arrive pas à lire la ligne
        erreur("Echec de la détection des données dans la ligne",
               "Impossible de lire la ligne fichier",
               "Veuillez verifier les caractères delimiteur et jalons de cellule",
               err)
        return 1


def regroupe_donnees_ministere(fichier_source, colonnes):
    """
    Regroupes les donnees du fichier source par ministère dans un dictionnaire

    Args:
        fichier_source (file): Fichier source à traiter
        colonnes (dict): Colonnes à traiter

    Returns:
         dictionnaire_ministere (dict): Dictionnaire des données regroupées par ministère
    """
    dictionnaire_ministere = dict()

    info("Regroupement du contenu du fichier source par ministère...")
    for ligne in fichier_source:  # On lit ligne après ligne le fichier source

        # On essaye de récupérer les cellules du ligne après ligne
        try: # Si tout se passe bien
            cellules = detection_cellules(ligne) # On extrait les cellules de la lignes sous forme de tableau

        except: # Si la ligne ne contient pas de données valides
            break # On ne traite pas la ligne

        cellule_ministere = cellules[colonnes["ministère"]]  # Ministère concerné par la ligne
        cellule_poste = cellules[colonnes["postes"]]  # Poste concerné par la ligne
        cellule_sous_poste = cellules[colonnes["sous-postes"]]  # Sous poste concerné par la ligne

        dep_2022, dep_2012 = savon(cellules[colonnes["2022"]], cellules[colonnes["2022"]]) # Nettoyage des données

        info(f"Ligne à traiter : Ministère {cellule_ministere}, "
        f"poste : {cellule_poste}, "
        f"sous-poste : {cellule_sous_poste}, ")

        if cellule_ministere == "":  # Si le ministère n'est pas renseigné sur la ligne (inconnu)
            cellule_ministere = "inconnu"  # On créera un ministère inconnu

        if cellule_poste == "":  # Si le poste n'est pas renseigné sur la ligne (inconnu)
            cellule_poste = "inconnu"  # On créera un poste inconnu

        if cellule_sous_poste == "":  # Si le sous-poste n'est pas renseigné sur la ligne (inconnu)
            cellule_sous_poste = "inconnu"  # On créera un sous-poste inconnu

        if cellule_ministere not in dictionnaire_ministere:  # Si le ministère n'a pas déja été enregistré
            info(f"Traitement d'un nouveau ministère {cellule_ministere}")
            # On créer le dictionnaire des dépenses totales du ministère pour les deux années
            dictionnaire_ministere[cellule_ministere] = dict()  # On créer le dictionnaire du ministère
            dictionnaire_ministere[cellule_ministere]["dépense_annuelle"] = {
                2022: 0,
                2012: 0
            }
            # On créer le dictionnaire parent des dépenses par postes du ministères
            dictionnaire_ministere[cellule_ministere]["postes"] = dict()

        # Si le poste n'est pas déja enregistré dans le ministère, on créer un enfant poste
        if cellule_poste not in dictionnaire_ministere[cellule_ministere]:
            info(f"Traitement du nouveau poste {cellule_poste} pour le ministère {cellule_ministere}")
            # On créer le dictionnaire des dépenses par poste du ministère pour les deux années
            dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste] = dict()
            dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste]["dépense_annuelle"] = {
                2022: 0,
                2012: 0
            }
            # On créer le dictionnaire des sous-postes de ce poste
            dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste]["sous-postes"] = dict()

        # Si le sous-poste n'est pas déja enregistré dans le ministère, on créer le sous-poste dans le poste
        if cellule_sous_poste not in dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste]["sous-postes"]:
            info(f"Traitement du nouveau sous-poste {cellule_sous_poste} pour le ministère {cellule_ministere}")
            # On créer le dictionnaire des dépenses par sous-poste du poste du ministère pour les deux années
            dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste]["sous-postes"][cellule_sous_poste] = dict()
            dictionnaire_ministere[cellule_ministere]\
                ["postes"][cellule_poste]\
                ["sous-postes"][cellule_sous_poste]\
                ["dépense_annuelle"] = {
                2022: 0,
                2012: 0
            }

        # Ajout des données au ministère créé
        info(f"Nouvelle entrée : Dépense du ministère {cellule_ministere}, "
             f"poste : {cellule_poste}, "
             f"sous-poste : {cellule_sous_poste}, "
             f"dépense 2022 : {dictionnaire_ministere[cellule_ministere]['dépense_annuelle'][2022]}, "
             f"dépense 2012 : {dictionnaire_ministere[cellule_ministere]['dépense_annuelle'][2012]}")

        # Ajout de la dépense à la somme annuelle du ministère
        dictionnaire_ministere[cellule_ministere]["dépense_annuelle"][2022] += dep_2022
        dictionnaire_ministere[cellule_ministere]["dépense_annuelle"][2012] += dep_2012

        # Ajout de la dépense à la somme annuelle du poste
        dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste]["dépense_annuelle"][2022] += dep_2022
        dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste]["dépense_annuelle"][2022] += dep_2012

        # Ajout de la dépense à la somme annuelle du sous-poste
        dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste]["sous-postes"][cellule_sous_poste]["dépense_annuelle"][2022] += dep_2022
        dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste]["sous-postes"][cellule_sous_poste]["dépense_annuelle"][2022] += dep_2012




