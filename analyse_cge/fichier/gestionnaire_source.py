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

from analyse_cge.donnees.nettoyage_valeur import savon_a_chiffres, savon_a_lettres
from analyse_cge.journalisation.traces import *
from analyse_cge.fichier.detection_donnees import detection_cellules


def regroupe_donnees_ministere(fichier_source, colonnes, ligne_traiter=-1):
    """
    Créatio du ctionnaire en regroupant les donnees du fichier source par ministère dans un dictionnaire
    Afin de tester le programme plus facilement
    On introduit un compteur de ligne pour n'en traiter qu'un petit nombre
    par défaut = -1 pour ne pas tomber à 0 et arreter la lecture s'il n'est pas précisé

    Args:
        fichier_source (file): Fichier source à traiter
        colonnes (dict): Colonnes à traiter
        ligne_traiter (int): Nombre de lignes à traiter

    Returns:
         dictionnaire_ministere (dict): Dictionnaire des données regroupées par ministère
    """

    dictionnaire_ministere = dict()

    info("Regroupement du contenu du fichier source par ministère...")
    for ligne in fichier_source:  # On lit ligne après ligne le fichier source

        # On essaye de récupérer les cellules, ligne après ligne
        try:  # Si tout se passe bien
            cellules = detection_cellules(ligne)  # On extrait les cellules de la lignes sous forme de tableau

        except:  # Si la ligne ne contient pas de données valides
            break  # On ne traite pas la ligne

        # On récupère les valeurs qui nous intéressent dans la ligne étudiée du fichier source.
        # On les récupère a partir du numéro d'indice des en-têtes.
        cellule_ministere = savon_a_lettres(cellules[colonnes["ministère"]])  # Ministère concerné par la ligne
        cellule_poste = savon_a_lettres(cellules[colonnes["postes"]])  # Poste concerné par la ligne
        cellule_sous_poste = savon_a_lettres(cellules[colonnes["sous-postes"]])  # Sous poste concerné par la ligne
        balance_2022, balance_2012 = savon_a_chiffres(cellules[colonnes["2022"]], cellules[colonnes["2012"]])  # Nettoyage des données

        debug(f"[l{ligne_traiter}] Traitement de la ligne : Ministère \"{cellule_ministere}\”, ",
              f"poste : \"{cellule_poste}\", ",
              f"sous-poste : \"{cellule_sous_poste}\", ",
              f"dep_2022 : \"{balance_2022}\", ",
              f"dep_2012 : \"{balance_2012}\"")

        # On prépare les données récupérée pour la création du dictionnaire
        # On gère les cases vides
        if cellule_ministere == "":  # Si le ministère n'est pas renseigné sur la ligne (Non renseigné)
            cellule_ministere = "Non renseigné"  # On créera un ministère Non renseigné

        if cellule_poste == "":  # Si le poste n'est pas renseigné sur la ligne (Non renseigné)
            cellule_poste = "Non renseigné"  # On créera un poste Non renseigné

        if cellule_sous_poste == "":  # Si le sous-poste n'est pas renseigné sur la ligne (Non renseigné)
            cellule_sous_poste = "Non renseigné"  # On créera un sous-poste Non renseigné

        # On commence à remplir le dictionnaire
        # On créer les ministères qui n'exsitent pas encore
        if cellule_ministere not in dictionnaire_ministere:  # Si le ministère n'a pas déja été enregistré :
            # On créer le dictionnaire des dépenses et recettes totales du ministère pour les deux années
            info(f"Création d'un nouveau ministère {cellule_ministere}")

            # On créer le dictionnaire du ministère
            dictionnaire_ministere[cellule_ministere] = dict()

            # On créer les dictionnaires des dépenses et recettes pour les deux années
            dictionnaire_ministere[cellule_ministere]["dépense_annuelle"] = {
                "2022": 0.0,
                "2012": 0.0
            }
            dictionnaire_ministere[cellule_ministere]["recette_annuelle"] = {
                "2022": 0.0,
                "2012": 0.0
            }

            # On créer un dictionnaire vide qui accueillera les postes du ministère
            dictionnaire_ministere[cellule_ministere]["postes"] = dict()

        # On traite les postes de la ligne
        # Si le poste n'est pas déja enregistré dans le ministère, alors on créer un enfant poste dans le ministère
        if cellule_poste not in dictionnaire_ministere[cellule_ministere]:
            debug(f"Création du nouveau poste {cellule_poste} pour le ministère {cellule_ministere}")

            # On créer le dctionnaire du poste
            dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste] = dict()

            # On créer le dictionnaire des dépenses et recettes par poste du ministère pour les deux années
            dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste]["dépense_annuelle"] = {
                "2022": 0.0,
                "2012": 0.0
            }
            dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste]["recette_annuelle"] = {
                "2022": 0.0,
                "2012": 0.0
            }

            # On créer le dictionnaire des sous-postes de ce poste
            dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste]["sous-postes"] = dict()

        # On traite le sous-poste de la ligne
        # Si le sous-poste n'est pas déja enregistré dans le ministère, on créer le sous-poste dans le poste
        if cellule_sous_poste not in dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste]["sous-postes"]:
            debug(f"Création du nouveau sous-poste {cellule_sous_poste} pour le ministère {cellule_ministere}")

            # On créer le dictionnaire du sous poste traité
            dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste]["sous-postes"][
                cellule_sous_poste] = dict()

            # On créer le dictionnaire des dépenses par sous-poste du poste du ministère pour les deux années
            dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste]["sous-postes"][cellule_sous_poste]["dépense_annuelle"] = {
                "2022": 0.0,
                "2012": 0.0
            }
            dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste]["sous-postes"][cellule_sous_poste]["recette_annuelle"] = {
                "2022": 0.0,
                "2012": 0.0
            }

        # Ajout des données aux ministères
        # Ajout de la dépense et/ou de la recette de la ligne
        # On les ajoutes à la somme du minitère, du poste, et du sous poste

        # 2022
        if balance_2022 >= 0:  # S'il s'agit d'une recette
            dictionnaire_ministere[cellule_ministere]["recette_annuelle"]["2022"] += balance_2022
            dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste]["recette_annuelle"]["2022"] += balance_2022
            dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste]["sous-postes"][cellule_sous_poste]["recette_annuelle"]["2022"] += balance_2022
        if balance_2022 < 0:  # S'il s'agit d'une dépense
            dictionnaire_ministere[cellule_ministere]["dépense_annuelle"]["2022"] += balance_2022
            dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste]["dépense_annuelle"]["2022"] += balance_2022
            dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste]["sous-postes"][cellule_sous_poste]["dépense_annuelle"]["2022"] += balance_2022

        # 2012
        if balance_2022 >= 0:  # S'il s'agit d'une recette
            dictionnaire_ministere[cellule_ministere]["recette_annuelle"]["2012"] += balance_2012
            dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste]["recette_annuelle"]["2022"] += balance_2012
            dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste]["sous-postes"][cellule_sous_poste]["recette_annuelle"]["2012"] += balance_2012
        if balance_2012 < 0:  # S'il s'agit d'une recette
            dictionnaire_ministere[cellule_ministere]["dépense_annuelle"]["2012"] += balance_2012
            dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste]["dépense_annuelle"]["2012"] += balance_2012
            dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste]["sous-postes"][cellule_sous_poste]["dépense_annuelle"]["2012"] += balance_2012

        debug(f"Nouvel état pour le ministère \"{cellule_ministere}\", ",
            f"dépense 2022 : {dictionnaire_ministere[cellule_ministere]['dépense_annuelle']['2022']}, ",
            f"dépense 2012 : {dictionnaire_ministere[cellule_ministere]['dépense_annuelle']['2012']}, ",
            f"recette 2022 : {dictionnaire_ministere[cellule_ministere]['recette_annuelle']['2022']}, ",
            f"recette 2012 : {dictionnaire_ministere[cellule_ministere]['recette_annuelle']['2012']}, ",
            f"poste : \"{cellule_poste}\", ",
            f"dépense 2022 : {dictionnaire_ministere[cellule_ministere]['postes'][cellule_poste]['dépense_annuelle']['2022']}, ",
            f"dépense 2012 : {dictionnaire_ministere[cellule_ministere]['postes'][cellule_poste]['dépense_annuelle']['2012']}, ",
            f"recette 2022 : {dictionnaire_ministere[cellule_ministere]['postes'][cellule_poste]['recette_annuelle']['2022']}, ",
            f"recette 2012 : {dictionnaire_ministere[cellule_ministere]['postes'][cellule_poste]['recette_annuelle']['2012']}, ",
            f"sous-poste : \"{cellule_sous_poste}\", ",
            f"dépense 2022 : {dictionnaire_ministere[cellule_ministere]['postes'][cellule_poste]['sous-postes'][cellule_sous_poste]['dépense_annuelle']['2022']}, ",
            f"dépense 2012 : {dictionnaire_ministere[cellule_ministere]['postes'][cellule_poste]['sous-postes'][cellule_sous_poste]['dépense_annuelle']['2012']}, ",
            f"dépense 2022 : {dictionnaire_ministere[cellule_ministere]['postes'][cellule_poste]['sous-postes'][cellule_sous_poste]['recette_annuelle']['2022']}, ",
            f"dépense 2012 : {dictionnaire_ministere[cellule_ministere]['postes'][cellule_poste]['sous-postes'][cellule_sous_poste]['recette_annuelle']['2012']}")

        ligne_traiter -= 1
        if ligne_traiter == 0 :
            debug("Seul certaines lignes ont été traitées")
            break

    return dictionnaire_ministere
