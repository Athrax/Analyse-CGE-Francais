import json

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

#def sauvegarder_csv(chemin_fichier):
    #with open(chemin_fichier, 'w') as csv_file:

