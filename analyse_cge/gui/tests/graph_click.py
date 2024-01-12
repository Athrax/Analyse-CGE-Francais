import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class MatplotlibTkinterApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Matplotlib dans Tkinter")

        # Créer une instance de la classe Figure de Matplotlib
        self.fig = Figure(figsize=(3, 2), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.pie([10, 20, 30], labels=["Partie A", "Partie B", "Partie C"], autopct='%1.1f%%')

        # Créer un canvas Tkinter pour afficher le graphique
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.NONE)

        self.canvas.mpl_connect("button_press_event", self.on_pie_click)

    def on_pie_click(self, quelquechose):
        print("click")
        print(quelquechose)


if __name__ == "__main__":
    fenetre = MatplotlibTkinterApp()
    fenetre.geometry("1000x550")
    fenetre.resizable(width=0, height=0)

    fenetre.mainloop()
