import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from cli.gestionnaire_commande import graph_ministeres
from source.gestionnaire_json import importer_json
from source.gestionnaire_arborescence import chemin, grand_parent
from affichage.gestionnaire_affichage import affichage_pie
from journalisation.traces import *


class MatplotlibTkinterApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Matplotlib dans Tkinter")

        # Créer une instance de la classe Figure de Matplotlib
        self.fig = Figure(figsize=(3, 2), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.graph_ministere(False)

        # Créer un canevas Tkinter pour afficher le graphique
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.NONE)


    def graph_ministere(self, ministere_inconnu):
        # Chargment de la base de donnée
        db = importer_json(chemin("../../..", "docs", "db_ministere.json"))

        labels = [*db]
        if ministere_inconnu:
            valeurs = [-int(db[ministere]["dépense_annuelle"]["2022"]) for ministere in [*db]]
        else:
            valeurs = [-int(db[ministere]["dépense_annuelle"]["2022"]) for ministere in [*db]
                       if ministere != "Non renseigné"]
            labels.pop(labels.index("Non renseigné"))

        titre = "Dépenses des ministères en 2022"

        self.ax.pie(valeurs, labels=labels, autopct='%1.1f%%')


if __name__ == "__main__":
    fenetre = MatplotlibTkinterApp()
    fenetre.geometry("1000x550")
    fenetre.resizable(width=0, height=0)

    fenetre.mainloop()
