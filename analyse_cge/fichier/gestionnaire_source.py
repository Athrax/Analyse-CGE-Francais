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

from analyse_cge.donnees.nettoyage_valeur import savon
from analyse_cge.journalisation.traces import *
from analyse_cge.fichier.detection_donnees import detection_cellules


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

        # On essaye de récupérer les cellules, ligne après ligne
        try:  # Si tout se passe bien
            cellules = detection_cellules(ligne)  # On extrait les cellules de la lignes sous forme de tableau

        except:  # Si la ligne ne contient pas de données valides
            break  # On ne traite pas la ligne

        cellule_ministere = cellules[colonnes["ministère"]]  # Ministère concerné par la ligne
        cellule_poste = cellules[colonnes["postes"]]  # Poste concerné par la ligne
        cellule_sous_poste = cellules[colonnes["sous-postes"]]  # Sous poste concerné par la ligne

        dep_2022, dep_2012 = savon(cellules[colonnes["2022"]], cellules[colonnes["2012"]])  # Nettoyage des données

        debug(f"Ligne à traiter : Ministère {cellule_ministere}, "
              f"poste : {cellule_poste}, "
              f"sous-poste : {cellule_sous_poste}, "
              f"dep_2022 : {dep_2022}, "
              f"dep_2012 : {dep_2012}")

        if cellule_ministere == "":  # Si le ministère n'est pas renseigné sur la ligne (Inconnu)
            cellule_ministere = "Inconnu"  # On créera un ministère Inconnu

        if cellule_poste == "":  # Si le poste n'est pas renseigné sur la ligne (Inconnu)
            cellule_poste = "Inconnu"  # On créera un poste Inconnu

        if cellule_sous_poste == "":  # Si le sous-poste n'est pas renseigné sur la ligne (Inconnu)
            cellule_sous_poste = "Inconnu"  # On créera un sous-poste Inconnu

        if cellule_ministere not in dictionnaire_ministere:  # Si le ministère n'a pas déja été enregistré
            info(f"Création d'un nouveau ministère {cellule_ministere}")
            # On créer le dictionnaire des dépenses totales du ministère pour les deux années
            dictionnaire_ministere[cellule_ministere] = dict()  # On créer le dictionnaire du ministère
            dictionnaire_ministere[cellule_ministere]["dépense_annuelle"] = {
                "2022": 0.0,
                "2012": 0.0
            }
            # On créer le dictionnaire parent des postes
            dictionnaire_ministere[cellule_ministere]["postes"] = dict()

        # Si le poste n'est pas déja enregistré dans le ministère, on créer un enfant poste
        if cellule_poste not in dictionnaire_ministere[cellule_ministere]:
            debug(f"Création du nouveau poste {cellule_poste} pour le ministère {cellule_ministere}")
            # On créer le dictionnaire des dépenses par poste du ministère pour les deux années
            dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste] = dict()
            dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste]["dépense_annuelle"] = {
                "2022": 0.0,
                "2012": 0.0
            }
            # On créer le dictionnaire des sous-postes de ce poste
            dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste]["sous-postes"] = dict()

        # Si le sous-poste n'est pas déja enregistré dans le ministère, on créer le sous-poste dans le poste
        if cellule_sous_poste not in dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste]["sous-postes"]:
            debug(f"Création du nouveau sous-poste {cellule_sous_poste} pour le ministère {cellule_ministere}")
            # On créer le dictionnaire des dépenses par sous-poste du poste du ministère pour les deux années
            dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste]["sous-postes"][
                cellule_sous_poste] = dict()
            dictionnaire_ministere[cellule_ministere] \
                ["postes"][cellule_poste] \
                ["sous-postes"][cellule_sous_poste] \
                ["dépense_annuelle"] = {
                "2022": 0.0,
                "2012": 0.0
            }

        # Ajout des données au ministère créé
        debug(f"Nouvelle entrée pour le ministère {cellule_ministere}, "
              f"poste : {cellule_poste}, "
              f"sous-poste : {cellule_sous_poste}, "
              f"dépense 2022 : {dictionnaire_ministere[cellule_ministere]['dépense_annuelle']['2022']} + {dep_2022}, "
              f"dépense 2012 : {dictionnaire_ministere[cellule_ministere]['dépense_annuelle']['2012']} + {dep_2012}")

        # Ajout de la dépense à la somme annuelle du ministère
        dictionnaire_ministere[cellule_ministere]["dépense_annuelle"]["2022"] += dep_2022
        dictionnaire_ministere[cellule_ministere]["dépense_annuelle"]["2012"] += dep_2012

        # Ajout de la dépense à la somme annuelle du poste
        dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste]["dépense_annuelle"]["2022"] += dep_2022
        dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste]["dépense_annuelle"]["2012"] += dep_2012

        # Ajout de la dépense à la somme annuelle du sous-poste
        dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste]["sous-postes"][cellule_sous_poste][
            "dépense_annuelle"]["2022"] += dep_2022
        dictionnaire_ministere[cellule_ministere]["postes"][cellule_poste]["sous-postes"][cellule_sous_poste][
            "dépense_annuelle"]["2012"] += dep_2012

        debug(f"Mise à jour terminée pour le minisètre {cellule_ministere}, "
              f"dépense 2022 : {dictionnaire_ministere[cellule_ministere]['dépense_annuelle']['2022']}, "
              f"dépense 2012 : {dictionnaire_ministere[cellule_ministere]['dépense_annuelle']['2012']}, "
              f"poste : {cellule_poste}, "
              f"2022 : {dictionnaire_ministere[cellule_ministere]['postes'][cellule_poste]['dépense_annuelle']['2022']}, "
              f"2012 : {dictionnaire_ministere[cellule_ministere]['postes'][cellule_poste]['dépense_annuelle']['2012']}, "
              f"sous-poste : {cellule_sous_poste}, "
              f"2022 : {dictionnaire_ministere[cellule_ministere]['postes'][cellule_poste]['sous-postes'][cellule_sous_poste]['dépense_annuelle']['2022']}, "
              f"2012 : {dictionnaire_ministere[cellule_ministere]['postes'][cellule_poste]['sous-postes'][cellule_sous_poste]['dépense_annuelle']['2012']}")

    return dictionnaire_ministere
