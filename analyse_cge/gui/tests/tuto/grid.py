import customtkinter as ctk

fenetre_principal = ctk.CTk()  # Objet de la fenetre
fenetre_principal.title("my app")  # Titre de la fenetre
fenetre_principal.geometry("800x450")  # Taille de la fenetre

# Parametrage de la grille
fenetre_principal.grid_columnconfigure(0, weight=1)
fenetre_principal.grid_columnconfigure(1, weight=4)
fenetre_principal.grid_rowconfigure(0, weight=2)
fenetre_principal.grid_rowconfigure(1, weight=2)


# Ajout d'un bouton
bouton = ctk.CTkButton(fenetre_principal, text="OK", command=print("coucou"))
bouton.grid(row=0, column=0, padx=5, pady=5, sticky="e")  # Placement du bouton sur la grille


fenetre_principal.mainloop()