import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


class CadreMenu(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        bouton_menu_detail_ministere = ctk.CTkButton(master=self, text="Détail d'un ministère")
        bouton_menu_detail_ministere.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        bouton_menu_evolution_tous_ministere = ctk.CTkButton(master=self, text="Évolution des ministères")
        bouton_menu_evolution_tous_ministere.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        bouton_menu_evolution_un_ministere = ctk.CTkButton(master=self, text="Evolution d'un ministère")
        bouton_menu_evolution_un_ministere.grid(row=2, column=0, sticky="ew", padx=5, pady=5)


class CadreTitre(ctk.CTkFrame):
    def __init__(self, master, ):
        super().__init__(master)
        self.titre_haut = ctk.CTkLabel(self, text="Analyse CGE")
        self.grid_columnconfigure(0, weight=1)
        self.titre_haut.grid(row=0, column=0, padx=5, pady=5)


class CadrePrincipal(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Importer les différents menus
        self.cadre_graphique_evolution_un_ministere = MenuEvolutionUnMinistere(self)
        self.cadre_graphique_evolution_un_ministere.grid(column=0, row=0, sticky="nswe")



        # Placer celui demandé en haut de la pile




class MenuEvolutionUnMinistere(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.graphique_figure = Figure()
        self.graphique_axes = self.graphique_figure.add_subplot(111)
        self.graphique_axes.plot(["2012", "2013", "2014", "2015", "2016", "2017", "2018"],[10, 20, 30, 40, 50, 60, 70],[30, 40, 50, 60, 70, 80, 90])
        self.canvas = FigureCanvasTkAgg(self.graphique_figure, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=ctk.TOP, fill=ctk.BOTH, expand=1)

        self.bind("<Configure>", self.au_redimmensionnement)

    def au_redimmensionnement(self, event):
        width = self.winfo_width()
        height = self.winfo_height()
        self.graphique_figure.set_size_inches(width / 100, height / 100)
        self.canvas.draw()
        print(f"redim")


class FenetrePrincipale(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title = "Analyse du Compte Général de l'État Français"
        self.geometry("800x500")
        self.minsize(width=800, height=500)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.cadre_titre = CadreTitre(self)
        self.cadre_titre.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nswe", columnspan=2)

        self.cadre_menu = CadreMenu(self)
        self.cadre_menu.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="nsw")

        self.cadre_principal = CadrePrincipal(self)
        self.cadre_principal.grid(row=1, column=1, padx=(0,10), pady=(10, 0), sticky="nsew")
        self.cadre_principal.configure(fg_color="transparent")

        self.bouton = ctk.CTkButton(self, text="my button")
        self.bouton.grid(row=2, column=0, padx=10, pady=10, sticky="ew", columnspan=2)


app = FenetrePrincipale()
app.mainloop()

