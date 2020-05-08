from tkinter import *
import os
import glob
from PIL import ImageTk, Image
import random
from time import time

class game:
    def __init__(self, master):
        self.master = master
        master.title("Memoory")
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
            for card in self.flipped_cards:
                card.turn_back()
            self.flipped = 0
            self.flipped_cards.clear()
            self.flipped_keys.clear()
        
class card:
    def __init__(self,master, row, column):
        self.master = master
        self.row = row
        self.column = column
        self.img = game.img_dict[game.img_keys[4*row+column]]
        self.key = game.img_keys[4*row+column]
        self.back = ImageTk.PhotoImage(Image.open("back.jpg"))
        self.button = Button(self.master, image = self.back, command = lambda: self.flip())
        self.button.grid(row=row, column=column)

    def flip(self):
        self.button.config(image = self.img, state = DISABLED)
        game.flipped_card(self)
        
    def turn_back(self):
        self.button.config(image = self.back, state = NORMAL)
        
root = Tk()
root.geometry("616x616")
game = game(root)
cards = []
for r in range(4):
    for c in range(4):
        cards.append(card(root,r,c))
root.mainloop()