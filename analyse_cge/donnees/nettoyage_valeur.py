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
from analyse_cge.journalisation.traces import debug, avert


def savon(*valeurs):
    """
    Cette fonction nettoie les données. Son rôle est de ne retourner que des nombre flotant signés.
    Elle est programmée pour :
    - Effacer les guillements dans la cellule
    - Remplacer les virgules par un point
    - Remplacer les valeur vide ou avec un "-" par 0
    - Renvoyer les valeurs à 0 si elles n'ont pas réussies à être traitée
    Args:
        valeurs (tuple): Des valeurs a nettoyer.
    Returns:
        nombre (tuple): Valeurs nettoyée
    """
    debug(f"Nettoyage des valeurs {valeurs} ...")
    try:
        # Essaye de convertir en float la valeur directement obtenue
        return tuple(float(nombre) for nombre in valeurs)  # La valeur est déja un nombre

    except ValueError as err:  # La valeur n'est pas un nombre convertissable en float
        try:
            # On convertit toutes nos valeurs en chaine de caractère pour les traiter également
            valeurs = tuple(str(valeur) for valeur in valeurs)

            # Essaye en supprimant les guillements dans la cellule
            suppression_guillement = tuple(valeur.strip('"') for valeur in valeurs)

            # Remplace les virgules par des points
            remplacement_virgule = tuple(valeur.replace(",", ".") for valeur in suppression_guillement)

            # Si une valeur est vide ("") ou contient un trait ("-"), on remplace par 0
            remplissage_cellule = tuple(
                0 if valeur == "" or valeur == "-" else valeur for valeur in remplacement_virgule)

            # On créer le tuple nettoyé et on le renvoi
            nombres = tuple(float(valeur) for valeur in remplissage_cellule)
            debug(f"Valeurs nettoyées avec succès : {nombres}")
            return nombres

        except ValueError as err:  # La valeur semble ne pas contenir de nombre
            # Ces instructions sont executées si les valeurs de dépenses contient par exemple des lettres
            # On remplace la valeur récupérée par 0
            avert(f"Echec du nettoyage des valeurs : {valeurs}",
                  "Ces valeurs ont été rempalcées par 0",
                  err)
            return tuple(0 for valeur in valeurs)
