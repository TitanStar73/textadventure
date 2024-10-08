DISABLE_COLORS = False #Turns off colors if enabled
DEFAULT_COLOR = "\033[0m"
RED = DEFAULT_COLOR if DISABLE_COLORS else "\033[31m"
BLUE = DEFAULT_COLOR if DISABLE_COLORS else "\033[34m"
GREEN = DEFAULT_COLOR if DISABLE_COLORS else "\033[32m"
YELLOW = DEFAULT_COLOR if DISABLE_COLORS else "\033[33m"
WHITE = DEFAULT_COLOR if DISABLE_COLORS else "\033[37m"
PURPLE = DEFAULT_COLOR if DISABLE_COLORS else "\033[35m"

import keyboard
from time import sleep
from itertools import cycle as itercycle
from time import time as timenow
from random import randint

BATTLE_SIZE = 10
BATTLE_REFRESH = f"\033[{BATTLE_SIZE + 3}A"

HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"

MOVE_COOLDOWN = 0.25 #In seconds
SHOOT_COOLDOWN = 1.5 #In seconds
BULLET_SPEED = 5
DIFFICULTY_BOSS = 300 #Max is 500
FPS = 30

class Board:
    def __init__(self):
        self.icons = [
            [" p ",(0,0)],
            [" e ",(BATTLE_SIZE-1,1)],
        ]
        self.render_icons = {
            ' p ' : f' {GREEN}@{DEFAULT_COLOR} ',
            ' e ' : f' {RED}#{DEFAULT_COLOR} ',
            'PRB' : f' {GREEN}→{DEFAULT_COLOR} ',
            'PLB' : f' {GREEN}←{DEFAULT_COLOR} ',
            'PDB' : f' {GREEN}↓{DEFAULT_COLOR} ',
            'PUB' : f' {GREEN}↑{DEFAULT_COLOR} ',
            'ERB' : f' {RED}→{DEFAULT_COLOR} ',
            'ELB' : f' {RED}←{DEFAULT_COLOR} ',
            'EDB' : f' {RED}↓{DEFAULT_COLOR} ',
            'EUB' : f' {RED}↑{DEFAULT_COLOR} ',
            'ERM' : f' {RED}⇒{DEFAULT_COLOR} ',
            'ELM' : f' {RED}⇐{DEFAULT_COLOR} ',
            'EDM' : f' {RED}⇓{DEFAULT_COLOR} ',
            'EUM' : f' {RED}⇑{DEFAULT_COLOR} ',
        }

    def render_screen(self, header, footer, default):
        self.clean()
        print(header)
        for i in range(0,BATTLE_SIZE):
            for j in range(BATTLE_SIZE):
                at_here = default
                for k in self.icons:
                    if k[1][0] == j and k[1][1] == i:
                        if k[0] in self.render_icons:
                            at_here = self.render_icons[k[0]]
                        else:
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

def upload_banner(text, i):
    global banner
    if len(banner) <= len(text):
        banner = text
    else:
        banner = text + (' ' * (len(banner) - len(text)))
    global banner_showed_at
    banner_showed_at = i


last_moved_at = -1000
last_shot_at = -1000
banner_showed_at = -1000
banner = ""

boss_health = 100
player_health = 5

boss_moving_up = True

for key in ["w","a","s","d","j","k","l","i"]:
    keyboard.block_key(key)

print(HIDE_CURSOR)

for i in range(0,1_000_000):
    last_pressed = sleep_check_keys(1/FPS,["w","a","s","d","j","k","l","i"])

    #Movement handler
    if last_pressed in {"w","a","s","d"} and i - last_moved_at > (FPS*MOVE_COOLDOWN): #Prevent too fast movement
        x,y = my_board[" p "][1]
        if last_pressed == "w":
            y -= 1
        elif last_pressed == "a":
            x -= 1
        elif last_pressed == "s":
            y += 1
        elif last_pressed == "d":
            x += 1
        if x >= BATTLE_SIZE - 2: #Limit player movement to 2 blocks from the right
            x = BATTLE_SIZE - 3
        if y >= BATTLE_SIZE:
            y = BATTLE_SIZE - 1
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        
        last_moved_at = i
        my_board[" p "] = (x,y)

    #Shoot handler
    if last_pressed in {"j","k","l","i"} and i - last_shot_at > (FPS*SHOOT_COOLDOWN): #Prevent too fast shooting
        x,y = my_board[" p "][1]
        if last_pressed == "l":
            my_board["newPRB"] = (x,y)
        elif last_pressed == "k":
            my_board["newPDB"] = (x,y)
        elif last_pressed == "j":
            my_board["newPLB"] = (x,y)
        elif last_pressed == "i":
            my_board["newPUB"] = (x,y)
        last_shot_at = i


    #Bullet mover
    if i%(FPS//BULLET_SPEED) == 0: #Every half second
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
    
    #Enemy bullet mover, moves 1 frame later, to prevent bullets from "phasing" through each other
    if i%(FPS//BULLET_SPEED) == 1: #Every half second
        for j in range(0,len(my_board)):
            if my_board[j][0] in {"ERB","ELB","EDB","EUB", "ERM","ELM","EDM","EUM"}:
                x,y = my_board[j][1]
                if my_board[j][0][1] == "R":
                    x += 1
                elif my_board[j][0][1] == "L":
                    x -= 1
                elif my_board[j][0][1] == "D":
                    y += 1
                elif my_board[j][0][1] == "U":
                    y -= 1
                if x >= BATTLE_SIZE or x < 0 or y >= BATTLE_SIZE or y < 0:
                    my_board[j][1] = None #removes bullet in next render
                else:
                    my_board[j][1] = (x,y) #moves bullet
    
    my_board.clean()

    #Detect bullet collisions
    already_exits = []
    collisions = []
    for j in range(0,len(my_board)):
        if my_board[j][0] in {"ERB","ELB","EDB","EUB","PRB","PLB","PDB","PUB", "ERM","ELM","EDM","EUM"}:
            x,y = my_board[j][1]
            if (x,y) in already_exits:
                collisions.append((x,y))
            else:
                already_exits.append((x,y))
    for j in range(0,len(my_board)):
        if my_board[j][0] in {"ERB","ELB","EDB","EUB","PRB","PLB","PDB","PUB"}: #Missile immune from being destoryed
            x,y = my_board[j][1]
            if (x,y) in collisions:
                my_board[j][1] = None

    #Shoot enemy bullets
    if boss_health < 50:
        difficulty_multiplier = 2
    elif boss_health < 75:
        difficulty_multiplier = 1.5
    else:
        difficulty_multiplier = 1

    my_board.clean()
    if i%int((FPS*100)/(DIFFICULTY_BOSS * difficulty_multiplier)) == 0:
        if randint(0,1000) < DIFFICULTY_BOSS:
            for j in range(0,len(my_board)):
                if my_board[j][0] == " e ":
                    x,y = my_board[j][1]
                    bullet_type = ""
                    if boss_health > 50:
                        if randint(1,4) == 2:
                            bullet_type = "M" #Missile
                        else:
                            bullet_type = "B"
                    else: #Always shoot missiles after <50% health
                        bullet_type = "M"

                    my_board.append([f"EL{bullet_type}",(x,randint(0,BATTLE_SIZE-1))])
                    
                    
    #Check if player got hit
    my_board.clean()
    for j in range(0,len(my_board)):
        if my_board[j][0] in {"ERB","ELB","EDB","EUB", "ERM","ELM","EDM","EUM"}:
            x,y = my_board[j][1]
            if my_board[" p "][1] == (x,y):
                if my_board[j][0][2] == "B":
                    player_health -= 1
                elif my_board[j][0][2] == "M":
                    player_health -= 3
                my_board[j][1] = None

    my_board.clean()
    #Check if player hit enemy
    for j in range(0,len(my_board)):
        if my_board[j][0] in {"PRB","PLB","PDB","PUB"}:
            x,y = my_board[j][1]
            if my_board[" e "][1] == (x,y):
                my_board[j][1] = None
                if randint(1,20) == 2: #5% chance of crit
                    boss_health -= 20
                    upload_banner("CRIT! ", i)
                elif randint(1,4) == 2: #25% chance after that to be blocked
                    upload_banner("BLOCKED! ", i)
                else:
                    boss_health -= randint(5,9) #Normal hit

    if i%int((FPS*100)/(DIFFICULTY_BOSS*difficulty_multiplier)) == 2:
        x,y = my_board[" e "][1]
        if boss_moving_up:
            y -= 1
        else:
            y += 1
        if y >= BATTLE_SIZE:
            boss_moving_up = True
            y = BATTLE_SIZE - 1
        if y < 0:
            boss_moving_up = False
            y = 0

        my_board[" e "] = (x,y)

    if i == 300:
        upload_banner("CRIT! ", i)

    if boss_health < 0:
        boss_health = 0
    if player_health < 0:
        player_health = 0

    shot_charged = min(100, round(((i - last_shot_at)/(FPS*SHOOT_COOLDOWN))*100))
    shot_charged_color = GREEN if shot_charged == 100 else (RED if shot_charged < 75 else YELLOW)
    banner_data = " " * (len(banner) + 5) if i - banner_showed_at > (FPS*2.5) else ' | ' + banner

    my_board.render_screen(f"{PURPLE}BOSS HEALTH: {boss_health}{DEFAULT_COLOR}{banner_data}", f"YOUR HEALTH: {RED}{player_health * '♥'}{DEFAULT_COLOR}{' ' * (5-player_health)}  |  Shot charged up: {shot_charged_color}{' '*(3-len(str(shot_charged)))}{shot_charged}%{DEFAULT_COLOR}", " - ")

    if player_health == 0:
        print("\n" * (BATTLE_SIZE + 4))
        print("YOU DIED!")
        break

    if boss_health == 0:
        print("\n" * (BATTLE_SIZE + 4))
        print("YOU WON!")
        break

print(SHOW_CURSOR)

for key in ["w","a","s","d","j","k","l","i"]:
    keyboard.unblock_key(key)
