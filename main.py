print("""
Welcome to the Text Based Adventure!

Some tips:
Come back every once in a while to see if there are any new updates!
Enter quit to exit the game.
Enter save to save your progress in the game to a file (you will need to enter a filename).
""")



def get_input(msg,accepted, err_msg = ""): #{'choice1':['choice1','alias1','alias2'],'choice2':['choice2','alias1','alias2']}
    while True:
        choice = input(msg).lower()
        if choice == 'quit':
            a = input("Are you sure? If you haven't saved your progress, you will lose it. Press enter to confirm, or anything else to cancel. You can enter 'save' to save")
            if a == '':
                exit()
        elif choice == 'save':
            filename = input("Enter a filename: ")
            with open(filename, 'w') as f:
                f.write(f"{situtation}\n{NAME}\n{been_in_situations}\n{morailty}\n{person_type}")
        for key in accepted:
            if choice in [item.lower() for item in accepted[key]]:
                print(key)
                return key
        print(err_msg, end = "")

situtation = 0
been_in_situations = set()
morailty = 0
NAME = "person"
person_type = 0

while True:
    if situtation == 0:
        print("Welcome Adventurer! Start a new game (1) or load a game (2)?")
        choice = get_input("Enter your choice: ",{'a':['1','start','new'],'b':['2','load']}, "")
        if choice == 'a':
            situtation = 1
        elif choice == 'b':
            with open(input("Enter a filename: ")) as file:
                save_data = file.read().split('\n')
                situtation = int(save_data[0])
                NAME = save_data[1]
                been_in_situations = {int(item) for item in save_data[2].strip('{}').split(',')}
                morailty = int(save_data[3])
                person_type = int(save_data[4])
        situation = 1
    
    if situtation == 1: #Clearing
        if 1 not in been_in_situations:
            print("You wake up in the clearing of a forest, not remembering how you got here. You don't remember anything or anyone. The only thing you remember is a single word: your name.")
            NAME = input("What is it?: ")
            been_in_situations.add(1)
        print(f"Hello {NAME}. You see 4 paths labeled with signs: ")

        print("\n\n")
        print("1. The path going to the Temple, it has a a bricked road with lamps on the side.")
        print("2. The path going to the Library, it has a road covered with leaves, seemingly not being disturbed in years.")
        print("3. The path to the Arena, it has a road with a lot of footprints, and you can hear the sound of swords clashing from the distance.")                    
        print("4 The path to the Dragon's lair, the sign itself tangled with vines and the path so overgrown it may as well not have been there.")
        choice = get_input("Which path do you take?: ",{'2':['1','temple'],'3':['2','library'],'4':['3','arena'],'5':['4',"dragon","lair"]})
        situtation = int(choice)
    
    if situtation == 2: #Temple
        print("Temple")

    if situtation == 3: #Library
        print("Library")

    if situtation == 4: #Arena
        print("Arena")

    if situtation == 5: #Dragon's Lair
        print("Dragon's Lair")

