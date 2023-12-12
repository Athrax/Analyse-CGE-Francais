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

# python_version >= "3.11"

# matplotlib : graphiques
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# numpy : outils mathématiques
import numpy as np

# sys : système
import sys

# Importation des modules principaux
from gestionnaire_affichage import affichage

def run():
    """
    Fonction principale du logiciel.
    Executée si main.py n'est pas appelée comme un module

    Args:
        data_file_path (string): Chemin vers le fichier de données.
    """
    affichage()

if __name__ == '__main__': # On vérifie si on execute bien le fichier directement et non comme un module
    sys.exit(run()) # Si on ne l'execute pas comme un module, alors on démarre notre programme