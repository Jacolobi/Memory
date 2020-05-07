from tkinter import *

class highscore():
    
    hiscore = []
    f = open("highscore.txt")
    lines = f.readlines()
    for line in lines:
        rad = line.strip("\n")
        words = rad.split(' ')
        wee = (words[0],int(words[1]),int(words[2]))
        hiscore.append(wee)
    f.close
    
    def cmp_hi_score(self, newscore):
        self.hiscore.append(newscore)
        index = 0
        for i in range(3):
            if newscore[1] < self.hiscore[index][1]:
                temp = self.hiscore[index]
                self.hiscore.pop(index)
                self.hiscore.append(temp)
            elif newscore[1] == self.hiscore[index][1]:
                if newscore[2] < self.hiscore[index][2]:
                    temp = self.hiscore[index]
                    self.hiscore.pop(index)
                    self.hiscore.append(temp)
            else:
                index += 1
        if newscore != self.hiscore[3]:
            self.hiscore.pop(3)
            return True
        else:
            self.hiscore.pop(3)
            return False
        
    
    def player_name(self, newscore):
        if cmp_hi_score(newscore):
            #Label(top, text = "Skriv ditt namn").place(x,y)
            #name Entry(top).place(x,y)
            temp = list(newscore)
            temp[0] = name
            score = tuple(temp)
            self.hiscore[self.hiscore.index(newscore)] = score
            return score

        
    def print_hi_score(self, newscore):
        #for result in self.hiscore:
            #tkinter Label(top, text = "bla").place(x,y)
        return
    
    def write_hi_score(self):
        f = open("highscore.txt", 'w')
        for result in self.hiscore:
            f.write((result[0] + ' ' + str(result[1]) + ' ' + str(result[2]) + '\n'))
        f.close()
        
test = highscore()
test.cmp_hi_score(('e',3,3))

test.write_hi_score()