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



    def activity_eat(self):
        self.food = self.food + random.randint(1, 6)
        return ("Mange...", 3.5)

    def activity_workout(self):
        self.food = self.food - random.randint(1, 6)
        self.bored = self.bored - random.randint(1, 11)
        self.exhausted = self.exhausted + random.randint(10, 21)
        return ("Fait du sport...", 6)

    def activity_play(self):
        self.food = self.food - random.randint(1, 5)
        self.bored = self.bored - random.randint(10, 21)
        self.exhausted = self.exhausted + random.randint(10, 21)
        return ("Joue...", 4)

    def activity_sleep(self):
        self.exhausted = 0
        self.food = 20
        return ("Endormi(e)...", 10)

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
  
    def run(self):
        self.clear()
        self.status()
        question = [
            inquirer.List(
                "activity",
                message="Que voulez-vous faire?",
                choices=["Eat", "Drink", "Workout", "Play", "Sleep"],
            ),
        ]
        answer = inquirer.prompt(question)
        activity_name = "activity_{}".format(answer.get("activity")).lower()
        activity = getattr(self, activity_name, lambda: "Invalid activity")
        (status, sleep) = activity()
        print(status)
        time.sleep(sleep)



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


# if __name__ == "__main__":
#     main()




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

mon_menu = Menu(root)
# Sous onglet
fichier = Menu(mon_menu, tearoff=0)
fichier.add_command(label="Quitter", command=quit_button_click)
options = Menu(mon_menu, tearoff=0)
options.add_command(label="Passer", command=pass_button_click)
# Les onglets
mon_menu.add_cascade(label="Fichier", menu=fichier)
mon_menu.add_cascade(label="Options", menu=options)

root.config(menu=mon_menu)



# Label input inclus
# def inputFunction():
#     if mon_input.get() == "hiloul":
#         print("cc")
#     else:
#         print("byebye")
# mon_input = StringVar()
# label8 = Label(root, text="test")
# label8.pack()
# entree=Entry(root, textvariable=mon_input)
# entree.pack()
# bouton = Button(root, text="Ok", textvariable=inputFunction)
# bouton.pack()

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

# pass_button = tk.Button(root, text="Passer", command=pass_button_click)
# pass_button.pack()

# quit_button = tk.Button(root, text="Quitter", command=quit_button_click)
# quit_button.pack()

root.mainloop()


