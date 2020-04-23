import random

def easyMode():
    print("\n___________________ EASY MODE ON___________________\n")
    easyModeNumber = random.randrange(1,10)
    count = 1
    guessCount = 6 #user has 6 chances in easy mode
     #loop check user input for correct number if option is remaining
    while(count <= guessCount):
        try:
            userInput = int(input(f"\n You have {guessCount} chances Guess the Number "))
            if (userInput == easyModeNumber):
                print("\nYour guess is right")
                print(f"You got the number right after {count} trial \n")
                #break
                menuOption()  
            elif (userInput < easyModeNumber):
                print("\nThat was wrong\nYour guess is low")
                print(f"\nYou have {guessCount-count} chances left\n")
                count += 1
                continue
            else:
                print("\nThat was wrong\nYour guess is high")
                print(f"\nYou have {guessCount-count} chances left\n")
                count += 1
                continue
        except ValueError:
            print("\n You Must Enter a Number")
            continue
    print(f"Game Over! You have used up your {guessCount} chances ")
    menuOption()

def mediumMode():
    print("\n___________________  MEDIUM MODE ON ___________________ \n")
    mediumModeNumber = random.randrange(1,20)
    count = 1
    guessCount = 4 # In medium mode user has 4 number options
    #loop check user input for correct number if option is remaining
    while (count <= guessCount):
        try:
            userInput = int(input("\nWhat is the number? "))
            if (userInput == mediumModeNumber):
                print("\nYou guessed right")
                print(f"You got it after {count} trials\n")
                #break
                menuOption()
            elif (userInput < mediumModeNumber):
                print("\nThat was wrong\nYour guess is low")
                print(f"\nYou have {guessCount-count} guesses left\n")
                count += 1
                continue
            else:
                print("\nThat was wrong\nYour guess is high")
                print(f"\nYou have {guessCount-count} guesses left\n")
                count += 1
                continue
        except ValueError:
            print("\nYou Must Enter a Number")
            continue
    print(f"Game Over! You have used up your {guessCount} chances")
    menuOption()

def hardMode():
    print("\n___________________ HARD MODE ON ___________________\n")
    hardModeNumber = random.randrange(1,50)
    count = 1
    guessCount = 3
    while (count <= guessCount):
        try:
            userInput = int(input("\nWhat is the number? "))
            if (userInput == hardModeNumber):
                print("\nYou guessed right")
                print(f"You got it after {count} trials\n")
                #break
                menuOption()
            elif (userInput < hardModeNumber):
                print("\nThat was wrong\nYour guess is low")
                print(f"\nYou have {guessCount-count} guesses left\n")
                count += 1
                continue
            else:
                print("\nThat was wrong\nYour guess is high")
                print(f"\nYou have {guessCount-count} guesses left\n")
                count += 1
                continue
        except ValueError:
            print("\nYou Must enter a number")
            continue
    print(f"Game Over! You have used up your {guessCount} chances")
    menuOption()

def gameHomeMenu():
    print("\n WELCOME, CAN YOU GUESS THE NUMBER? \n")
    print("___________________ HOME___________________\n")
    print("1. Easy Mode")
    print("2. Medium Mode")
    print("3. Hard Mode")
    print("4. Exit the Game \n")
    print("Choose the level you wish to play \n")

    promptQuestion = int(input("Reply: "))
    if (promptQuestion == 1):
        easyMode()
    elif (promptQuestion == 2):
        mediumMode()
    elif (promptQuestion == 3):
        hardMode()
    elif (promptQuestion == 4):
        exit()
    else:
        print("Enter a valid option")
        menuOption()
#return the user to the manin menu or exit the game
def menuOption():
    print("\nNice try, Do you want to try again? \n")
    print("\n-------------------------- KINDLY CHOOSE WHAT NEXT --------------------------\n")
    print("1. Do you want to return to home page?")
    print("2. Do you want to exit\n")
    promptQuestion = input("Reply: ")
    if (promptQuestion == '1'):
        gameHomeMenu()
    elif (promptQuestion == '2'):
        exit()
    else:
        exit()
var = 1
while var == 1:  # it is used to create an infinite loop in order to continue running the program
    gameHomeMenu()