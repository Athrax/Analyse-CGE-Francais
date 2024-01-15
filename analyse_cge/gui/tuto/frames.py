import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from cli.gestionnaire_commande import *


class CadreMenu(ctk.CTkFrame):
    def afficher_detail_ministere(self):
        # self.master.cadre_principal.cadre_graphique_evolution_un_ministere.tkraise()
        pass

    def afficher_evolution_etat(self):
        self.master.cadre_principal.cadre_graphique_evolution_etat.tkraise()

    def afficher_evolution_un_ministere(self):
        self.master.cadre_principal.cadre_graphique_evolution_un_ministere.tkraise()

    def __init__(self, master):
        super().__init__(master)
        self.bouton_menu_detail_ministere = ctk.CTkButton(master=self, text="Détail d'un ministère",
                                                          command=self.afficher_detail_ministere)
        self.bouton_menu_detail_ministere.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

        self.bouton_menu_evolution_etat = ctk.CTkButton(master=self, text="Évolution de l'État",
                                                        command=self.afficher_evolution_etat)
        self.bouton_menu_evolution_etat.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

        self.bouton_menu_evolution_un_ministere = ctk.CTkButton(master=self, text="Evolution d'un ministère",
                                                                command=self.afficher_evolution_un_ministere)
        self.bouton_menu_evolution_un_ministere.grid(row=2, column=0, sticky="ew", padx=5, pady=5)


class CadreTitre(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.titre_haut = ctk.CTkLabel(self, text="Analyse CGE")
        self.grid_columnconfigure(0, weight=1)
        self.titre_haut.grid(row=0, column=0, padx=5, pady=5)


class CadrePrincipal(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Importer les différents menus
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.cadre_graphique_evolution_etat = CadreEvolutionEtat(self)
        self.cadre_graphique_evolution_un_ministere = CadreEvolutionUnMinistere(self)

        self.cadre_graphique_evolution_etat.grid(column=0, row=0, sticky="nswe")
        self.cadre_graphique_evolution_un_ministere.grid(column=0, row=0, sticky="nswe")


class CadreEvolutionUnMinistere(ctk.CTkFrame):
    def rafraichir(self, _):
        self.figure_evolution_ministere.clear()
        self.figure_evolution_ministere = graph_ministere_evolution(self.cont_choix_ministere.get(),
                                                                    self.cont_choix_echelle.get()).gcf().get_figure()
        self.canvas_evolution_ministere.draw()
        print(self.figure_evolution_ministere.figbbox)

    def __init__(self, master):
        super().__init__(master)

        self.cont_choix_ministere = ctk.StringVar(value=[*db][0])
        self.cont_choix_echelle = ctk.StringVar(value="semilog")

        self.bouton_choix_ministere = ctk.CTkOptionMenu(self, values=[*db],
                                                        command=self.rafraichir,
                                                        variable=self.cont_choix_ministere)
        self.bouton_choix_echelle = ctk.CTkOptionMenu(self, values=["semilog", "linéaire"],
                                                      command=self.rafraichir,
                                                      variable=self.cont_choix_echelle)

        self.bouton_choix_ministere.grid(row=1, column=0, padx=5, pady=(5, 5), sticky="nwse")
        self.bouton_choix_echelle.grid(row=1, column=1, padx=5, pady=(5, 5), sticky="nse")

        figure = graph_ministere_evolution(self.cont_choix_ministere.get(), self.cont_choix_echelle.get()).gcf().get_figure()
        self.figure_evolution_ministere = figure
        self.figure_evolution_ministere.set_dpi(80)
        self.canvas_evolution_ministere = FigureCanvasTkAgg(self.figure_evolution_ministere, self)
        self.canvas_evolution_ministere.draw()

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(1, weight=1)
        self.canvas_evolution_ministere.get_tk_widget().grid(row=0, column=0, padx=5, pady=5, sticky="nswe",
                                                             columnspan=2)


class CadreEvolutionEtat(ctk.CTkFrame):
    def rafraichir(self, _):
        self.figure_evolution_etat.clear()
        self.figure_evolution_etat = graph_etat_evolution(self.cont_choix_echelle.get()).gcf().get_figure()
        self.canvas_evolution_etat.draw()

    def __init__(self, master):
        super().__init__(master)

        self.cont_choix_echelle = ctk.StringVar(value="semilog")

        self.bouton_choix_echelle = ctk.CTkOptionMenu(self, values=["semilog", "linéaire"],
                                                      command=self.rafraichir,
                                                      variable=self.cont_choix_echelle)

        self.bouton_choix_echelle.grid(row=1, column=1, padx=5, pady=(5, 5), sticky="nse")
        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(1, weight=1)

        figure = graph_etat_evolution(self.cont_choix_echelle.get()).gcf().get_figure()
        self.figure_evolution_etat = figure
        self.figure_evolution_etat.set_dpi(80)
        self.canvas_evolution_etat = FigureCanvasTkAgg(self.figure_evolution_etat, self)
        self.canvas_evolution_etat.draw()

        self.grid_rowconfigure(0, weight=1)
        self.canvas_evolution_etat.get_tk_widget().grid(row=0, column=0, padx=5, pady=5, sticky="nswe", columnspan=2)


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
        self.cadre_menu.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="nsw")

        self.cadre_principal = CadrePrincipal(self)
        self.cadre_principal.grid(row=1, column=1, padx=(0, 10), pady=(10, 10), sticky="nsew")
        # self.cadre_principal.configure(fg_color="transparent")


app = FenetrePrincipale()
app.mainloop()
