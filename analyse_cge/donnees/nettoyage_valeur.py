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
from journalisation.traces import debug, avert


def savon_a_chiffres(*valeurs):
    """
    Cette fonction nettoie les données. Son rôle est de ne retourner que des nombre flotant signés.
    Elle est programmée pour :
    - Effacer les guillements dans la cellule
    - Remplacer les virgules par un point
    - Remplacer les valeur vide ou avec un "-" par 0
    - Renvoyer les valeurs à 0 si elles n'ont pas réussies à être traitée
    Args:
        valeurs (tuple): Valeurs a nettoyer.
    Returns:
        nombre (tuple): Tuple des flotants nettoyés
    """
    debug(f"Nettoyage des valeurs {valeurs} ...")
    try:
        # Essaye directement de convertir en float la valeur à traiter
        if len(valeurs) == 1:
            return float(valeurs[0])
        else:
            return tuple(float(nombre) for nombre in valeurs)  # Ici, on convertit les string en float

    except ValueError as err:  # Si les valeurs ne sont pas des convertissables en float
        try:  # Alors on continue de les convertir :
            # On convertit toutes nos valeurs en chaine de caractère pour les traiter également
            valeurs = tuple(str(valeur) for valeur in valeurs)

            # Supprime les guillements dans la cellule
            suppression_guillement = tuple(valeur.strip('"').strip(" ") for valeur in valeurs)

            # Remplace les virgules par des points
            remplacement_virgule = tuple(valeur.replace(",", ".") for valeur in suppression_guillement)

            # Si une valeur est vide ("") ou contient un trait ("-"), on remplace par 0.0
            remplissage_cellule = tuple(
                0.0 if valeur == "" or valeur == "-"
                else valeur
                for valeur in remplacement_virgule)

            # On créer le tuple nettoyé et on le renvoi
            if len(valeurs) == 1:
                nombres_savonnes = float(remplissage_cellule[0])
            else:
                # Ici, on convertit les string en float
                nombres_savonnes = tuple(float(valeur) for valeur in remplissage_cellule)

            debug(f"Valeurs nettoyées avec succès : {nombres_savonnes}")
            return nombres_savonnes

        except ValueError as err:  # La valeur semble ne pas contenir de nombre
            # Ces instructions sont executées si les valeurs de dépenses contient par exemple des lettres
            # On remplace la valeur récupérée par 0
            debug(f"Echec du nettoyage des valeurs : {valeurs}",
                  "Ces valeurs ont été rempalcées par 0",
                  err)
            return tuple(0.0 for _ in valeurs)


def savon_a_lettres(*valeurs):
    """
    Cette fonction nettoie les données textuelles. Son rôle est de nettoyer les caractère qui poseraient problème
    dans une chaine de caractère
    Elle est programmée pour :
    - Effacer les esapces inutiles dans la cellule

    Args:
        valeurs (tuple): Valeurs a nettoyer.
    Returns:
        nombre (tuple): Tuple des string nettoyés
    """
    debug(f"Nettoyage des valeurs {valeurs} ...")
    try:  # Alors on continue de les convertir :
        # On convertit toutes nos valeurs en chaine de caractère pour les traiter également
        valeurs = tuple(str(valeur) for valeur in valeurs)

        # Supprime les espaces inutiles dans la cellule
        suppression_espace = tuple(valeur.strip(" ") for valeur in valeurs)

        debug(f"Valeurs nettoyées avec succès : {suppression_espace}")

        # Si une seule valeur est donnée à nettoyer
        if len(valeurs) == 1:
            return suppression_espace[0]
        else: # Si plusieurs, on renvoi un tuple
            return suppression_espace

    except ValueError as err:  # La valeur semble ne pas contenir de nombre
        # Ces instructions sont executées si les valeurs de dépenses contient par exemple des lettres
        # On remplace la valeur récupérée par 0
        avert(f"Echec du nettoyage des valeurs : {valeurs}",
              "Ces valeurs n'ont pas été néttoyées",
              err)
        return valeurs
