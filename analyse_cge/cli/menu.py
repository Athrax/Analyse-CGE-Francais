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
from journalisation.traces import info, debug, avert, erreur
from source.gestionnaire_json import importer_json
from source.gestionnaire_arborescence import chemin, parent, grand_parent
from cli.gestionnaire_commande import commande
from source.detection_donnees import en_tete_utiles


def lf(n=1):
    while n: info(); n -= 1


def separateur():
    info("---")


def effacer_console(n=50):
    while n: print(""); n -=1


def affichage_menu():
    choix = ""
    separateur()
    menus = importer_config_menus()  # Importe la configuration du menu

    # On créer une liste qui contient le chemin du menu à chaque instant
    chemin_menu = ["menu"]

    while True:  # Boucle du menu
        # On recréer a chaque nouvelle commande le chemin vers le menu demandé
        # Sinon on ne peut pas effectuer de retour.
        # On part de la racine
        menu_courant = menus
        menu_parent = menus

        # Et on parcours le menu étape après étape
        for parcours in chemin_menu:  # On liste le chemin du menu
            menu_parent = menu_courant  # On se déplace au fur et à mesure
            menu_courant = menu_courant[parcours]  # On se déplace au fur et à mesure

        # On affiche le menu démandé
        # On déroule une liste créée avec tous les choix possibles et leur titre à partir du menu courant.
        # On déroule les elements (séparés par des virgules) d'un tuple contenant un générateur (compréhension)
        # des lignes à afficher correspondant aux choix du menu (menus_cli.json)
        if not "choix_annee" in [*menu_courant]:
            info(*(f"{menu_courant[choix]['titre']}: [{choix}]" for choix in menu_courant))
        else:  # Si l'entrée correspondait à un parametre (choix) plutot qu'un menu
            annee_min = en_tete_utiles[-1]
            annee_max = en_tete_utiles[3]
            info(f"{menu_courant['choix_annee']['titre']}")
            info(f"Années possibles : entre {annee_min} et {annee_max}")

        # On vérifie si une opération est à effectuer en arrivant dans le menu demandé
        # Une opération est effectuée nécessairement lorsque l'utilisateur à choisit une option finale dans le menu
        # Ainsi, les choix qui s'offrent à l'utiliseur sont réduit à "retour"
        # Si l'unique choix du menu actuel est "retour". Alors on vérifie si une action est à effectuer.
        # Cette action est associée à la clef operation dans le dictionnaire associé à la cle "retour".
        if ["retour"] == [*menu_courant]:  # Si la seule option possible dans le menu courant est choix, alors :
            operation = menu_parent["operation"]
            debug(f"L'opération {operation} est demandée")

            # On appel le gestionnaire de commande
            try:
                commande(operation, choix)
            except Exception as exc:
                avert(f"La commande {operation} a échouée", f"Erreur: {exc}",
                      "Veuillez entrer une commande ou paramètres valide",
                      "Retour [retour]")

        # On invite l'utilisateur à entrer la commande souhaitée
        entree = input("> ")
        info("> " + entree)  # On journalise l'entrée
        effacer_console()  # Puis on la cache pour l'utilisateur

        # On traite l'entrée de l'utilisateur
        # On peut executer la commande quitter à tout moment, dans tous les menus
        if entree == "quitter":
            break

        # Si l'on souhaite acceder au menu précédent
        # Qu'on tape retour, ou qu'on tape n'importe quoi et que retour est le seul choix possible
        elif (entree == "retour" and len(chemin_menu) > 1) or (
                ["retour"] == [*menu_courant] and entree not in [*menu_courant]):
            chemin_menu.pop()  # Mi chemin (on remonte aux paramtères du menu, comme le nom complet)
            chemin_menu.pop()  # Puis on revient au menu précédent

        # Dans le cas ou le menu demande à entrer une valeur ou choix propre à la volonté de l'utilisateur
        # alors il ne faut pas le considérer comme le nom d'un menu mais plutot comme une variable à retenir
        # Exemple: Demander à l'utilisateur une année. Il ne faut pas ouvrir un menu avec l'entrée, mais l'enregistrer.
        elif "choix_annee" in [*menu_courant]:
            choix = entree
            chemin_menu += ["choix_annee", "menu"]

        # On vérifie si la commande entrée existe
        # On déballe les choix possible dans le menu actuel
        elif entree in [*menu_courant]:
            chemin_menu += [entree, "menu"]

        # Si on tape une mauvaise commande, on reste dans le même menu
        # car on ne change pas le chemin de menu, on passe juste.
        else:
            pass


def importer_config_menus():
    try:
        # Le chemin est relatif pa rapport à main.py
        menus = importer_json(chemin("config", "menus_cli.json"))
        debug("Fichier de configuration des menus importé")
        return menus

    except FileNotFoundError as err:
        erreur("Aucun fichier de configuration des menus n'existe", err)
        sys.exit(1)


def cli():
    info("Bienvenue dans l'interface en ligne de commande du programme d'Analayse du CGE")
    affichage_menu()
