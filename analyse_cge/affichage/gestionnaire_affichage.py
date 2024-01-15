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
from journalisation.traces import avert


def affichage_X_Y(X, Y, titre):
    """
    Cette fonction affiche un graph linéaire.

    Args:
        X (list): Valeurs abscisse
        Y (list): Valeurs ordonnées
    """

    return


def affichage_X_Y1_Y2(X, echelle, Y1, Y2, titre, label_Y1, label_Y2):
    """
    Cette fonction affiche un graph linéaire, avec légende, titre, et lignes horizontales
    Les données sont affichées en millions

    Args:
        X (list): Valeurs abscisse
        Y1 (list): Valeurs ordonnées
        Y2 (list): Valeurs ordonnées
    """
    fig, ax = plt.subplots()

    try:
        # Tracer les deux courbes
        ax.plot(X, Y1, label=label_Y1)
        ax.plot(X, Y2, label=label_Y2)

        # Ajout des légendes, grille, étiquettes, etc.
        ax.legend()
        ax.grid(axis='y')
        ax.set_xticks(X)
        ax.set_ylabel('en Milliards €')

        if echelle == "semilog":
            # Ajuster les paramètres de l'axe y en échelle logarithmique
            ax.set_yscale('log')
            ax.locator_params(axis='y', numticks=10)  # Ajustez numticks selon vos besoins

        fig.tight_layout() # Ajuste automatiquement la disposition du graphique
        fig.subplots_adjust(top=0.9)

        try:
            ax.set_title(titre)
        except Exception as exc:
            print("Echec de la génération du titre du graphique", exc)

    except Exception as exc:
        print("Erreur lors de la création du graphique", exc)

    return fig, ax


def affichage_bar(X, echelle, Y, titre):
    """
    Cette fonction affiche un diagramme en barre à partir de listes X et Y

    Args:
        X (list): Valeurs abscisse
        Y (list): Valeurs ordonnées
    """

    # Création d'une figure et d'axes
    fig, ax = plt.subplots()

    try:
        # Ajout de titres et d'étiquettes
        ax.set_title(titre)
        ax.set_ylabel('Dépenses en €')
        ax.grid(axis='y', color='lightgrey')


        ax.xaxis.set_ticks([i for i in range(len(X))])
        ax.set_xticklabels(X, rotation=25, ha="right")  # On tourne légèrement les labels de l'axe x
        if echelle == "semilog":
            ax.set_yscale('log')  # On définit l'échelle logarithmique sur l'axe y
        fig.tight_layout()  # Ajuste automatiquement la disposition du graphique pour voir les labels en entier
        fig.subplots_adjust(left=0.2)

        palette = plt.get_cmap("Set2")  # On utilise une palette de couleur matplotlib

        for i in range(len(X)):  # Affichage des barres avec des couleurs différentes
            ax.bar(X[i], Y[i], color=palette(i))

        return fig, ax
    except UserWarning:
        pass


def affichage_pie(X, Y, titre):
    """
    Cette fonction affiche un diagramme en camembert à partir d'une liste X

    Args:
        X (list): Liste des valeurs à représenter
        Y (list): Liste des labels
        titre (string): Titre du graphique
    """

    # On génère le graphique en camembert
    fig, ax = plt.subplots()
    ax.pie(X, labels=Y, autopct='%1.1f%%')

    try:
        ax.set_title(titre)
    except Exception as exc:
        avert("Echec de la génération du titre du graphique", exc)

    return fig, plt
