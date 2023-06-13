import random
import inquirer
import time
import sched
import threading
import tkinter as tk
from tkinter import*
from tkinter import messagebox

class Tamagochi:
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness
    age = 0
    bored = 0
    food = 100
    exhausted = 0
    alive = True
    
    def __init__(self):
        question = [
            inquirer.Text("name", message="Quel est le nom de votre tamagochi?")
        ]
        answer = inquirer.prompt(question)
        self.name = answer.get("name")

    def create_pet(self):
        question = [
            inquirer.Text("name", message="Quel est le nom de votre tamagochi?")
        ]    
    # Afficher la boîte de dialogue avec la question
        reponse = inquirer.prompt(question)
        self.name = reponse.get("name")
    # Récupérer la réponse et l'afficher dans une boîte de dialogue Tkinter
        nom = reponse['name']
        messagebox.showinfo('Réponse', f'Coucou {nom}')

    def activity_eat(self):
        self.food = self.food + random.randint(1, 6)
        return ("Mange...", time.sleep(3.5))
       

    def activity_workout(self):
        self.food = self.food - random.randint(1, 6)
        self.bored = self.bored - random.randint(1, 11)
        self.exhausted = self.exhausted + random.randint(10, 21)
        return ("Fait du sport...", time.sleep(6))

    def activity_play(self):
        self.food = self.food - random.randint(1, 5)
        self.bored = self.bored - random.randint(10, 21)
        self.exhausted = self.exhausted + random.randint(10, 21)
        return ("Joue...", time.sleep(4))

    def activity_sleep(self):
        self.exhausted = 0
        self.food = 20
        return ("Endormi(e)...", time.sleep(10))

    def pass_time(self):
        self.age = self.age + random.randint(1, 3)
        self.bored = self.bored + random.randint(1, 5)
        self.food = self.food - random.randint(1, 5)
        self.exhausted = self.exhausted + 0.5

        if self.food <= 0 or self.exhausted >= 100:
            self.alive = False

    def status(self):
         messagebox.showinfo("Status",
            f"""
Nom: {self.name}\n
Age: {round(self.age)}\n
Nourriture: {self.food}\n
Ennui: {self.bored}\n
Energie: {self.exhausted}
-----------
        """
        )

    def main():
        # Créer une animal de compagnie
        tamago = Tamagochi()
        # Sleep pour les actions
        s = sched.scheduler(time.time, time.sleep)

        def run(sc):
            tamago.pass_time()
            if tamago.alive:
                s.enter(10, 1, run, (sc,))

        s.enter(10, 1, run, (s,))
        t = threading.Thread(target=s.run)
        t.start()

        while tamago.alive:
            tamago.run()

        print(f"{tamago.name} has died :(")

# Fonctions des boutons
def create_button_click():
    if messagebox.askyesno("Recréer", "Vous êtes sur(e) de vouloir recommencer?"):
        pet.create_pet()
        pet.status()

def eat_button_click():
    pet.activity_eat()
    pet.status()

def work_button_click():
    pet.activity_workout()
    pet.status()

def play_button_click():
    pet.activity_play()
    pet.status()

def sleep_button_click():
    pet.activity_sleep()
    pet.status()

def pass_button_click():
    if messagebox.askyesno("Passer", "Vous êtes sur(e) de vouloir passer?"):
        pet.pass_time()
        pet.status()

def quit_button_click():
    if messagebox.askyesno("Quit", "Vous êtes sur(e) de vouloir quitter?"):
        root.destroy()

# Créer une animal de compagnie
pet = Tamagochi()

# Créer une fenêtre Tkinter
root = tk.Tk()
root.title("TamagocHilel")
root.resizable(height=False, width=False)
label = Label(root, text="Coucou Toi !", fg="magenta", font=("Verdana", 20, "italic bold"))
label.pack()
# Label name Test
label_name = tk.Label(root, text="Nom:")
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()


mon_menu = Menu(root)
# Sous onglets (à mettre au dessus des onglet principaux)
fichier = Menu(mon_menu, tearoff=0) #tearoff=0 evite le vide du menu
fichier.add_command(label="Créer", command=create_button_click)
fichier.add_command(label="Quitter", command=quit_button_click)
options = Menu(mon_menu, tearoff=0)
options.add_command(label="Passer", command=pass_button_click)
# Les onglets
mon_menu.add_cascade(label="Fichier", menu=fichier)
mon_menu.add_cascade(label="Options", menu=options)

# create_button = tk.Button(root, text="Créer", command=create_button_click)
# create_button.pack()

root.config(menu=mon_menu)

# Preparation du canvas
can1 = tk.Canvas(root, bg='Salmon1', height=600, width=600)
can1.pack()

# Créer des boutons pour les actions
# bouton_question = tk.Button(root, text="Poser une question", command=poser_question)
# bouton_question.pack()

eat_button = tk.Button(root, text="Manger", command=eat_button_click)
eat_button.pack()

work_button = tk.Button(root, text="Sport", command=work_button_click)
work_button.pack()

play_button = tk.Button(root, text="Jouer", command=play_button_click)
play_button.pack()

sleep_button = tk.Button(root, text="Dormir", command=sleep_button_click)
sleep_button.pack()

root.mainloop()






