import os
import time
import sched
import threading
import inquirer


class Tamagotchi:
    age = 0
    bored = 0
    food = 100
    exhausted = 0
    alive = True

    def __init__(self):
        question = [
            inquirer.Text("name", message="What's the name of your tamagotchi?")
        ]
        answer = inquirer.prompt(question)
        self.name = answer.get("name")

    def activity_eat(self):
        self.food = self.food + 2.5
        return ("Eating...", 3.5)

    def activity_drink(self):
        self.food = self.food + 0.5
        return ("Drinking...", 2.5)

    def activity_workout(self):
        self.food = self.food - 5
        self.bored = self.bored - 10
        self.exhausted = self.exhausted + 20
        return ("Working out...", 6)

    def activity_play(self):
        self.food = self.food - 2
        self.bored = self.bored - 20
        self.exhausted = self.exhausted + 10
        return ("Playing a game...", 4)

    def activity_sleep(self):
        self.exhausted = 0
        self.food = 20
        return ("Sleeping...", 10)

    def pass_time(self):
        self.age = self.age + 0.2
        self.bored = self.bored + 2.5
        self.food = self.food - 5
        self.exhausted = self.exhausted + 0.5

        if self.food < -20 or self.exhausted >= 100:
            self.alive = False

    def status(self):
        print(
            f"""
Name: {self.name}
Age: {round(self.age)}
Food: {self.food}
Bored: {self.bored}
Exhausted: {self.exhausted}
-----------
        """
        )

    def run(self):
        self.clear()
        self.status()
        question = [
            inquirer.List(
                "activity",
                message="What should we do?",
                choices=["Eat", "Drink", "Workout", "Play", "Sleep"],
            ),
        ]
        answer = inquirer.prompt(question)
        activity_name = "activity_{}".format(answer.get("activity")).lower()
        activity = getattr(self, activity_name, lambda: "Invalid activity")
        (status, sleep) = activity()
        print(status)
        time.sleep(sleep)

    def clear(self):
        if os.name == "nt":
            _ = os.system("cls")
        else:
            _ = os.system("clear")


def main():
    tamago = Tamagotchi()

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


if __name__ == "__main__":
    main()