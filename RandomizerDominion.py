# Randomizer for Dominion Setup
# Finished so far, but potentially to do:
# - Catch the edge case if a user tries to generate more cards of any given expansion that this expansion has
# - customtkinter design?

# I realize now that I should have made "Card" a class - would've been more DRY

# MAX CARDS nach Set
    # Basis: 25
    # Mix: 25
    # Intrigen: 25
    # Abenteurer: 30

import random
import tkinter as tk
from tkinter import *
import logging

logging.basicConfig(level=logging.INFO, filename="RanDom.log", filemode="w", 
format="%(asctime)s: %(levelname)s - %(message)s")

## The Randomizer ##
global list_of_cards
list_of_cards = []

def choose_game():
    return random.randint(1, 4)

def choose_card(game):
    cards_in_expansion = 0
    if game == 1 or 2 or 3:
        cards_in_expansion = 25
    elif game == 4:
        cards_in_expansion = 25
    
    card = random.randint(1, cards_in_expansion)
    while (game, card) in list_of_cards:
            card = random.randint(1, 25)
            logging.info("Card already in list of drawn cards, generate new draw")

    match game:
        case 1:
            intro_label.configure(bg="#d2b48c")
            root.configure(bg="#d2b48c")
            result_field.insert('1.0', "Basisspiel, Karte " + str(card) + "\n")
        case 2:
            intro_label.configure(bg="#ffe5b4")
            root.configure(bg="#ffe5b4")
            result_field.insert('1.0', "Mixbox, Karte " + str(card) + "\n")
        case 3:
            intro_label.configure(bg="#add8e6")
            root.configure(bg="#add8e6")
            result_field.insert('1.0', "Die Intrige, Karte " + str(card) + "\n")
        case 4:
            root.configure(bg="#b22222")
            intro_label.configure(bg="#b22222")
            result_field.insert('1.0', "Abenteurer, Karte " + str(card) + "\n")

    logging.info("Length of list of cards is now %s", len(list_of_cards))
    if len(list_of_cards) == 9:
        intro_label_text.set("10 Karten generiert.")
        logging.info("10 cards generated: %s and (%s, %s) which is about to be added", list_of_cards, game, card)
    return (game, card)

def add_to_list(game_card_pair):
    list_of_cards.append(game_card_pair)
    logging.debug("Card %s added", game_card_pair)
    logging.debug("List of cards is now: %s (%s length)", list_of_cards, len(list_of_cards))

global cards
cards_draw = 1

## GUI ##
def button_clicked():
    add_to_list(choose_card(choose_game()))

button_color = "#e7feff"

root = tk.Tk()
root.title("Dominion Randomizer")
intro_label_text = StringVar()
intro_label_text.set("Willkommen zum Dominion Randomizer!")
intro_label = Label(root, textvariable=intro_label_text, font=("Arial", 15), width=32)
button_generate = Button(root, text="Nächste Karte generieren", bg=button_color, command=button_clicked)
result_field = Text(root, height=10, width=18, font=("Arial", 19))

intro_label.grid(row=0, column=0, padx=10, pady=0)
button_generate.grid(row=1, column=0, pady=15)
result_field.grid(row=3, column=0, padx=5)


## Window Size & Position ##
width, height = 380, 400
screen_w, screen_h = root.winfo_screenwidth(), root.winfo_screenheight()
winpos_x, winpos_y = int(screen_w/2 - width/2), int(screen_h/2 - height/2)
root.geometry(f'{width}x{height}+{winpos_x}+{winpos_y}') # make sure the window is centered on user's screen
#root.resizable(False, False)

if __name__ == "__main__":
    root.mainloop()