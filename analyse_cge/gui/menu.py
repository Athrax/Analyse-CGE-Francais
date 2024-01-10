#  ==============================================================================
#   Copyright (c) 2023 Aymeric Schaeffer et Lise Renaud
#
#   Permission vous est accordée de copier, distribuer et/ou modifier ce code
#   sous les termes de la licence open source.
#
#   Ce programme est distribué dans l'espoir qu'il sera utile, mais SANS
#   AUCUNE GARANTIE ; sans même la garantie implicite de COMMERCIALISATION
#   ou D'ADAPTATION À UN OBJET PARTICULIER. Voir la licence pour plus de détails.
#
#   Vous devriez avoir reçu une copie de la licence avec ce programme. Sinon,
#   consultez.
#  ==============================================================================

from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("1000x550")
app.resizable(0, 0)


def button_function():
    print("button pressed")


# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="Menu", command=button_function)
button.place(relx=0, rely=0, anchor=customtkinter.NW)
button.configure(height=50, width=120)

button1 = customtkinter.CTkButton(master=app, text="Evolution", command=button_function)
button1.place(relx=0, rely=0.10, anchor=customtkinter.NW)
button1.configure(height=50, width=120)

button2 = customtkinter.CTkButton(master=app, text="Ministeres", command=button_function)
button2.place(relx=0, rely=0.20, anchor=customtkinter.NW)
button2.configure(height=50, width=120)

button4 = customtkinter.CTkButton(master=app, text="Etat", command=button_function)
button4.place(relx=0, rely=0.30, anchor=customtkinter.NW)
button4.configure(height=50, width=120)


app.mainloop()
