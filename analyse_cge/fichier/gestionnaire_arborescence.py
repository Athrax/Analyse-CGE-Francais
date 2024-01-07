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
import os.path


def parent(fichier):
    chemin_fichier = os.path.abspath(fichier)  # On récupère le chemin absolu
    chemin_parent = os.path.join(chemin_fichier, os.path.pardir)  # On remonte une fois
    return os.path.abspath(chemin_parent)  # On renvoit le chemin absolue du parent


def grand_parent(fichier):
    chemin_fichier = os.path.abspath(fichier)  # On récupère le chemin absolu
    chemin_grand_parent = os.path.join(chemin_fichier, os.path.pardir, os.path.pardir)
    return os.path.abspath(chemin_grand_parent)


def chemin(*entrees):
    return os.path.join(*entrees)