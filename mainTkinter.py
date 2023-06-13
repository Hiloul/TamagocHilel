
import random
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

class Person:
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def get_older(self):
        self.age += 1
        self.health -= random.randint(1, 10)
        self.happiness -= random.randint(1, 10)

    def work(self):
        self.happiness -= random.randint(1, 5)

    def exercise(self):
        self.health += random.randint(1, 5)
        self.happiness += random.randint(1, 5)

    def socialize(self):
        self.happiness += random.randint(1, 5)

    def display_status(self):
        messagebox.showinfo("Status", f"Name: {self.name}\nAge: {self.age}\nHealth: {self.health}\nHappiness: {self.happiness}")

def age_button_click():
    person.get_older()
    person.display_status()

def work_button_click():
    person.work()
    person.display_status()

def exercise_button_click():
    person.exercise()
    person.display_status()

def socialize_button_click():
    person.socialize()
    person.display_status()

def quit_button_click():
    if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        root.destroy()

# Créer une personne avec des attributs initiaux
person = Person("Hiloul", 29, 100, 100)

# Créer une fenêtre Tkinter
root = tk.Tk()
root.title("BitLife")

# Créer des boutons pour les actions
age_button = tk.Button(root, text="Vieillir", command=age_button_click)
age_button.pack()

work_button = tk.Button(root, text="Travailler", command=work_button_click)
work_button.pack()

exercise_button = tk.Button(root, text="Faire de l'exercice", command=exercise_button_click)
exercise_button.pack()

socialize_button = tk.Button(root, text="Socialiser", command=socialize_button_click)
socialize_button.pack()

quit_button = tk.Button(root, text="Quitter", command=quit_button_click)
quit_button.pack()

root.mainloop()