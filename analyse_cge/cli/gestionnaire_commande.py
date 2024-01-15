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
from journalisation.traces import avert, debug, info
from donnees.gestionnaire_donnees import trie_croissant_X_Y
from source.detection_donnees import en_tete_utiles
from donnees.db import db, db_etat


def graph_ministeres(ministere_inconnu, annee, dep_ou_rec="Dépenses"):
    labels = [*db]
    if ministere_inconnu == ("Ministère connues et inconnus" or True):
        if dep_ou_rec == "Dépenses":
            valeurs = [-int(db[ministere]["dépense_annuelle"][annee]) for ministere in [*db]]
            titre = f"Dépenses des ministères en {annee}"
        else:
            valeurs = [int(db[ministere]["recette_annuelle"][annee]) for ministere in [*db]]
            titre = f"Recettes des ministères en {annee}"

    else:
        if dep_ou_rec == "Dépenses":
            valeurs = [-int(db[ministere]["dépense_annuelle"][annee]) for ministere in [*db]
                       if ministere != "Non renseigné"]
            titre = f"Dépenses des ministères en {annee}"
        else:
            valeurs = [int(db[ministere]["recette_annuelle"][annee]) for ministere in [*db]
                       if ministere != "Non renseigné"]
            titre = f"Recettes des ministères en {annee}"

        labels.pop(labels.index("Non renseigné"))

    try:
        debug("Valeurs du graphique :", valeurs, "labels :", labels)
        return affichage_pie(valeurs, labels, titre)

    except Exception as exc:
        avert(f"Le graphique \"{titre}\" n'a pas pu être créer", exc)

    except RuntimeWarning as warn:
        avert("Indication :", warn)


def graph_postes(annee, ministere=None, echelle="semilog"):
    if not ministere:
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
        ministere = liste_ministeres[entree]
        effacer_console()
        info(f"Ce graphique représente les dépenses du ministère \"{ministere}\" par poste en {annee}.")

    titre = f"Dépense du ministère \n\"{ministere}\" par poste en {annee}"
    X = [clef
         for clef, poste in db[ministere]["postes"].items()
         if poste["dépense_annuelle"][annee]]  # On liste les postes
    Y = [-poste["dépense_annuelle"][annee]
         for clef, poste in db[ministere]["postes"].items()
         if poste["dépense_annuelle"][annee]]  # On récupère les dépenses

    Xtrie, Ytrie = trie_croissant_X_Y(X, Y)
    return affichage_bar(Xtrie, echelle, Ytrie, titre)


def afficher_db():
    # Chargement de la base de donnée
    print(db)


def graph_etat_evolution(echelle="semilog"):
    labels = [int(annee) for annee in en_tete_utiles[3:]]  # Contient toutes les années
    sorted(labels, reverse=True)
    titre = f"Évolution des dépenses et recettes de l'État"

    depenses = [-dep_annee / 10e9 for dep_annee in db_etat["dépenses"].values()]
    recettes = [rec_annee / 10e9 for rec_annee in db_etat["recettes"].values()]
    return affichage_X_Y1_Y2(labels, echelle, depenses, recettes, titre, "Dépenses", "Recettes")


def graph_ministere_evolution(ministere=None, echelle="semilog"):
    # Si aucun ministère n'a été passé en argument (cas de l'interface graphique), le demander en cli
    if not ministere:
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
        ministere = liste_ministeres[entree]
        effacer_console()
        info(f"Ce graphique représente les dépense et les recettes du ministère \"{ministere}\" au fil des ans")

    titre = f"Évolution des dépenses et recettes du ministère \n\"{ministere}\""
    labels = [int(annee) for annee in en_tete_utiles[3:]]  # Contient toutes les années
    sorted(labels, reverse=True)
    depenses = [-db[ministere]["dépense_annuelle"][str(annee)] / 10e9 for annee in labels]
    recettes = [db[ministere]["recette_annuelle"][str(annee)] / 10e9 for annee in labels]
    return affichage_X_Y1_Y2(labels, echelle, depenses, recettes, titre, "Dépenses", "Recettes")


def graph_pie_autre(ministere_inconnu, annee, dep_ou_rec="Dépenses"):
    labels = [*db]
    if ministere_inconnu == ("Ministère connues et inconnus" or True):
        if dep_ou_rec == "Dépenses":
            valeurs = [-int(db[ministere]["dépense_annuelle"][annee]) for ministere in [*db]]
            titre = f"Dépenses des ministères en {annee}"
        else:
            valeurs = [int(db[ministere]["recette_annuelle"][annee]) for ministere in [*db]]
            titre = f"Recettes des ministères en {annee}"

    else:
        if dep_ou_rec == "Dépenses":
            valeurs = [-int(db[ministere]["dépense_annuelle"][annee]) for ministere in [*db]
                       if ministere != "Non renseigné"]
            titre = f"Dépenses des ministères en {annee}"
        else:
            valeurs = [int(db[ministere]["recette_annuelle"][annee]) for ministere in [*db]
                       if ministere != "Non renseigné"]
            titre = f"Recettes des ministères en {annee}"

        labels.pop(labels.index("Non renseigné"))

    liste_autre = []
    labels_autre = []

    valeurs_pas_autre = []
    labels_pas_autre = []
    total_autre = 0

    total = sum(valeurs)

    for i in range(len(valeurs)):
        if valeurs[i] <= total * 0.05:
            total_autre += valeurs[i]
            liste_autre.append(valeurs[i])
            labels_autre.append(labels[i])
        else:
            valeurs_pas_autre.append(valeurs[i])
            labels_pas_autre.append(labels[i])

    valeurs_pas_autre.append(total_autre)
    labels_pas_autre.append("Autre")

    return affichage_pie_autre(liste_autre, labels_autre, valeurs_pas_autre, labels_pas_autre, titre, total_autre)


def commande(operation, parametre):
    if operation == "graph_ministere_avec_inconnu":
        graph = affichage_pie_autre(True, parametre)
        plt.show()

    elif operation == "graph_ministere_sans_inconnu":
        graph = affichage_pie_autre(False, parametre)
        plt.show()

    elif operation == "graph_poste_par_ministere":
        graph = graph_postes(parametre)
        plt.show()

    elif operation == "graph_etat_evolution_sans_inconnu":
        graph = graph_etat_evolution()
        plt.show()

    elif operation == "graph_ministere_evolution_sans_inconnu":
        graph = graph_ministere_evolution()
        plt.show()

    elif operation == "afficher_db":
        afficher_db()

    else:
        pass
