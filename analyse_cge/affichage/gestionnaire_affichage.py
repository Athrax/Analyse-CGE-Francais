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
from analyse_cge.journalisation.traces import avert


def affichage_X_Y(X, Y):
    """
    Cette fonction affiche un graph linéaire.

    Args:
        X (list): Valeurs abscisse
        Y (list): Valeurs ordonnées
    """

    return


def affichage_bar(X, Y, titre):
    """
    Cette fonction affiche un diagramme en barre à partir de listes X et Y

    Args:
        X (list): Valeurs abscisse
        Y (list): Valeurs ordonnées
    """

    # On génère le graphique en barres
    plt.bar(X, Y)

    try:
        # Ajout de titres et d'étiquettes
        plt.title(titre)
        plt.ylabel('Dépenses en €')

        plt.xticks(rotation=25, ha="right")  # On tourne légerement les labels de l'axe x
        plt.yscale('log')  # On définit l'échelle logarithmique sur l'axe y
        plt.tight_layout()  # Ajuste automatiquement la disposition du graphique pour voir les labels en entier

        palette = plt.get_cmap("Set2")  # On utilise une palette de couleur matplotlib

        for i in range(len(X)): # Affichage des barres avec des couleurs différentes
            plt.bar(X[i], Y[i], color=palette(i))

    except Exception as exc:
        avert("Echec de la génération du titre/étiquettes du graphique", exc)

    try:
        plt.show()
    except Exception as exc:
        avert("Echec de l'affichage du graphique", exc)


def affichage_pie(X, Y, titre):
    """
    Cette fonction affiche un diagramme en camembert à partir d'une liste X

    Args:
        X (list): Liste des valeurs à représenter
        Y (list): Liste des labels
        titre (string): Titre du graphique
    """

    # On génère le graphique en camembert
    plt.pie(X, labels=Y, autopct='%1.1f%%')

    try:
        plt.title(titre)
    except Exception as exc:
        avert("Echec de la génération du titre du graphique", exc)

    try:
        plt.show()
    except Exception as exc:
        avert("Echec de l'affichage du graphique", exc)