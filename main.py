"""
Code by Arush Mundada

Disclaimer:
Some stuff was generated by AI, those parts have #AI Generated Start and #AI Generated End before and after them

Users will be given the option to provide an OpenAI API key to create a more imersive experience (optional always)
"""

print("""
Welcome to the Text Based Adventure!

Some tips:
Come back every once in a while to see if there are any new updates!
Enter quit to exit the game.
Enter save to save your progress in the game to a file (you will need to enter a filename).
Enter autosave to automatically save the game whenever possible.

Nothing is as it seems, nothing is fixed, everything is a choice. Choose wisely.
      
If you see a "..." click enter to continue
      
Try it out...""")

input()
print("Great! Let's get started!")

from random import choice as randchoice
from time import sleep
import os.path

WPM = 500 #Words per minute for the text animation, 1 word = 6 characters including spaces and special characters, neglecting time for print statement
DISABLE_ANIMATION = False #Turns off text animation

#Optional will not change gameplay descisons only provides a more immersive dialogue
#If not provided make it None

OPENAI_API_KEY = None 

DEBUG_ALLOWED = False #Turns on debug mode | PROCEED WITH CAUTION, ARBITARY PYTHON CODE CAN BE EXECUTED


if OPENAI_API_KEY != None:
    import openai

    def get_openai_response(prompt):
        response = openai.Completion.create(
            engine="gpt4",
            prompt=prompt,
            max_tokens=300
        )
        return response.choices[0].text.strip()

else:
    def get_openai_response(prompt):
        return "Roses are red, Violets are blue, to get a better response, provide an OpenAI API key too!"


def char_animation(msg, end = "\n"):
    for char in msg:
        print(char, end = "", flush = True)
        sleep(10/WPM)
    print(end, end = "")

def char_animation_in(msg):
    char_animation(msg, end = "")
    return input()

if DISABLE_ANIMATION:
    char_animation = print
    char_animation_in = input

def get_char_animation_in(msg,accepted, allow_save = False,err_msg = ""): #{'choice1':['choice1','alias1','alias2'],'choice2':['choice2','alias1','alias2']}
    while True:
        choice = char_animation_in(msg).lower()
        if choice == 'autosave':
            autosave = not autosave
            char_animation(f"Autosave is now {'on' if autosave else 'off'}. Enter autosave again to toggle.")
            continue
        if choice == 'quit':
            a = char_animation_in("Are you sure? If you haven't saved your progress, you will lose it. Press enter to confirm, or anything else to cancel. You can enter 'save' to save")
            if a == '':
                exit()
        elif choice == 'save' or (autosave and allow_save):
            if not allow_save:
                char_animation("You can't save right now :(\nPlease wait till you are prompted which place to go next!")
                continue
            if autosave:
                filename = "game.data"
            else:
                filename = char_animation_in("Enter a filename: ")
            with open(filename, 'w') as f:
                f.write(f"{situtation}\n{NAME}\n{been_in_situations}\n{morailty}\n{person_type}\n{career}\n{previous_choices}\n{gold}\n{inventory}\n{autosave}")

        for key in accepted:
            if choice in [item.lower() for item in accepted[key]]:
                return key
        char_animation(err_msg, end = "")

def get_karma(thing):
    try:
        return previous_choices[thing]
    except KeyError:
        return 0

def parse_dict(dictt):
    dictt = [item for item in dictt.strip('{}').split(',') if item != ""] #{'key1':'value1','key2':'value2'} -> ["'key1':'value1'"","'key2':'value2'"]
    new_dict = {}
    for item in dictt:
        key, value = item.split(':') #key = "'key1'", value = "'value1'"
        key = key.strip()
        value = value.strip()
        try:
            key = int(key) #Try int
        except ValueError:
            try:
                key = float(key) #Try float
            except ValueError:
                key = key[1:-1] #Remove quotes

        try:
            value = int(value) #Try int
        except ValueError:
            try:
                value = float(value) #Try float
            except ValueError:
                value = value[1:-1] #Remove quotes

        new_dict[key] = value
    return new_dict


situtation = 0
been_in_situations = set()
morailty = 0
NAME = "person"
person_type = 0
career = 'None'
previous_choices = {}
gold = 0
inventory = set()
autosave = False
#Constants
WIZARD = "Wizard"
WARRIOR = "Warrior"
VILLIAN = "Villian"
WARLOCK = "Warlock"
GHOST = "Ghost"

#AI GENERATED START
RIDDLES = {
    'What has keys but can’t open locks?': {'piano', 'keyboard'},
    'What has to be broken before you can use it?': {'egg'},
    'I’m tall when I’m young, and I’m short when I’m old. What am I?': {'candle'},
    'What is full of holes but still holds water?': {'sponge'},
    'What gets wet while drying?': {'towel'},
    'What can you catch, but not throw?': {'cold'},
    'What goes up but never comes down?': {'age'},
    'I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?': {'echo'},
    'What has a head, a tail, is brown, and has no legs?': {'penny'},
    'What runs all around a backyard, yet never moves?': {'fence'}
}
#AI GENERATED END


while True:
    if career == None: #Standard Careers (not including ghost)
        if abs(morailty) >= 5 and abs(person_type) >= 5:
            if morailty >= 5 and person_type >= 5:
                career = WIZARD
            elif morailty >= 5 and person_type <= -5:
                career = WARRIOR
            elif morailty <= -5 and person_type >= 5:
                career = VILLIAN
            elif morailty <= -5 and person_type <= -5:
                career = WARLOCK

    if situtation == 0:
        char_animation("Welcome Adventurer!")
        char_animation("1) Start a new game")
        char_animation("2) Load a game")

        if os.path.exists("game.data"):
            char_animation("3) Continue from save detected in game.data")
            choice = get_char_animation_in("Enter your choice: ",{'a':['1','start','new'],'b':['2','load'],'c':['3','game']}, "")
        else:
            choice = get_char_animation_in("Enter your choice: ",{'a':['1','start','new'],'b':['2','load']}, "")

        if choice == 'a':
            situtation = 1
        elif choice == 'b' or choice == 'c':
            if choice == 'b':
                filename = char_animation_in("Enter a filename: ")
            else:
                filename = "game.data"
            with open(filename) as file:
                save_data = file.read().split('\n')
                situtation = int(save_data[0])
                NAME = save_data[1]
                been_in_situations = {int(item) for item in save_data[2].strip('{}').split(',')}
                morailty = int(save_data[3])
                person_type = int(save_data[4])
                career = save_data[5]
                previous_choices = parse_dict(save_data[6]) #Fix change to properly parse dictionary
                gold = int(save_data[7])
                inventory = {int(item) for item in save_data[8].strip('{}').split(',')}
                autosave = save_data[9] == 'True'
        situtation = 1
    
    elif situtation == 1: #Clearing
        if 1 not in been_in_situations:
            char_animation("You wake up in the clearing of a forest, not remembering how you got here. You don't remember anything or anyone. The only thing you remember is a single word: your name.")
            NAME = char_animation_in("What is it?: ")
            been_in_situations.add(1)
        char_animation(f"Hello {NAME}. You see 4 paths labeled with signs: ")

        char_animation("\n\n")
        char_animation("1. The path going to the Temple, it has a a bricked road with lamps on the side.")
        char_animation("2. The path going to the Library, it has a road covered with leaves, seemingly not being disturbed in years.")
        char_animation("3. The path to the Arena, it has a road with a lot of footchar_animations, and you can hear the sound of swords clashing from the distance.")                    
        char_animation("4 The path to the Dragon's lair, the sign itself tangled with vines and the path so overgrown it may as well not have been there.")
        choice = get_char_animation_in("Which path do you take?: ",{'2':['1','temple'],'3':['2','library'],'4':['3','arena'],'5':['4',"dragon","lair"]}, allow_save=True)
        situtation = int(choice)

    elif situtation == 2: #Temple
        char_animation("\n\nTemple")
        if 2 not in been_in_situations:
            char_animation("As you walk down this path you see another person walking down the path. Do you?: ")
            char_animation("1. Ask him for help")
            char_animation("2. Ignore him")
            char_animation("3. Attack him")
            choice = get_char_animation_in("Enter your choice: ",{'a':['1','ask','help'],'b':['2','ignore'],'c':['3','attack']})
            if choice == 'a':
                previous_choices["old man"] = 1
                person_type += 1
                morailty += 1
                char_animation("You ask him for help, and he says: ")
                char_animation("What do you mean you don't know where you are?! You are in the kingdom of Mythopes, ruled by Emporer Rahas! Child you look like you need help, I am old I don't have much but you can have this: he hands you a bag of gold")
                if career == GHOST:
                    char_animation("You are a ghost, you can't hold the gold :(")
                else:
                    char_animation("You take the gold and thank him + 100 Gold")
                    gold += 100
            elif choice == 'b':
                previous_choices["old man"] = 0
                person_type -= 1
                if career != GHOST:
                    char_animation("You ignore him and continue down the path... On your way there you see a bag of gold on the side of the path, you could've sworn it wasn't there a moment ago, +100 Gold")
                    gold += 100
            elif choice == 'c':
                previous_choices["old man"] = -1
                person_type -= 1
                morailty -= 10000
                if career == GHOST:
                    char_animation("You attack him but float right through him lol.")
                else:
                    char_animation("You attack him and quickly overpower him. +100 Gold")
                    gold += 100

            if career != GHOST:
                char_animation("You continue down the path and you see a temple, and you enter it. There are a few people inside who seem to put money into the temple's donation box. Do you: ")
                char_animation("1. Put some money in the donation box")
                char_animation("2. Ignore the donation box")
                choice = get_char_animation_in("Enter your choice: ",{'a':['1','put','money'],'b':['2','ignore']})
                if choice == 'a':
                    amt = int(char_animation_in("How much money do you put in the donation box?: "))
                    previous_choices["donation"] = amt
                    gold -= amt
                    if amt > 0:
                        char_animation(f"You put the {amt} money in the donation box")
                    if gold < 0:
                        char_animation("You are now in debt but you feel good :)")
                        morailty += 1000
                    if amt > 50:
                        morailty += 2
                    if amt > 80:
                        morailty += 1
                    if morailty == 100:
                        morailty += 2
                    if amt < 0:
                        char_animation(f"You take the {amt} money from the donation box", end="")
                        char_animation(f".{' '*150}.{' '*150}.{' '*150}\nYou suddenly feel a sharp pain in you head. You hear a nasty voice in your head 'hahaha you think you can fool me!!'")
                        char_animation(f"Do you wish to explain yourself? (yes/no)")
                        choice = get_char_animation_in("Enter your choice: ",{'a':['1','yes','explain', 'y'],'b':['2','no','ignore', 'n']})
                        if choice == 'a':
                            the_explanation = char_animation_in("[Explain youself]: ").lower()
                            if 'sorry' in the_explanation:
                                the_explanation = the_explanation.split('sorry')
                                the_explanation = the_explanation[0].split('not')
                                if len(the_explanation)%2 == 0:
                                    char_animation("Intersting explanation, *not* an apology though.")
                                else:
                                    char_animation("You explain yourself... ")
                                    char_animation("The voice in your head says 'I will let you go this time... if you solve my riddle'")
                                    riddle = randchoice(list(RIDDLES.keys()))
                                    char_animation("    " + riddle)
                                    ans = char_animation_in("Answer: ").lower()
                                    if ans in RIDDLES[riddle]:
                                        char_animation("You are correct... surprising for a mortal... to bad you still have to go")
                                    else:
                                        char_animation("You're wrong... bye!")
                            else:
                                char_animation("You don't even say sorry... some apology!")
                        char_animation("The sharp pain in your head multiplies hundred fold and you die... no worse... you are neither here nor there, you are a ghost.")
                        career = GHOST
                if choice == 'b' or amt == 0:
                    previous_choices["donation"] = 0
                    char_animation("You ignore the donation box and continue down the path...")
                
                if choice == 'a' and amt > 0:
                    char_animation("PROVIDE INFO 1") #To be added Info 1
            else:
                char_animation("You enter the temple and you feel a deep chill... You feel a similar dark presence.")
                char_animation("A familiar voice says: ")
                char_animation("PROVIDE INFO 1")

            been_in_situations.add(2)

        char_animation("Where do you chose to go?")
        char_animation("1. Back to the clearing")
        char_animation("2. Go to the town")
        choice = get_char_animation_in("Enter your choice: ",{'a':['1','back'],'b':['2','town']}, allow_save=True)
        if choice == 'a':
            situtation = 1
        elif choice == 'b':
            situtation = 10
        
    elif situtation == 3: #Library
        if 3 not in been_in_situations:
            char_animation("\n\nLibrary")
            char_animation("You walk down the path for what seems like ages. You finally reach the library.")
            char_animation("Its a grand structurem, so tall you cant see the top. It so huge you cant see where it ends.")
            char_animation("Yet it appears abandoned, the building is covered in vines.")
            char_animation("You enter the library and see huge lines of bookshelves filled with thousands of dusty books.")
            
            lib_loc = 0
            char_animation("You continue foraward and see two paths, one up a ladder and one down steep stairs.")
            char_animation("Do you: ")
            char_animation("1. Go up the ladder")
            char_animation("2. Go down the stairs")
            choice = get_char_animation_in("Enter your choice: ",{'1':['1','up','ladder'],'-1':['2','down','stairs']},allow_save=True)
            lib_loc += int(choice)
            
            char_animation("You continue foraward and see two more paths, one up a spiral staircase and one down a trapdoor.")
            char_animation("Do you: ")
            char_animation("1. Go up the stairs")
            char_animation("2. Go down the trapdoor")
            choice = get_char_animation_in("Enter your choice: ",{'1':['1','up','stairs'],'-1':['2','down','trapdoor']})
            lib_loc += int(choice)
            if choice == '1':
                person_type += 1
            else:
                person_type -= 1
            
            char_animation("You continue foraward and see two more paths, left towards a large shelf of boooks, same yet different from what you've seen so far or right towards a set of glowing spheres on the bookshelves.")
            char_animation("Do you: ")
            char_animation("1. Go left towards a large shelf of boooks")
            char_animation("2. Go right towards a set of glowing spheres on the bookshelves")
            choice = get_char_animation_in("Enter your choice: ",{'1':['1','left'],'-1':['2','right']})
            if OPENAI_API_KEY != None and choice == '1':
                char_animation("You see open a book and it reads: ")
                char_animation(get_openai_response("Give a short story about an ancient library. Only provide the story do not say anything else."))
            if OPENAI_API_KEY != None and choice == '2':
                char_animation("You see a glowing sphere and you touch it, you see a vision of a great library, the biggest you have ever seen. Inside of it you see you. You hear a voice: ")
                char_animation(get_openai_response("Provide a prophecy of the player doing great things. Only provide the prophecy do not say anything else."))            

            lib_loc += int(choice)
            if choice == '1':
                person_type -= 1
            else:
                person_type += 2


            char_animation("You continue foraward and see two more paths, each with a huge archway and a single word on the top.")
            char_animation("Do you: ")
            char_animation("1. Go left towards the archway with the word 'Power' on the top")
            char_animation("2. Go right towards the archway with the word 'Knowledge' on the top")
            choice = get_char_animation_in("Enter your choice: ",{'1':['1','left'],'-1':['2','right']})
            lib_loc += int(choice)
            if choice == '1':
                morailty -= 2
            if choice == '2':
                morailty += 1
                person_type += 1

            lib_loc //= 2
            
            if lib_loc == 0:
                choice = char_animation_in("Now what?: ")
                if choice == 'BA':
                    char_animation(f".{' '*150}.{' '*150}.{' '*150}\nYou have broken out of the matrix... Just kidding but you can chose either path: ")
                    char_animation("1. Meet the librarian")
                    char_animation("2. Meet the priest")
                    choice = get_char_animation_in("Enter your choice: ",{'a':['1','librarian'],'b':['2','priest']})
                    if choice == 'a':
                        lib_loc = 1
                    elif choice == 'b':
                        person_type += 1
                        lib_loc = -1
                    char_animation("Great choice, also heres +100 Gold for being smart :)")
                else:
                    char_animation(":(")
                    lib_loc = randchoice([-1,1])

            if lib_loc < 0:
                char_animation("You continue down the path and you see a priest, he looks at you with eyes that seem thousands of years old yet like those of a newborn.")
                char_animation(f"He looks at you mysteriously and says: 'Better {' '*150}elsewhere {' '*150}you {' '*150}will {' '*150}do!'")
                char_animation("You feel a tug in your gut and you feel your entire body being compressed into a tiny ball.")
                char_animation("You wake up and are now in...") #Arena
                situtation = 4
                been_in_situations.add(3)
                continue
            if lib_loc > 0:
                char_animation("You see a librarian, who looks as old as time itself. She looks at you and says: ")
                char_animation("Its been a long time since I've seen a mortal here... You must be special.")
                char_animation("INFO 1") #To be added info 1
            
            been_in_situations.add(3)
        
        char_animation("Where do you chose to go?")
        char_animation("1. Back to the clearing")
        char_animation("2. Go to the town")
        choice = get_char_animation_in("Enter your choice: ",{'a':['1','back'],'b':['2','town']}, allow_save=True)
        if choice == 'a':
            situtation = 1
        elif choice == 'b':
            situtation = 10

    elif situtation == 4: #Arena entrance
        char_animation("\n\nThe Arena")
        if 4 not in been_in_situations:
            char_animation("You walk down the path and enter a large clearing")
            char_animation("The largest building you have ever seen is in front of you.")
            char_animation("It is a massive colosseum made of chisled white marble.")
            char_animation("Yet on looking closer it seems to be in ruins, with cracks all over and vines appearing to grow over it")
            char_animation("You enter the colosseum and see a large arena, with no one in the stands.")
            
            if gold > 0 and career != GHOST:
                char_animation("As you walk in you see a shopkeeper, he looks at you and says would you like to purchase something: ")
                char_animation("1. Buy a sword (66 gold)")
                char_animation("2. Buy a potion (50 gold)")
                char_animation("3. Buy food (50 gold)")
                char_animation("4. Ignore him and move on")
                choice = get_char_animation_in("Enter your choice: ",{'a':['1','sword'],'b':['2','potion'],'c':['3','food'],'d':['4','ignore']})
                if choice == 'a':
                    if gold >= 66:
                        gold -= 66
                        inventory.add("sword")
                        char_animation("You buy a sword")
                        person_type -= 1
                    else:
                        char_animation("You don't have enough gold. The shopkeeper is annoyed and you move forward.")
                elif choice == 'b':
                    if gold >= 50:
                        gold -= 50
                        inventory.add("potion")
                        char_animation("You buy a potion")
                        person_type += 1
                    else:
                        char_animation("You don't have enough gold. The shopkeeper is annoyed and you move forward.")
                elif choice == 'c':
                    if gold >= 50:
                        gold -= 50
                        inventory.add("food")
                        char_animation("You buy food")
                    else:
                        char_animation("You don't have enough gold. The shopkeeper is annoyed and you move forward.")
                elif choice == 'd':
                    char_animation("You ignore the shopkeeper and move forward.")
                
                if 'food' in inventory:
                    char_animation("You continue down the path and you see a beggar who asks you for some alms. Do you:")
                    char_animation("1. Give him all your food")
                    char_animation("2. Give him some food")
                    char_animation("3. Ignore him")
                    choice = get_char_animation_in("Enter your choice: ",{'a':['1','all'],'b':['2','some'],'c':['3','ignore']})
                    if choice == 'a':
                        inventory.remove('food')
                        char_animation("You give him all your food")
                        morailty += 3
                        previous_choices['beggar_arena'] = 2
                    elif choice == 'b':
                        char_animation("You give him some food")
                        previous_choices['beggar_arena'] = 1
                        morailty += 1
                    elif choice == 'c':
                        char_animation("You ignore him")
                        morailty -= 1
                
                else:
                    char_animation("You continue down the path and you see a beggar who asks you for some alms. Do you:")
                    char_animation("1. Give him all your gold")
                    char_animation(f"2. Give him some gold {min(10,gold//3)}")
                    char_animation("3. Ignore him")
                    choice = get_char_animation_in("Enter your choice: ",{'a':['1','all'],'b':['2','some'],'c':['3','ignore']})
                    
                    if choice == 'a':
                        gold = 0
                        char_animation("You give him all your gold")
                        previous_choices['beggar_arena'] = 2
                        morailty += 3
                    elif choice == 'b':
                        gold -= min(10,gold//3)
                        char_animation("You give him some gold")
                        previous_choices['beggar_arena'] = 1
                        morailty += 1
                    elif choice == 'c':
                        char_animation("You ignore him")
                        morailty -= 1

                if choice == 'a' or choice == 'b':
                    char_animation("The beggar says: ")
                    char_animation("Remember in life,")
                    char_animation("In chaos you'll find peace,")
                    char_animation("Neither charging forth nor seeking release,")
                    char_animation("With no steps forward nor backward, you'll conquer the storm.")
                    char_animation("and you'll find out you were wrong all along.")

            elif career == GHOST:
                char_animation("An apparation appears and says: ")
                char_animation("Remember in life,")
                char_animation("In chaos you'll find peace,")
                char_animation("Neither charging forth nor seeking release,")
                char_animation("With no steps forward nor backward, you'll conquer the storm.")
                char_animation("and you'll find out you were wrong all along.")
                char_animation("Before you can say anything else it dissapears.")

            else:
                char_animation("You feel a deep sense that you would be better off coming back later...")
                char_animation("Do you: ")
                char_animation("1. Go back to the clearing")
                char_animation("2. Continue forward")
                choice = get_char_animation_in("Enter your choice: ",{'a':['1','back'],'b':['2','forward']})
                if choice == 'a':
                    situtation = 1
                    continue
                elif choice == 'b':
                    char_animation("You continue forward")
            
            been_in_situations.add(4)
        
        situtation = 12
    
    elif situtation == 12: #Arena
        if 12 not in been_in_situations:
            char_animation("You walk into the arena and see it in its glory. ")
            char_animation("You can almost see the warriors fighting in the arena, the crowd cheering.")
            char_animation("And then you see a large man, 7ft tall, 300 pounds of pure muscle, barelling at you.")
            char_animation("Do you: ")
            char_animation("1. Stay and fight him")
            char_animation("2. Run away")
            choice = get_char_animation_in("Enter your choice: ",{'a':['1','fight'],'b':['2','run'],'c':['stay','still','none','nothing','peace']})
            if choice == 'a':
                char_animation("You stay and fight him...")
                person_type -= 2
                if 'potion' in inventory:
                    char_animation("You accidently throw your potion at him and he dissapears in a poof of smoke...")
                elif 'sword' in inventory and get_karma('beggar_arena') in {1,2}:
                    char_animation("You fight him with your sword and you win.")
                else:
                    char_animation("You fight him but he is too strong and you die. Better luck next time...")
                    char_animation("Game over.... not yet...")
                    char_animation_in("You can go back a step if you would like... Press enter to go back...")
                    input()
                    situtation = 12
                    continue

            elif choice == 'b':
                char_animation("You run away as fast as you can, as strong as he looks you are faster.")
                char_animation("You run and run until you reach the clearing.")
                person_type += 1
                situtation = 1
                continue
            
            elif choice == 'c':
                char_animation("You stay still and do nothing... He continues running forward... You still do nothing, you stay still...")
                char_animation("You remember the beggar's words...")
                char_animation("In chaose you'll find peace... Neither charging forth nor seeking release... With no steps forward nor backward, you'll conquer the storm.")
                char_animation("He is still running at you....")
                char_animation("And he runs right at you and stops... He looks at you and says: ")
                char_animation("You are the first one who hasn't run away or fought me...")
                char_animation("Intriguing...")
                char_animation("Most find my appearance terrifying... I am the guardian of the arena... I am here to test you and all who come for all of enternity.")
                char_animation("You have passed the test...")
                previous_choices['fighter_arena'] = 1

            been_in_situations.add(12)
            
        char_animation_in("Where would you like to go?: ")
        char_animation("1. Back to the clearing")
        char_animation("2. Go to the town")
        if get_karma('fighter_arena') == 1:
            char_animation("3. Go to the warrior's base")
            choice = get_char_animation_in("Enter your choice: ",{'a':['1','back'],'b':['2','town'],'c':['3','warrior','base']}, allow_save=True)
        else:
            choice = get_char_animation_in("Enter your choice: ",{'a':['1','back'],'b':['2','town']}, allow_save=True)

        if choice == 'a':
            situtation = 1
        elif choice == 'b':
            situtation = 10
        elif choice == 'c':
            situtation = 11

    elif situtation == 5: #Dragon's Lair path 1
        person_type -= 1
        char_animation("You go down the dragon lair path, and you see bones scattered along the path. Do you: ")
        char_animation("1. Continue down the path")
        char_animation("2. Go back")
        choice = get_char_animation_in("Enter your choice: ",{'a':['1','continue'],'b':['2','back']}, allow_save=True)
        if choice == 'a':
            situtation = 6
        elif choice == 'b':
            situtation = 1
    
    elif situtation == 6: #Dragon's Lair path 2
        person_type -= 1
        char_animation("You continue down the path, and you see a dead body of a knight, possibly just a few days old, Do you: ")
        char_animation("1. Continue down the path")
        char_animation("2. Go back")
        choice = get_char_animation_in("Enter your choice: ",{'a':['1','continue'],'b':['2','back']}, allow_save=True)
        if choice == 'a':
            situtation = 7
        elif choice == 'b':
            situtation = 1
    
    elif situtation == 7: #Dragon's Lair
        person_type -= 1
        char_animation("You see a large cavern, nothing but darkness ahead. You hear a deep growling sound. Do you: ")
        char_animation("1. Go back")
        char_animation("2. Continue")
        choice = get_char_animation_in("Enter your choice: ",{'a':['1','back'],'b':['2','continue']}, allow_save=True)
        if choice == 'a':
            situtation = 1
        elif choice == 'b':
            situtation = 8
    
    elif situtation == 8: #Dragon's Lair
        if 8 in been_in_situations:
            char_animation("You have already been here before... You are too scared to go back in.")
            situtation = 1
            continue
        been_in_situations.add(8)
        char_animation("\n\nDragon's Lair")
        
        char_animation("In the center of the cavern, you can barely see a shadowy figure. You slowly approach it and it moves with deadly speed. In the blink of an eye the way you came in is blocked by rocks.")
        char_animation("In the most petrifying voice you here it speak... Wait its speaking not to you but in you... You can hear its voice in your head.")
        char_animation("It voice loathes of pure evil and it speaks to you.")
        char_animation("\"You can only leave if you answer my riddle correctly.\"")
        riddle = randchoice(list(RIDDLES.keys()))
        char_animation("")
        char_animation("    " + riddle)
        ans = char_animation_in("Answer: ").lower()
        if ans in RIDDLES[riddle]:
            char_animation("The dragon lets out a laugh, yesss you have answer correctly... To bad you still have to die.")
            
        char_animation("The shadowy figure lets out a loud roar and you feel a searing pain in your head.")
        char_animation("You are now... not dead but not alive. You are something worse - a ghost. Not in the mortal plane but not in the afterlife. Neither here nor there")
        career = GHOST
        char_animation("You leave to go back to the clearing...")
        input("")
        situtation = 1

    elif situtation == 10: #Town
        if career == None or career == 'None':
            if morailty > 0 and person_type > 0:
                career = WIZARD
            elif morailty < 0 and person_type < 0:
                career = WARLOCK
            elif morailty > 0 and person_type < 0:
                career = WARRIOR
            elif morailty < 0 and person_type > 0:
                career = VILLIAN
            else:
                career = randchoice([WIZARD, WARLOCK, WARRIOR, VILLIAN])
                previous_choices['career_choice'] = 1

        char_animation("\n\nTown")
        char_animation("\n\nThis is all for now! Come back later when chapter 2 is released!")
        input()
    
    elif situtation == 11: #Warrior's Base
        char_animation("\n\nWarrior's Base")
        char_animation("\n\nThis is all for now! Come back later when chapter 2 is released!")
        char_animation("Would you like to go: ")
        char_animation("1. Back to th Arena")
        char_animation("2. To the town")
        choice = get_char_animation_in("Enter your choice: ",{'a':['1','back'],'b':['2','town']}, allow_save=True)
        if choice == 'a':
            situtation = 12
        elif choice == 'b':
            situtation = 10
    
    elif situtation == -1 and DEBUG_ALLOWED: #Debug
        print("Debug mode")
        print(f"Situtation: {situtation}")
        print(f"Morailty: {morailty}")
        print(f"Person Type: {person_type}")
        print(f"Career: {career}")
        print(f"Previous Choices: {previous_choices}")
        print(f"Gold: {gold}")
        print(f"Inventory: {inventory}")
        print(f"Autosave: {autosave}")
        print(f"Name: {NAME}")
        print(f"Been in Situations: {been_in_situations}")
        
        print("Would you like to edit anything?")
        choice = input("Enter your choice (y/n): ").lower()
        if choice in {'y','yes'}:
            while True:
                command = input(">>> ")
                if command == 'exit':
                    break
                else:
                    exec(command)
        
        situtation = int(input("Enter the new situtation: "))
