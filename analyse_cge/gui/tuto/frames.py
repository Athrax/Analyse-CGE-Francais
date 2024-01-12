import customtkinter as ctk

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
    def __init__(self, master):
        super().__init__(master)
        self.titre_haut = ctk.CTkLabel(self, text="Analyse CGE")
        self.grid_columnconfigure(0, weight=1)
        self.titre_haut.grid(row=0, column=0, padx=5, pady=5)

class FenetrePrincipale(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title = "Analyse du Compte Général de l'État Français"
        self.geometry("480x280")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.checkbox_frame = CadreTitre(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nswe")

        self.checkbox_frame = CadreMenu(self)
        self.checkbox_frame.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="nsw")

        self.button = ctk.CTkButton(self, text="my button")
        self.button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

app = FenetrePrincipale()
app.mainloop()
