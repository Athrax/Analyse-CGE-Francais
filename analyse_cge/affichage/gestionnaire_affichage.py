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

import matplotlib.pyplot as plt


def affichage_X_Y(X, Y):
    """
    Cette fonction affiche un graph linéaire.

    Args:
        X (list): Valeurs abscisse
        Y (list): Valeurs ordonnées
    """

    return


def affichage_bar(X, Y):
    """
    Cette fonction affiche un diagramme en barre à partir de listes X et Y

    Args:
        X (list): Valeurs abscisse
        Y (list): Valeurs ordonnées
    """

    return


def affichage_pie(X, Y, titre):
    """
    Cette fonction affiche un diagramme en camembert à partir d'une liste X

    Args:
        X (list): Liste des valeurs à représenter
        Y (list): Liste des labels
        titre (string): Titre du graphique
    """

    # On importe un modèle pour créer des graphiques camembert
    plt.pie(X, labels=Y, autopct='%1.1f%%')
    plt.title(titre)
    plt.show()
    plt.close()