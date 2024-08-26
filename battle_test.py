import keyboard
from time import sleep
from itertools import cycle as itercycle
from time import time as timenow

BATTLE_SIZE = 10
BATTLE_REFRESH = f"\033[{BATTLE_SIZE + 3}A"

HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"
FPS = 30

icons = {
    " p ":(0,0),
    " e ":(0,1),
}

def sleep_check_keys(sleeptime,keys):
    start = timenow() #Apparently faster than datetime.now()?
    last_pressed = None
    for i in itercycle(keys):
        if keyboard.is_pressed(i):
            last_pressed = i
        if timenow() - start > sleeptime:
            return last_pressed
        
def render_screen(header, footer, icons, default):
    print(header)
    for i in range(0,BATTLE_SIZE):
        for j in range(BATTLE_SIZE):
            flag = True
            for k in icons:
                if icons[k][0] == j and icons[k][1] == i:
                    print(k,end="")
                    flag = False
                    break
            if flag:
                print(default,end="")
        print("")            

    print(footer)
    print(BATTLE_REFRESH)

print(HIDE_CURSOR)

last_pressed_at = -1000
for i in range(0,1_000_000):
    last_pressed = sleep_check_keys(1/FPS,["w","a","s","d"])
    if last_pressed != None and i - last_pressed_at > (FPS/10): #Prevent too fast movement
        last_pressed_at = i
        x,y = icons[" p "]
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
        if last_pressed == "j":
            icons["PRB"] = (x,y)
        elif last_pressed == "k":
            icons["PDB"] = (x,y)
        elif last_pressed == "l":
            icons["PLB"] = (x,y)
        elif last_pressed == "i":
            icons["PUB"] = (x,y)
            
        icons[" p "] = (x,y)

    render_screen(f"BATTLE {last_pressed}", f"SCORE: {i}", icons, " - ")

print(SHOW_CURSOR)
