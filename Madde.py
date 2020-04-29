import tkinter as tk
from PIL import ImageTk, Image
"""Varför funkar inte PhotoImage?"""

class memory(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		container = tk.Frame(self)
		grass_background = ImageTk.PhotoImage(Image.open("Webp.net-gifmaker.gif"))
		background = tk.Label(image=grass_background)
		background.pack()
		container.pack(side="top", fill="both", expand = True)

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		
		self.frames = {}
		
		for frames in (start_menu, new_game, show_highscore):
			frame = frames(container, self)
			self.frames[frames] = frame
			frame.grid(row= 0, column = 0)
			
		self.show_frame(start_menu)
		
		
	def show_frame(self, container):
		frame = self.frames[container]
		frame.tkraise()
		#Hur gömmer vi de andra??


class start_menu(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label_menu = tk.Label(self, text = "Cow Moomory")
		label_menu.pack(pady=10,padx=10)

		button_start_new_game = tk.Button(self, text = "Start New Game", font = "comic_sans_ms 36", command = lambda: controller.show_frame(new_game))
		button_start_new_game.pack()
		"""Lamda har jag för att värdet hos min knapp inte ska referera till något annat efter körning"""
		
		button_show_highscore = tk.Button(self, text = "Show Highscore", font = "comic_sans_ms 36", command = lambda: controller.show_frame(show_highscore))
		button_show_highscore.pack()



class new_game(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
	
		button_go_to_menu = tk.Button(self, text = "Quit and Return to Menu", font = "comic_sans_ms 24", command = lambda: controller.show_frame(start_menu))
		button_go_to_menu.pack(pady=10,padx=10)
		
		button_show_highscore = tk.Button(self, text = "Show Highscore", font = "comic_sans_ms 24", command = lambda: controller.show_frame(show_highscore))
		button_show_highscore.pack()
	
	
class show_highscore(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text = "Highscore")
		label.pack(pady = 10, padx = 10) #placerar ut label på exakt plats
		
		button_go_to_menu = tk.Button(self, text = "Return to Menu", font = "comic_sans_ms 24", command = lambda: controller.show_frame(start_menu))
		button_go_to_menu.pack()
		
memory = memory()
memory.mainloop()
