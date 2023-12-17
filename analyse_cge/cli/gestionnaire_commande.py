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
from analyse_cge.affichage.gestionnaire_affichage import *
from analyse_cge.fichier.gestionnaire_json import importer_json
from analyse_cge.fichier.gestionnaire_arborescence import chemin, grand_parent


def graph_ministere():
    # Chargment de la base de donnée
    db = importer_json(chemin(grand_parent(__file__), "..", "docs", "db_ministere.json"))

    valeurs = [int(db[ministere]["recette_annuelle"]["2022"]) for ministere in [*db]]
    labels = [*db]
    titre = "Dépenses des ministères en 2022"

    affichage_pie(valeurs, labels, titre)


def afficher_db():
    # Chargement de la base de donnée
    db = importer_json(chemin(grand_parent(__file__), "..", "docs", "db_ministere.json"))
    print(db)


def commande(operation):
    if operation == "graph_ministere":
        graph_ministere()

    if operation == "afficher_db":
        afficher_db()

