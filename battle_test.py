import keyboard
from time import sleep
from itertools import cycle as itercycle
from time import time as timenow

BATTLE_SIZE = 10
BATTLE_REFRESH = f"\033[{BATTLE_SIZE + 3}A"

HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"
FPS = 30

class Board:
    def __init__(self):
        self.icons = [
            [" p ",(0,0)],
            [" e ",(0,1)],
        ]

    def render_screen(self, header, footer, default):
        self.clean()
        print(header)
        for i in range(0,BATTLE_SIZE):
            for j in range(BATTLE_SIZE):
                at_here = default
                for k in self.icons:
                    if k[1][0] == j and k[1][1] == i:
                        at_here = k[0]
                print(at_here,end="")
            print("")            

        print(footer)
        print(BATTLE_REFRESH)
    
    def __getitem__(self,key): #Returns icon data depending on key: int -> location on list; str -> dictionary value
        try:
            int(key)
            return self.icons[key]
        except:
            for i in self.icons:
                if i[0] == key:
                    return i
        return None
    
    def __setitem__(self,key,value):
        try:
            int(key)
            self.icons[key] = value
            return
        except:
            if key[:3] == "new":
                self.icons.append([key[3:],value])
                return

            for i in range(0,len(self.icons)):
                if self.icons[i][0] == key:
                    self.icons[i][1] = value
                    return
        self.icons.append([key, value])

    def __len__(self):
        return len(self.icons)
    
    def append(self,value):
        self.icons.append(value)
    
    def __iter__(self):
        return iter(self.icons)
    
    def clean(self):
        to_remove = []
        for ij in range(0,len(self.icons)):
            try:
                #Checks to see if coords are still well formed
                x,y = self.icons[ij][1]
                int(x)
                int(y)
            except:
                to_remove.append(ij)
        to_remove = sorted(to_remove,reverse=True) #Reverse to avoid index errors
        for i in to_remove:
            self.icons.pop(i) #Pop later to avoid index errors
                
my_board = Board()

def sleep_check_keys(sleeptime,keys):
    start = timenow() #Apparently faster than datetime.now()?
    last_pressed = None
    for i in itercycle(keys):
        if keyboard.is_pressed(i):
            last_pressed = i
        if timenow() - start > sleeptime:
            return last_pressed

print(HIDE_CURSOR)

last_pressed_at = -1000
for i in range(0,1_000_000):
    last_pressed = sleep_check_keys(1/FPS,["w","a","s","d","j","k","l","i"])

    #Input handler
    if last_pressed != None and i - last_pressed_at > (FPS/10): #Prevent too fast movement
        x,y = my_board[" p "][1]
        if last_pressed == "w":
            y -= 1
        elif last_pressed == "a":
            x -= 1
        elif last_pressed == "s":
            y += 1
        elif last_pressed == "d":
            x += 1
        if x >= BATTLE_SIZE:
            x = BATTLE_SIZE - 1
        if y >= BATTLE_SIZE:
            y = BATTLE_SIZE - 1
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        if i - last_pressed_at > (FPS/3):
            if last_pressed == "j":
                my_board["newPRB"] = (x,y)
            elif last_pressed == "k":
                my_board["newPDB"] = (x,y)
            elif last_pressed == "l":
                my_board["newPLB"] = (x,y)
            elif last_pressed == "i":
                my_board["newPUB"] = (x,y)
        
        last_pressed_at = i
        my_board[" p "] = (x,y)


    #Bullet mover
    if i%(FPS//2) == 0: #Every half second
        for j in range(0,len(my_board)):
            if my_board[j][0] in {"PRB","PLB","PDB","PUB"}:
                x,y = my_board[j][1]
                if my_board[j][0] == "PRB":
                    x += 1
                elif my_board[j][0] == "PLB":
                    x -= 1
                elif my_board[j][0] == "PDB":
                    y += 1
                elif my_board[j][0] == "PUB":
                    y -= 1
                if x >= BATTLE_SIZE or x < 0 or y >= BATTLE_SIZE or y < 0:
                    my_board[j] = None #removes bullet in next render
                else:
                    my_board[j][1] = (x,y) #moves bullet
                
            
    my_board.render_screen(f"BATTLE {last_pressed}", f"SCORE: {i}", " - ")

print(SHOW_CURSOR)
