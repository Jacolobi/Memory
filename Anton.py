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
        self.buttons = [[tk.Button(root, image = background,
                                   width=8,
                                   height=4,
                                   command=lambda row=row, column=column: self.choose_tile(row, column)
                                   ) for column in range(4)] for row in range(4)]
        
        for row in range(4):
            for column in range(4):
                self.buttons[row][column].grid(row=row, column=column)
                
        self.first = None
        self.draw_board()           

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
                button.config(text='', state=tk.NORMAL)
        self.start_time = time.monotonic()    


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
                self.buttons[a][b].config(state=tk.Disabled)
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
            

root = tk.Tk()
memory_tile = MemoryTile(root)
root.mainloop(    )
        
    #def place_buttons(self):
        #self.buttons = (Tkinter.Button(memory, image("sarah ansikte"), command=()))
        #for row in range(4):
            #for column in range(4):
                #self.buttons[row][column].grid(row=row, column=column)
        #self.first = None
        #self.draw_board()        
