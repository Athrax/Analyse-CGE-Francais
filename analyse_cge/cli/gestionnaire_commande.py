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
from affichage.gestionnaire_affichage import *
from source.gestionnaire_json import importer_json
from source.gestionnaire_arborescence import chemin, grand_parent
from journalisation.traces import avert, debug, info
from donnees.gestionnaire_donnees import trie_croissant_X_Y
from donnees.db import db


def graph_ministeres(ministere_inconnu, annee):
    labels = [*db]
    if ministere_inconnu:
        valeurs = [-int(db[ministere]["dépense_annuelle"][annee]) for ministere in [*db]]
    else:
        valeurs = [-int(db[ministere]["dépense_annuelle"][annee]) for ministere in [*db]
                   if ministere != "Non renseigné"]
        labels.pop(labels.index("Non renseigné"))
    titre = f"Dépenses des ministères en {annee}"

    try:
        affichage_pie(valeurs, labels, titre)
        debug("Valeurs du graphique :", valeurs, "labels :", labels)

    except Exception as exc:
        avert(f"Le graphique \"{titre}\" n'a pas pu être créer", exc)

    except RuntimeWarning as warn:
        avert("Indication :", warn)


def graph_postes(annee):
    # On affiche les choix des ministères
    liste_ministeres = [*db]  # On créer une liste avec tous les ministères
    for i in range(len(db)):  # On la parcours associer un nombre a chaque ministère
        info(f"{liste_ministeres[i]}: [{str(i)}]")

    # On demande le choix du ministere à l'utilisateur
    from cli.menu import effacer_console  # Pour eviter les boucles d'appel, on importe la fonction ici
    while True:
        try:
            entree = int(input("> "))  # On ne récupère l'entrée que si c'est un nombre
            break
        except:
            pass
    info("> " + str(entree))
    effacer_console()
    info(f"Ce graphique représente les dépenses du ministère \"{liste_ministeres[entree]}\" par poste en {annee}.")

    titre = (f"Dépense du ministère \"{liste_ministeres[entree]}\" par poste en {annee}")
    X = [clef
         for clef, poste in db[liste_ministeres[entree]]["postes"].items()
         if poste["dépense_annuelle"][annee]]  # On liste les postes
    Y = [-poste["dépense_annuelle"][annee]
         for clef, poste in db[liste_ministeres[entree]]["postes"].items()
         if poste["dépense_annuelle"][annee]]  # On récupère les dépenses

    Xtrie, Ytrie = trie_croissant_X_Y(X, Y)
    affichage_bar(Xtrie, Ytrie, titre)


def graphe_temp_ministere():
    pass


def afficher_db():
    # Chargement de la base de donnée
    print(db)


def commande(operation, parametre):
    if operation == "graph_ministere_avec_inconnu":
        graph_ministeres(True, parametre)

    if operation == "graph_ministere_sans_inconnu":
        graph_ministeres(False, parametre)

    if operation == "afficher_db":
        afficher_db()

    if operation == "graph_poste_par_ministere":
        graph_postes(parametre)
