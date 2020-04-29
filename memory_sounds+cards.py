from Tkinter import *

class sounds:
    def __init__(self):
        """måste man ha en init?"""
        
    def moo(self):
        spela moo
        
    def bellows(self):
        spela brööl
        
class cards:
    def __init__(self):
        list_cows = [bild1, bild2, ..., bildn]
        self.first = None
        
    def picture(self):
	picture = random.choice(list_cows)
	list_cows.remove(picture)
	return picture
    
    def choose_cards(self):
	self.buttons[relx][rely].config(image = self.answer[relx][rely])
	"""Vi måste komma underfund med hur vi placerar ut korten i class board"""
	if not self.first:
		self.first = (relx, rely)
		self.buttons[relx][rely].config(state=Tk.DISABLED)
	else:
		a, b = self.first
		if self.answer[relx][rely] == self.answer[a][b]:
			self.buttons[a][b].config(state=tk.DISABLED)
			progress_bar.moves()
			progress_bar.pairs()
			sounds.moo()
		else:
			self.parent.after(3000, self.hide_cards, relx, rely, a, b)
			progress_bar.moves()
		self.first = None
		
	def hide_cards(self, x1, y1, x2, y2):
	    self.buttons[x1][y1].config(state=tk.NORMAL) 
	    self.buttons[x1][y1].config(image = "sarahs ansikte")
	    self.buttons[x2][y2].config(image = "sarahs ansikte")
	    
	
    