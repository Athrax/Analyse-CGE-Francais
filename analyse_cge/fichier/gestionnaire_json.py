import json
import os

from analyse_cge.journalisation.traces import *

exemple = {
    "ministeres" : {
        "finance" : {
            "somme_depense" : 2003040934,
            "postes" : {
                "1er poste" : {
                    2012 : 29389383,
                    2022 : 298329839
                },
                "2eme poste" : {
                    2012 : 29389383,
                    2022 : 298329839
                }
            },
            "sous_postes" : {
                "dettes" : {
                    2012 : 29389383,
                    2022 : 298329839
                },
                "produit regalier" : {
                    2012 : 29389383,
                    2022 : 298329839
                }
            }
        },
        "intérieur" : {
            "somme_depense" : 39422340934,
            "postes" : {
                "1er poste" : {
                    2012 : 29389383,
                    2022 : 298329839
                },
                "2eme poste" : {
                    2012 : 29389383,
                    2022 : 298329839
                }
            },
            "sous_postes" : {
                "dettes" : {
                    2012 : 29389383,
                    2022 : 298329839
                },
                "produit regalier" : {
                    2012 : 29389383,
                    2022 : 298329839
                }
            }
        }
    }
}

def exemple():
    with open("exemple.json", 'w') as json_file:
        json.dump(exemple, json_file, indent=2)

    with open("exemple.json", 'r') as json_file:
        dictionnaire_importe = json.load(json_file)
        print(dictionnaire_importe)

def sauvegarder_json(dictionnaire, chemin_json):  # Sauvargder en fichier json un dictionnaire
    if ".json" not in chemin_json:
        chemin_json += ".json"
        info(f"Le nom du fichier json à sauvegarder à été modifier en {chemin_json}")
    try:
        with open(chemin_json, 'w') as json_file:
            json.dump(exemple, json_file, indent=2)
            info(f"Le fichier json à été sauvegardé : {chemin_json}")
    except IOError as err:
        erreur(f"{err}", f"Impossible de créer le fichier {chemin_json},")

def importer_json(chemin_json):
    try:
        with open("exemple.json", 'r') as json_file:
            info(f"Le fichier {chemin_json} json à été importé")
            return json.load(json_file)
    except IOError as err:
        print(os.listdir())
        erreur(f"{err}", f"Impossible d'ouvrir le fichier {chemin_json},")


