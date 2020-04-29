import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image

LARGE_FONT= ("Verdana", 12)

class Memory (tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        
        tk.Tk.wm_title(self, "Cow Moomory")
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight= 1)
        container.grid_columnconfigure(0, weight = 1)
        
        img = ImageTk.PhotoImage(Image.open("gra.gif"))  
        l=Label(self, image=img)
        l.pack()        
        
        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save settings", command = lambda: popupmsg("not supported"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label = "File", menu=filemenu)
        
        tk.Tk.config(self,menu=menubar)
        
    
        
        self.frames = {}
        
        for F in (show_menu, new_game, show_highscore):
        
            frame = F (container, self)
            
            self.frames[F] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(show_menu)
        
    def show_frame(self, cont):
        
        frame = self.frames[cont]
                
        frame.tkraise()
        
class show_menu(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Cow Moomory", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
              
        
        button1 = ttk.Button(self, text = "Start New Game",
                            command=lambda: controller.show_frame(new_game))
        button1.pack()
        
        button2 = ttk.Button(self, text = "Highscore",
                            command=lambda: controller.show_frame(show_highscore))
        button2.pack()        

class new_game(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Cow Moomory", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button1 = ttk.Button(self, text = "Back to Home",
                            command=lambda: controller.show_frame(show_menu))
        button1.pack()
        
        button2 = ttk.Button(self, text = "Highscore",
                            command=lambda: controller.show_frame(show_highscore))
        button2.pack()        
        
class show_highscore(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Highscore", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button1 = ttk.Button(self, text = "Back to Menu",
                            command=lambda: controller.show_frame(show_menu))
        button1.pack()
        
 

app = Memory()
app.mainloop()
