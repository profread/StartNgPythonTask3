import random

userName = input("Enter a Username")

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
                print(f"YOU WON! {userName}")
                print(f"You got the number right after {count} trial \n")
                #break
                menuOption()  
            elif (userInput < easyModeNumber):
                print("\n Wrong guess, \n Your guess is low")
                print(f"\nYou have {guessCount-count} chances left\n")
                count += 1
                continue
            else:
                print("\n Wrong guess,\nYour guess is high")
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
                print(f"YOU WON! {userName}")
                print(f"You got it after {count} trials\n")
                #break
                menuOption()
            elif (userInput < mediumModeNumber):
                print("\nTWrong guess,\nYour guess is low")
                print(f"\nYou have {guessCount-count} guesses left\n")
                count += 1
                continue
            else:
                print("\n Wrong guess,\nYour guess is high")
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
                print(f"YOU WON! {userName}")
                print(f"You got it after {count} trials\n")
                #break
                menuOption()
            elif (userInput < hardModeNumber):
                print("\n Wrong guess,\nYour guess is low")
                print(f"\nYou have {guessCount-count} guesses left\n")
                count += 1
                continue
            else:
                print("\n Wrong guess,\nYour guess is high")
                print(f"\nYou have {guessCount-count} guesses left\n")
                count += 1
                continue
        except ValueError:
            print("\nYou Must enter a number")
            continue
    print(f"Game Over! You have used up your {guessCount} chances")
    menuOption()
#Game Home interface
def gameHomeMenu():
    #print("\n WELCOME, CAN YOU GUESS THE NUMBER? \n")
    print(f"\n WELCOME {userName}, CAN YOU GUESS THE NUMBER?")
    print("___________________ HOME___________________\n")
    print("1. Easy Mode")
    print("2. Medium Mode")
    print("3. Hard Mode")
    print("4. Exit the Game \n")
    print("Choose the level you wish to play \n")

    homeMenuPrompt = int(input("Reply: "))
    if (homeMenuPrompt == 1):
        easyMode()
    elif (homeMenuPrompt == 2):
        mediumMode()
    elif (homeMenuPrompt == 3):
        hardMode()
    elif (homeMenuPrompt == 4):
        exit()
    else:
        print("Enter a valid option")
        menuOption()


"""def user_id (prompt):
    if userName:
            (print(f"\n Welecome {userName}, CAN YOU GUESS THE NUMBER?"))
    while True:
        try:
             userName = str(input(prompt))
        except ValueError:
            print("Enter a Valid Username")
        continue
    if userName.isalpha():
        print(f"\n WELCOME {userName}, CAN YOU GUESS THE NUMBER? \n")
        continue
        else:
            print("Input a Valid UserName")
        break
    return userName """
   

#return the user to the manin menu or exit the game
def menuOption():
    print("\nNice try, Do you want to try again? \n")
    print("\n-------------------------- CHOOSE AN OPTION --------------------------\n")
    print("1. Return to home page?")
    print("2. Exit the Game\n")
    subhomeMenuPrompt = input("Reply: ")
    if (subhomeMenuPrompt   == '1'):
        gameHomeMenu()
    elif (subhomeMenuPrompt  == '2'):
        exit()
    else:
        exit()
var = 1
while var == 1:  
    gameHomeMenu()

