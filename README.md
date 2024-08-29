# Mythopes - Command Line Edition

always adding updates :)

Book 1 Completed!

![image](https://github.com/user-attachments/assets/624a18fd-d8a5-40b3-b8c4-1257ef356c2c)

# How to Play
 You have two options
 - Run the main.py python script
 - Run the main.exe (windows only) -> Find it in the latest release!

The other files are archival or just test files.

Keep in mind, when you enable autosave, it saves to `game.data` and will overwrite a pre-existing file with that name.

# Story

Set in a Mythical Kingdom, somewhere, sometime
> You wake up in the clearing of a forest, not remembering how you got here. You don't remember anything or anyone. The only thing you remember is a single word: your name.

Remember, nothing is as it seems. There are hundreds of choices and combinations and tons of minigames

# Commands
Enter quit to exit the game.
Enter save to save your progress in the game to a file (you will need to enter a filename).
Enter autosave to automatically save the game whenever possible.
Enter inventory to view your inventory

# Edits to source
You can edit the source to your liking! At the top of the source code you can change the following values. After that though beware, spoilers are there
```
WPM = 350 #Words speed text animation, recommended: 350
DISABLE_ANIMATION = False #Turns off text animation if enabled
DISABLE_COLORS = False #Turns off colors if enabled

#Optional | Will not change gameplay descisons only provides a more immersive dialogue
#If not provided make it None
OPENAI_API_KEY = None 
```

# Have a great idea?
Even if its a small one, write it up in a seperate text, markdown or image file and submit a pull request!

# Common Quesitons
 - Why is `main.exe` taking a while to boot up: Don't worry! The python script has been compiled using pyinstaller and is not the most efficient
 - Do I need to wait for the next book to come out before downloading the releases of the next chapters?: New binary releases will be released after every book is released. However you can always play the chapters already released by downloading and running the `main.py` script - They are interchangable!
 - Does my book 1 progress `game.data` work with book 2?: Yes! Book 2 release will include Book 1 in it and will be backward compatable.
