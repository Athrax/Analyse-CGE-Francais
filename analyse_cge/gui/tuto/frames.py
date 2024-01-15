import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from cli.gestionnaire_commande import *
from source.detection_donnees import en_tete_utiles as annees


class CadreMenu(ctk.CTkFrame):
    def afficher_evolution_etat(self):
        self.master.cadre_principal.cadre_graphique_evolution_etat.tkraise()

    def afficher_evolution_un_ministere(self):
        self.master.cadre_principal.cadre_graphique_evolution_un_ministere.tkraise()

    def afficher_repartition_ministeres(self):
        self.master.cadre_principal.cadre_graphique_repartition_ministeres.tkraise()

    def afficher_detail_ministere(self):
        # self.master.cadre_principal.cadre_graphique_evolution_un_ministere.tkraise()
        self.master.cadre_principal.cadre_graphique_detail_ministere.tkraise()

    def __init__(self, master):
        super().__init__(master)
        # Label Etat
        self.label_etat = ctk.CTkLabel(master=self, text="Etat")
        self.label_etat.grid(row=0, column=0)
        # Boutons Etat
        self.bouton_menu_evolution_etat = ctk.CTkButton(master=self, text="Évolution de l'État",
                                                        command=self.afficher_evolution_etat)
        self.bouton_menu_evolution_etat.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

        # Label Ministère
        self.label_etat = ctk.CTkLabel(master=self, text="Ministère")
        self.label_etat.grid(row=2, column=0)
        # Boutons Ministère
        self.bouton_menu_repartition_ministeres = ctk.CTkButton(master=self, text="Répartition entre ministère",
                                                          command=self.afficher_repartition_ministeres)
        self.bouton_menu_repartition_ministeres.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

        self.bouton_menu_detail_ministere = ctk.CTkButton(master=self, text="Détail d'un ministère",
                                                          command=self.afficher_detail_ministere)
        self.bouton_menu_detail_ministere.grid(row=4, column=0, sticky="ew", padx=5, pady=5)

        self.bouton_menu_evolution_un_ministere = ctk.CTkButton(master=self, text="Evolution d'un ministère",
                                                                command=self.afficher_evolution_un_ministere)
        self.bouton_menu_evolution_un_ministere.grid(row=5, column=0, sticky="ew", padx=5, pady=5)


class CadreTitre(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.titre_haut = ctk.CTkLabel(self, text="Analyse CGE")
        self.grid_columnconfigure(0, weight=1)
        self.titre_haut.grid(row=0, column=0, padx=5, pady=5)


class CadreRepartitionMinisteres(ctk.CTkFrame):
    def rafraichir(self, _):
        self.figure.clear()
        self.figure, self.axes = graph_ministeres(self.cont_ministere_inconnu.get(), self.cont_choix_annee.get(), self.cont_choix_dep_rec.get())
        self.figure.set_dpi(80)
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0, padx=5, pady=5, sticky="nswe", columnspan=3)

    def init_bouton(self):
        self.cont_choix_dep_rec = ctk.StringVar(value="Dépenses")
        self.bouton_choix_dep_rec = ctk.CTkOptionMenu(self, values=["Dépenses", "Recettes"],
                                                      command=self.rafraichir,
                                                      variable=self.cont_choix_dep_rec)
        self.bouton_choix_dep_rec.grid(row=1, column=2, padx=5, pady=(5, 5), sticky="nse")

        self.liste_annees = annees[3:]
        sorted(self.liste_annees)
        self.cont_choix_annee = ctk.StringVar(value=self.liste_annees[0])
        self.bouton_choix_annee = ctk.CTkOptionMenu(self, values=self.liste_annees, command=self.rafraichir,
                                                  variable=self.cont_choix_annee)
        self.bouton_choix_annee.grid(row=1, column=1, padx=5, pady=(5, 5), sticky="nwse")

        self.cont_ministere_inconnu = ctk.StringVar(value="Ministère connues")
        self.bouton_ministere_inconnu = ctk.CTkOptionMenu(self, values=["Ministère connues", "Ministère connues et inconnus"],
                                                         command=self.rafraichir,
                                                         variable=self.cont_ministere_inconnu)
        self.bouton_ministere_inconnu.grid(row=1, column=0, padx=5, pady=(5, 5), sticky="nwse")

        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def __init__(self, master):
        super().__init__(master)

        self.init_bouton()

        self.figure, self.axes = graph_ministeres(self.cont_ministere_inconnu.get(), self.cont_choix_annee.get(), self.cont_choix_dep_rec.get())
        self.figure.set_dpi(80)
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.draw()

        self.canvas.get_tk_widget().grid(row=0, column=0, padx=5, pady=5, sticky="nswe", columnspan=3)


class CadrePrincipal(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Importer les différents menus
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.cadre_graphique_evolution_etat = CadreEvolutionEtat(self)
        self.cadre_graphique_evolution_un_ministere = CadreEvolutionUnMinistere(self)
        self.cadre_graphique_detail_ministere = CadreDetailMinistere(self)
        self.cadre_graphique_repartition_ministeres = CadreRepartitionMinisteres(self)

        self.cadre_graphique_evolution_etat.grid(column=0, row=0, sticky="nswe")
        self.cadre_graphique_evolution_un_ministere.grid(column=0, row=0, sticky="nswe")
        self.cadre_graphique_detail_ministere.grid(column=0, row=0, sticky="nswe")
        self.cadre_graphique_repartition_ministeres.grid(column=0, row=0, sticky="nswe")


class CadreEvolutionEtat(ctk.CTkFrame):
    def rafraichir(self, _):
        self.figure.clear()
        self.figure, self.axes = graph_etat_evolution(self.cont_choix_echelle.get())
        self.figure.set_dpi(80)
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0, padx=5, pady=5, sticky="nswe", columnspan=2)


    def init_bouton(self):
        self.cont_choix_echelle = ctk.StringVar(value="semilog")
        self.bouton_choix_echelle = ctk.CTkOptionMenu(self, values=["semilog", "linéaire"],
                                                      command=self.rafraichir,
                                                      variable=self.cont_choix_echelle)
        self.bouton_choix_echelle.grid(row=1, column=1, padx=5, pady=(5, 5), sticky="nse")
        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def __init__(self, master):
        super().__init__(master)

        self.init_bouton()

        self.figure, self.axes = graph_etat_evolution(self.cont_choix_echelle.get())
        self.figure.set_dpi(80)
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.draw()

        self.canvas.get_tk_widget().grid(row=0, column=0, padx=5, pady=5, sticky="nswe", columnspan=2)


class CadreEvolutionUnMinistere(ctk.CTkFrame):
    def rafraichir(self, _):
        self.figure.clear()
        self.figure, self.axes = graph_ministere_evolution(self.cont_choix_ministere.get(),
                                                           self.cont_choix_echelle.get())
        self.figure.set_dpi(80)
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0, padx=5, pady=5, sticky="nswe", columnspan=2)

    def init_boutons(self):
        self.cont_choix_ministere = ctk.StringVar(value=[*db][0])
        self.bouton_choix_ministere = ctk.CTkOptionMenu(self, values=[*db], command=self.rafraichir, variable=self.cont_choix_ministere)
        self.bouton_choix_ministere.grid(row=1, column=0, padx=5, pady=(5, 5), sticky="nwse")

        self.cont_choix_echelle = ctk.StringVar(value="semilog")
        self.bouton_choix_echelle = ctk.CTkOptionMenu(self, values=["semilog", "linéaire"], command=self.rafraichir, variable=self.cont_choix_echelle)
        self.bouton_choix_echelle.grid(row=1, column=1, padx=5, pady=(5, 5), sticky="nse")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(1, weight=1)

    def __init__(self, master):
        super().__init__(master)

        self.init_boutons()

        self.figure, self.axes = graph_ministere_evolution(self.cont_choix_ministere.get(), self.cont_choix_echelle.get())
        self.figure.set_dpi(80)
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0, padx=5, pady=5, sticky="nswe", columnspan=2)


class CadreDetailMinistere(ctk.CTkFrame):
    def rafraichir(self, _):
        self.figure.clear()
        self.figure, self.axes = graph_postes(self.cont_choix_annee.get(), self.cont_choix_ministere.get(), self.cont_choix_echelle.get())

        self.figure.set_dpi(80)
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0, padx=5, pady=5, sticky="nswe", columnspan=3)

    def init_boutons(self):
        self.cont_choix_ministere = ctk.StringVar(value=[*db][0])
        self.bouton_choix_ministere = ctk.CTkOptionMenu(self, values=[*db], command=self.rafraichir, variable=self.cont_choix_ministere)
        self.bouton_choix_ministere.grid(row=1, column=0, padx=5, pady=(5, 5), sticky="nwse")

        self.liste_annees = annees[3:]
        sorted(self.liste_annees)
        self.cont_choix_annee = ctk.StringVar(value=self.liste_annees[0])
        self.cont_choix_annee = ctk.CTkOptionMenu(self, values=self.liste_annees, command=self.rafraichir,
                                                  variable=self.cont_choix_annee)
        self.cont_choix_annee.grid(row=1, column=1, padx=5, pady=(5, 5), sticky="nwse")

        self.cont_choix_echelle = ctk.StringVar(value="semilog")
        self.bouton_choix_echelle = ctk.CTkOptionMenu(self, values=["semilog", "linéaire"], command=self.rafraichir, variable=self.cont_choix_echelle)
        self.bouton_choix_echelle.grid(row=1, column=2, padx=5, pady=(5, 5), sticky="nse")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

    def __init__(self, master):
        super().__init__(master)

        self.init_boutons()

        self.figure, self.axes = graph_postes(self.cont_choix_annee.get(), self.cont_choix_ministere.get(), self.cont_choix_echelle.get())
        self.figure.set_dpi(80)
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0, padx=5, pady=5, sticky="nswe", columnspan=3)


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
