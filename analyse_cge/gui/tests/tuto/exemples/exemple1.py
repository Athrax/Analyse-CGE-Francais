import customtkinter


class PageSwitcherApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Page Switcher App")

        # Configuration de la grille
        self.grid_columnconfigure(0, weight=1)  # Colonne principale s'étend horizontalement
        self.grid_rowconfigure(0, weight=1)     # Première rangée s'étend verticalement

        # Création d'un menu vertical à droite
        self.page_textbox = customtkinter.CTkTextbox(self, wrap="none", state="disabled")
        self.page_textbox.grid(row=0, column=1, padx=20, pady=20, sticky="ns")  # Collé à droite

        # Ajoutez des éléments au menu (pages de l'application)
        pages = ["Page 1", "Page 2", "Page 3"]  # Ajoutez vos noms de page ici
        for page in pages:
            self.page_textbox.insert("end", page + "\n")

        # Ajout d'un gestionnaire d'événements pour détecter la sélection de page
        self.page_textbox.bind("<ButtonRelease-1>", self.switch_page)

        # Initialisation de la première page
        self.current_page = customtkinter.CTkFrame(self)  # Initialisez avec un cadre vide
        self.switch_page()

    def switch_page(self, event=None):
        # Méthode appelée lorsqu'une nouvelle page est sélectionnée dans le menu
        selected_index = self.page_textbox.index("current")
        if selected_index:
            # Obtenez le nom de la page sélectionnée
            selected_page = self.page_textbox.get(selected_index).strip()

            # Affichez la page correspondante (vous devrez implémenter cette méthode)
            self.display_page(selected_page)

    def display_page(self, page_name):
        # Méthode pour afficher la page spécifiée
        # Vous devrez implémenter la logique pour afficher le contenu de chaque page
        # Par exemple, vous pourriez utiliser des cadres différents pour chaque page
        # et basculer la visibilité en fonction de la page sélectionnée.
        self.current_page.grid_forget()  # Effacez le widget précédent de la grille

        if page_name == "Page 1":
            self.current_page = self.create_page1()
        elif page_name == "Page 2":
            self.current_page = self.create_page2()
        elif page_name == "Page 3":
            self.current_page = self.create_page3()

        self.current_page.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")  # Collé à gauche

    def create_page1(self):
        # Méthode pour créer le contenu de la page 1
        # Retournez le cadre ou widget approprié pour cette page
        return customtkinter.CTkLabel(self.current_page, text="Contenu de la Page 1")

    def create_page2(self):
        # Méthode pour créer le contenu de la page 2
        # Retournez le cadre ou widget approprié pour cette page
        return customtkinter.CTkLabel(self.current_page, text="Contenu de la Page 2")

    def create_page3(self):
        # Méthode pour créer le contenu de la page 3
        # Retournez le cadre ou widget approprié pour cette page
        return customtkinter.CTkLabel(self.current_page, text="Contenu de la Page 3")

if __name__ == "__main__":
    app = PageSwitcherApp()
    app.mainloop()
