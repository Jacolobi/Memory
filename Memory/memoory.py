# Written by Jacob Andersson <jaan0078@umu.se>, Anton Bonli <anbo0205@umu.se>, Madeleine Englund <maen0191@ad.umu.se> & Sarah Lorenzo <salo0038@umu.se> .
# May be used in the course Applikationsprogrammering i Python at Umeå University.
# Usage exept those listed above requires permission by the author.

"""
Purpose is to create a GUI memory game.
"""

from tkinter import *
from PIL import ImageTk, Image
import random

class game:
    def __init__(self, master):
        """
             Purpose: Creates the game board and stores all the images in a dictionary with a specifik key.
             Parameters: - 
             Returns: - 
             Comment: -
        """
        self.master = master
        master.title("Moomory")
        master.iconbitmap("cow-1.ico")
        self.pairs = 0
        self.img_dict = {}
        self.img_keys = []
        self.flipped_cards = []
        self.flipped = 0
        self.flipped_keys = []
        
        f = open("images.txt")
        lines = f.readlines()
        for p in range(8):
            img_name = lines[p].strip("\n")
            for i in range(2):
                img = ImageTk.PhotoImage(Image.open(img_name))
                key = i*8+p
                self.img_dict[key] = img
        self.img_keys = list(self.img_dict.keys())
        random.shuffle(self.img_keys)
        
        
    def flipped_card(self, card):
        """
             Purpose: Compare cards when two are flipped.
             Parameters: card - the card that the user clicked.
             Returns: - 
             Comment:  If cards match they stay flipped, otherwise they flip back.
        """
        self.flipped_cards.append(card)
        self.flipped_keys.append(card.key)
        if self.flipped == 0:
            self.flipped = 1
        elif self.flipped_keys[0] %8 == self.flipped_keys[1] %8:
            self.pairs +=1
            self.flipped = 0
            self.flipped_cards.clear()
            self.flipped_keys.clear()
        else:
            self.master.after(1000, self.flipBackAll)
            
    def flipBackAll(self): #sätter vi normal här? for card in self.flipped.cards?
        for card in self.flipped_cards:
            card.turn_back()
        self.flipped = 0
        self.flipped_cards.clear()
        self.flipped_keys.clear()
        
class card:
    def __init__(self,master, row, column):
        """
             Purpose: Creates the buttons and assign pictures to each button.
             Parameters: row - row in game.
                                  column - column in game.
             Returns: - 
             Comment: -
        """        
        self.master = master
        self.row = row
        self.column = column
        self.img = game.img_dict[game.img_keys[4*row+column]]
        self.key = game.img_keys[4*row+column]
        self.back = ImageTk.PhotoImage(Image.open("back.jpg"))
        self.button = Button(self.master, image = self.back, command = lambda: self.flip())
        self.button.grid(row=row, column=column)

    def flip(self):
        """
             Purpose: Flips the card that the user clicked.
             Parameters: -
             Returns: - 
             Comment: -
        """        
        self.button.config(image = self.img, state = DISABLED) #Hur gör vi alla disabled? Och hur gör vi dessa sen normal?
        game.flipped_card(self)
        
    def turn_back(self):
        """
             Purpose: Flip back cards if no match.
             Parameters: -
             Returns: - 
             Comment: -
        """                
        self.button.config(image = self.back, state = NORMAL)
        
root = Tk()
root.geometry("616x616")
game = game(root)
cards = []
for r in range(4):
    for c in range(4):
        cards.append(card(root,r,c))
root.mainloop()
