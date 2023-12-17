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
from sys import argv as args


def arguments():
    """
    Cette fonction a pour objectif de traiter les valeurs données arguments lors de l'appel du logiciel

    Examples:
        if "-source" in argument():
            chemin = argument["-source"]
    Returns:
        arguments (dict): dictionnaire contenant les arguments
    """
    # Les arguments ont la structure suivantes :
    # main.py -v -nogui -source ../docs/source.csv
    # La structure est -[argument] [valeur (optionnel)]

    # On créer le dictionnaire contenant les arguments
    arguments = {}

    for i in range(1, len(args[0:])):  # On observe chaque valeur donnée en argument
        if args[i][0] == "-":  # Si le début de l'agument étudié commence par un tiret
            try:
                if args[i + 1][0] != "-":  # Alors on vérifie si le suivant est valeur
                    arguments[args[i]] = args[i + 1]  # Et dans ce cas on associe argument et valeur ensemble
                    break

            except:  # Si on arrive à des arguments, alors on ne peut pas vérifier si le suivant est une valeur
                pass  # Donc estime qu'il n'y a pas de valeur

            # S'il n'y a pas de valeur précisé après l'argument
            # Ou si on arrive à la fin des arguments donnés, alors on enregistre largument sans valeur
            arguments[args[i]] = None

    return arguments  # On retourne le dictionnaire des arguments