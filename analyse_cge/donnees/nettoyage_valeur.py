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

def savon(*valeurs):
    """
    Cette fonction nettoie les données. Son rôle est de ne retourner que des nombre flotant signés.
    Args:
        valeurs (tuple): Des valeurs a nettoyer.
    Returns:
        nombre (tuple): Valeurs nettoyée
    """
    try :
        return tuple(float(nombre) for nombre in valeurs)
    except:
        #try
        pass