from random import choice as randchoice
from time import sleep
#Temporary assets
SLOT_ASSETS = [
r""" .----------------. 
| .--------------. |
| |              | |
| |              | |
| |              | |
| |      $$      | |
| |              | |
| |              | |
| |              | |
| '--------------' |
 '----------------' """,
r""" .----------------. 
| .--------------. |
| |              | |
| |              | |
| |              | |
| |      LL      | |
| |              | |
| |              | |
| |              | |
| '--------------' |
 '----------------' """
]

for item in SLOT_ASSETS:
    if len(item.split('\n')) != len(SLOT_ASSETS[0].split('\n')):
        print("Error: All assets must have the same number of lines.")
        exit()


for i in range(0,15):
    SLOT_ASSETS.append(SLOT_ASSETS[1])

SLOT_1_ROLLS = [SLOT_ASSETS[i] for i in range(0,7)]
SLOT_2_ROLLS = [SLOT_ASSETS[i] for i in range(0,11)]
SLOT_3_ROLLS = [SLOT_ASSETS[i] for i in range(0,13)]
SLOT_WINNING = SLOT_ASSETS[0]
SLOT_REFRESH = f"\033[{len(SLOT_1_ROLLS[0].split('\n'))+1}A" #Move cursor back up to create animation

SLOT_FPS = 30
SLOT_SLEEP = 1/SLOT_FPS
SLOT_ANIMATION_TIME = (1, 6, 0.35) #(time for each slot to be displayed, total slots per slot, transition time)

def special_print(texts):
    total = ""
    dubs = texts[0].split('\n')
    dubs2 = []
    #No idea what causes this bug but it took me ages to debug :(
    for text in dubs:
        if text != '':
            dubs2.append(text)

    for row_no in range(0,len(dubs2)):
        for text in texts:
            total += text.split('\n')[row_no] + " "
        total += "\n"
    print(total[:-1])
    

def get_spliced_asset(a1,a2,ratio): #ratio to ratio + 1 shown, e.g. 0.5 to 1.5
    total = a1 + "\n" + a2
    total = total.split("\n")

    final = ""
    start_line = int(len(a1.split('\n')) * ratio)

    for line_no in range(start_line, start_line + len(a1.split('\n'))):
        final += total[line_no] + "\n"

    return final

def create_roll(a1,a2, previous = []):
    frames_for_roll = int(SLOT_FPS*SLOT_ANIMATION_TIME[2])
    for i in range(0,frames_for_roll-1):
        previous.append(get_spliced_asset(a1,a2,i/frames_for_roll))
        special_print(previous)
        previous.pop()
        sleep(SLOT_SLEEP)
        print(SLOT_REFRESH, flush=True)
    
    previous.append(get_spliced_asset(a1,a2,1))
    special_print(previous)
    sleep(SLOT_SLEEP)
    

def play_slot_machine():
    print("Slot machine!")
    while True:
        try:
            bet = int(input("How much money would you like to bet?: "))
            break
        except:
            print("Please enter a whole number.")

    s1 = SLOT_ASSETS[0] #randchoice(SLOT_1_ROLLS)
    s2 = randchoice(SLOT_2_ROLLS)
    s3 = randchoice(SLOT_3_ROLLS)
    
    a2 = randchoice(SLOT_1_ROLLS)
    for i in range(0, SLOT_ANIMATION_TIME[1]):
        a1 = a2
        a2 = randchoice(SLOT_2_ROLLS)
        create_roll(a1,a2, previous=[])
        print(SLOT_REFRESH, flush=True)

    create_roll(a2,s1, previous=[])
    sleep(SLOT_ANIMATION_TIME[0])
    
    if s1 == s2 == s3 == SLOT_WINNING:
        print(f"Congratulations! You won {bet*1000} gold!")
        return bet*1000

    return -bet


print("s")
print("s")
print("s")
print("s")
print("s")

play_slot_machine()


print("s")
print("s")
print("s")
print("s")
print("s")
print("s")
