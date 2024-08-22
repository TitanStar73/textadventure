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

for i in range(0,15):
    SLOT_ASSETS.append(SLOT_ASSETS[1])

SLOT_1_ROLLS = [SLOT_ASSETS[i] for i in range(0,7)]
SLOT_2_ROLLS = [SLOT_ASSETS[i] for i in range(0,11)]
SLOT_3_ROLLS = [SLOT_ASSETS[i] for i in range(0,13)]
SLOT_WINNING = SLOT_ASSETS[0]
SLOT_REFRESH = f"\033[{len(SLOT_1_ROLLS[0].split('\n')) + 1}A" #Move cursor back up to create animation

SLOT_FPS = 30
SLOT_SLEEP = 1/SLOT_FPS
SLOT_ANIMATION_TIME = (0.5, 6, 0.2) #(time for each slot, total slots per slot, transition time)

def special_print(texts):
    for row_no in texts[0].split('\n'):
        for text in texts:
            print(text.split('\n')[row_no], end = ' ')
        print("")
    print("")

def play_slot_machine():
    print("Slot machine!")
    while True:
        try:
            bet = int(input("How much money would you like to bet?: "))
            break
        except:
            print("Please enter a whole number.")

    s1 = randchoice(SLOT_1_ROLLS)
    s2 = randchoice(SLOT_2_ROLLS)
    s3 = randchoice(SLOT_3_ROLLS)

    for i in range(0, SLOT_ANIMATION_TIME[1]):
        print(randchoice(SLOT_1_ROLLS))
        sleep(SLOT_ANIMATION_TIME[0])
        print(SLOT_REFRESH, flush=True)
    
    print(SLOT_1_ROLLS[0])

    if s1 == s2 == s3 == SLOT_WINNING:
        print(f"Congratulations! You won {bet*1000} gold!")
        return bet*1000

    return -bet

play_slot_machine()
