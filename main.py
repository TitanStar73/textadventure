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
            exit()
        elif choice == 'save':
            filename = input("Enter a filename: ")
            with open(filename, 'w') as f:
                f.write(str(situtation))
        for key in accepted:
            if choice in accepted[key]:
                return key
        print(err_msg, end = "")

situtation = 0
while True:
    if situtation == 0:
        print("Welcome Adventurer! Start a new game (1) or load a game (2)?")
        choice = get_input("Enter your choice: ",{'a':['1','start','new'],'b':['2','load']}, "")
        if choice == 'a':
            situtation = 1
        elif choice == 'b':
            with open(input("Enter a filename: ")) as file:
                situtation = int(file.read())
        situation = 1
    