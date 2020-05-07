import tkinter as tk
from tkinter import *
import cv2
import os
import glob
from tkinter import messagebox
from PIL import ImageTk, Image

class Board:
    def __init__(self, root):
        self.root=root
        self.frame = Frame(root)
        self.frame.pack()
        self.frame.grid()
        self.root.title("Cow Moomery")
        #self.background = PhotoImage(file = "cow1.gif")
        
        background = Image.open("cow1.jpg")

        
        
        #ImageTk.PhotoImage(Image.open("grass.jpg"))  
        #l=Label(image=img)
#l.pack()        

        #self.buttons = [[tk.Button(root, image = bg,
                                   #width=80,
                                   #height=40,
                                   #command=lambda row=row, column=column: self.choose_cards(row, column)
                                  #) for column in range(4)] for row in range(4)]
        #for button in self.buttons:
            #for e in button:
                #e(root, image=background).pack(side=TOP)
          
        
        #for row in range(4):
            #for column in range(4):
                #self.buttons[row][column].grid(row=row, column=column)[(ImageTk.PhotoImage(Image.open("cow1.jpg")) for i in range(10))]
        #backgrounds = list()
        #labels = list()
        #for i in range(16):
            #backgrounds.append(ImageTk.PhotoImage(Image.open("cow1.jpg")))
            #labels.append(Label(self.root, image = backgrounds[i]))
        #for r in range(4):
            #for c in range(4):
                #a = r
                #b = c
                #print(4*a+b)
                #labels[(4*a)+b].grid(row=r,column=c)
                ##ImageTk.PhotoImage(Image.open("cow1.jpg")).grid(row=row,column=column)                
        self.first = None
        #self.draw_board()           

class Cards:
    def __init__(self):
        pairs = 0
        img_folder = "" #mappen som våra bilder ligger i
        data_path= os.path.join(img.folder, "*g")
        files = glob.glob(data_path)
        cow_pics = []
        for image in files:
            img = cv2.imread(image)
            for i in range(1):
                cow_pics.append(img)
            
            
    def place_cards(self):
        self.answer = cow_pics()
        random.shuffle(self.answer)
        self.answer = [self.answer[:4],
                       self.answer[4:8],
                       self.answer[8:12],
                       self.answer[12:]]
        for row in self.buttons:
            for button in row:
                button.config(state=tk.NORMAL)
            


    def choose_cards(self, row, column):
        self.buttons[row][column].config(image=self.answer[row][column])
        self.buttons[row][column].config(state=tk.DISABLED)
        if not self.first:
            self.first = (row, column)
            self.buttons[row][column]
        else:
            a,b = self.first
            #OBS behöver fixa = blockera nya knapptryck innan korten vänts
            if self.answer[row][column] == self.answer[a][b]:
                self.buttons[a][b].config(state=tk.DISABLED)
                self.count_pairs(row, column, a, b)
            else:
                self.parent.after(1000, self.hide_tiles, row, column, a, b)
            self.first = None
    
    
    def hide_cards(self, x1, y1, x2, y2):
        self.buttons[x1][y1].config(state=tk.NORMAL)
        self.buttons[x1][y1].config(image = background ) #OBS!background ligger i annan klass
        self.buttons[x2][y2].config(image = background ) #OBS!background ligger i annan klass


    def count_pairs(self, x1, y1, x2, y2):
        if (self.buttons[x1][y1]) == (self.buttons[x2][y2]):
            pairs += 1
        if pairs == 8:
            messagebox.showinfo("Cow Moomery", "Congratulations You Have Won!")
            

root = tk.Tk()
memory_tile = Board(root)
root.mainloop()
        
    #def place_buttons(self):
        #self.buttons = (Tkinter.Button(memory, image("sarah ansikte"), command=()))
        #for row in range(4):
            #for column in range(4):
                #self.buttons[row][column].grid(row=row, column=column)
        #self.first = None
        #self.draw_board()        
