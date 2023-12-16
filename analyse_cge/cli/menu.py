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
import sys

from analyse_cge.journalisation.traces import info, debug, avert, erreur
from analyse_cge.fichier.gestionnaire_json import importer_json
from analyse_cge.fichier.gestionnaire_arborescence import chemin, parent, grand_parent


def lf(n=1):
    while n >= 0: info(); n += -1

def separateur():
    info("---")


def affichage_menu():
    separateur()
    menus = importer_config_menus() # Importe la configuration du menu

    # On créer une liste qui contient le chemin du menu à chaque instant
    chemin_menu = ["menu"]

    while True:  # Boucle du menu
        # On recréer a chaque nouvelle commande le chemin vers le menu demandé
        # Sinon on ne peut pas effectuer de retour.
        # On part de la racine
        menu_courant = menus

        # Et on parcours le menu étape après étape
        for parcours in chemin_menu: # On liste le chemin du menu
            menu_courant = menu_courant[parcours] # On se déplace au fur et à mesure

        # On affiche le menu démandé
        # On déroule une liste créée avec tous les choix possibles et leur titre à partir du menu courant.
        # Je n'ai pas copié collé cette ligne depuis Internet, et d'ailleurs aucune ligne ne l'est dans ce programme
        info(*(f"{menu_courant[choix]['titre']}: [{choix}]" for choix in menu_courant))


        # On vérifie si une opération est à effectuer en arrivant dans le menu demandé
        # Une opération est effectué nécessairement lorsque l'utilisateur à choisit une option finale dans le menu
        # Ainsi, les choix qui s'offrent à l'utiliseur sont réuit à "retour"
        # Si l'unique choix du menu actuel est "retour". Alors on vérifie si une action est à effectuer.
        # Cette action est associée à la clef operation dans le menu "retour".
        if ["retour"] == [*menu_courant]:
            operation = menu_courant["retour"]["operation"]
            info(f"L'opération {operation} est demandée")

        # On invite l'utilisateur à entrer la commande souhaitée
        commande = input("> ")

        if commande == "quitter": # On peut executer la commande quitter à tout moment, dans tous les menus
            break

        # Si l'on souhaite acceder au menu précédent
        elif commande == "retour" and len(chemin_menu) > 1:
            chemin_menu.pop() # Mi chemin (on remonte aux paramtères du menu, comme le nom complet)
            chemin_menu.pop() # Puis on revient au menu précédent

        # On vérifie si la commande tapée
        # On déballe les choix possible dans le menu actuel
        elif commande in [*menu_courant]:
            chemin_menu += [commande, "menu"]

        # Si on tape une mauvaise commande, on reste dans le même menu
        # car on ne change pas le chemin de menu, on passe juste.
        else:
            pass

        # On vérifie si une fonction doit être executée ou non

def importer_config_menus(chemin_fichier="config/menus_cli.json"):
    try:
        menus = importer_json(chemin(grand_parent(__file__),chemin_fichier))
        debug("Fichier de configuration des menus importé")
        return menus

    except FileNotFoundError as err:
        erreur("Aucun fichier de configuration des menus n'existe", err)
        sys.exit(1)


def cli():
    info("Bienvenue dans l'interface en ligne de commande du programme d'Analayse du CGE")
    affichage_menu()

cli()