import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random

def center_window(window):
    window.update_idletasks()
    width = window.winfo_reqwidth()
    height = window.winfo_reqheight()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f"{300}x{height}+{x}+{y}")

class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def attack_target(self, target):
        damage_dealt = random.randint(1, self.attack)
        target.take_damage(damage_dealt)
        self.update_hp_labels()
        if target.is_alive():
            target.attack_back(self)

    def attack_back(self, target):
        damage_dealt = random.randint(1, self.attack)
        target.take_damage(damage_dealt)
        self.update_hp_labels()

    def update_hp_labels(self):
        player_hp_label.config(text=f"{player.name}'s HP: {player.hp}")
        enemy_hp_label.config(text=f"{enemy.name}'s HP: {enemy.hp}")
        if not player.is_alive():
            messagebox.showinfo("Game Over", "You were defeated!")
        elif not enemy.is_alive():
            messagebox.showinfo("Victory", "You defeated the enemy!")

def start_game():
    global player, enemy
    player_name = name_entry.get()
    if player_name:
        player = Character(player_name, 100, 20)
        enemy = Character("Dragon", 50, 10)
        root.deiconify()
        name_window.destroy()

        player_hp_label.config(text=f"{player.name}'s HP: {player.hp}")
        player_hp_label.pack()

        enemy_hp_label.config(text=f"{enemy.name}'s HP: {enemy.hp}")
        enemy_hp_label.pack()

        attack_button.config(command=lambda: player.attack_target(enemy))
        attack_button.pack()

root = tk.Tk()
root.title("Simple RPG Game")
root.geometry("400x400")
root.withdraw()  # Hide the main window until player's name is entered
center_window(root)

name_window = tk.Toplevel(root)
name_window.title("Enter Your Name")
name_window.geometry("200x400")
center_window(name_window)

name_label = tk.Label(name_window, text="Enter Your Name:")
name_label.pack()

name_entry = tk.Entry(name_window)
name_entry.pack()

start_button = tk.Button(name_window, text="Start Game", command=start_game)
start_button.pack()

player_hp_label = tk.Label(root, text="")
enemy_hp_label = tk.Label(root, text="")

attack_button = tk.Button(root, text="Attack")
# attack_button.pack()  # This line is moved inside start_game

name_window.mainloop()