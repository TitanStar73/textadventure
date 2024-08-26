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
    "p":(0,0),
    "e":(0,1),
}

def sleep_check_keys(sleeptime,keys):
    start = timenow() #Apparently faster than datetime.now()?
    for i in itercycle(keys):
        if keyboard.is_pressed(i):
            return i
        if timenow() - start > sleeptime:
            return None
        
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

for i in range(0,1_000_000):
    last_pressed = sleep_check_keys(1/FPS,["w","a","s","d"])
    render_screen(f"BATTLE {last_pressed}", f"SCORE: {i}", icons, "-")

print(SHOW_CURSOR)
