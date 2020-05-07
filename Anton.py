from tkinter import *
import cv2
import os
import glob

class Board:
    def __init__(self, root):
        self.frame = Frame(root)
        frame.grid()
        frame.title("Cow Moomery")
        background = ImageTk.PhotoImage(Image.open("cow.jpg"))
        #ImageTk.PhotoImage(Image.open("grass.jpg"))  
        #l=Label(image=img)
        #l.pack()        
        self.buttons = [[tk.Button(root, image = background, width=8, height=4,
                                   command=lambda row=row, column=column: self.choose_tile(row, column)
                                   ) for column in range(4)] for row in range(4)]
        
        for row in range(4):
            for column in range(4):
                self.buttons[row][column].grid(row=row, column=column)
                
        self.first = None
        self.draw_board()           

class Cards:
    def __init__(self):
        self.pairs = 0
        self.img_folder = "" #mappen som våra bilder ligger i
        self.data_path = os.path.join(img.folder, "*g")
        self.files = glob.glob(data_path)
        self.cow_pics = []
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
                button.config(text='', state=tk.NORMAL)
        self.start_time = time.monotonic()    


    def choose_cards(self, row, column):
        self.buttons[row][column].config(image=self.answer[row][column])
        self.buttons[row][column].config(state=tk.DISABLED)
        if not self.first:
            self.first = (row, column)
            self.buttons[row][column] #vad gör denna?
        else:
            a,b = self.first
            #OBS behöver fixa = blockera nya knapptryck innan korten vänts
            if self.answer[row][column] == self.answer[a][b]:
                self.buttons[a][b].config(state=tk.Disabled)
                self.count_pairs(row, column, a, b)
            else:
                self.parent.after(1000, self.hide_cards, row, column, a, b)
            self.first = None
    
    
    def hide_cards(self, x1, y1, x2, y2):
        self.buttons[x1][y1].config(state=tk.NORMAL)
        self.buttons[x1][y1].config(image = background ) #OBS!background ligger i annan klass
        self.buttons[x2][y2].config(image = background ) #OBS!background ligger i annan klass


    def count_pairs(self, x1, y1, x2, y2):
        if (self.buttons[x1][y1]) == (self.buttons[x2][y2]):
            self.pairs += 1
        if self.pairs == 8:
            messagebox.showinfo("Cow Moomery", "Congratulations You Have Won!")
            

root = tk.Tk()
memory_tile = MemoryTile(root)
root.mainloop()
