import tkinter as tk

class Tamagotchi:
    def __init__(self):
        self.energie = 100
        self.sante = 100
        self.humeur = 100

    def nourrir(self):
        self.energie += 10
        self.sante += 5
        self.humeur += 5
        self.afficher_statut()

    def jouer(self):
        self.energie -= 5
        self.sante += 5
        self.humeur += 10
        self.afficher_statut()

    def dormir(self):
        self.energie += 20
        self.sante += 10
        self.humeur += 5
        self.afficher_statut()

    def afficher_statut(self):
        statut = f"Energie: {self.energie}\nSanté: {self.sante}\nHumeur: {self.humeur}"
        label_statut.config(text=statut)

# Créer une instance de Tamagotchi
tamagotchi = Tamagotchi()

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Tamagotchi")

# Créer les boutons
bouton_nourrir = tk.Button(fenetre, text="Nourrir", command=tamagotchi.nourrir)
bouton_nourrir.pack()

bouton_jouer = tk.Button(fenetre, text="Jouer", command=tamagotchi.jouer)
bouton_jouer.pack()

bouton_dormir = tk.Button(fenetre, text="Dormir", command=tamagotchi.dormir)
bouton_dormir.pack()

# Créer l'étiquette pour afficher le statut du Tamagotchi
label_statut = tk.Label(fenetre, text="")
label_statut.pack()

# Lancer la boucle principale
fenetre.mainloop()
