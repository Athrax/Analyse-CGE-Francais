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

def trie_croissant_X_Y(X, Y):
    """
    Fonction que trie par ordre décroissante une liste de flotants
    Args:
        liste (list): Liste de flotants

    Returns:
        list (list): Liste des flotants triés par ordre décroissant
    """

    magasin = list(zip(Y, X))  # Forme une liste avec couples X et Y
    magasin_trie = sorted(magasin)  # Trie les couples avec la première valeur de chaque couple (Y, X)
    Y, X = zip(*magasin_trie)  # On dissocie les deux listes
    return X, Y