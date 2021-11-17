# This is the start game function that also acts as an intro for the game

def start_game():
    print('''
 +-+-+-+ +-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+
 |T|h|e| |E|n|c|h|a|n|t|e|d| |F|o|r|e|s|t|
 +-+-+-+ +-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+
''')

    #User options at the start of the game
    answer = input("Are you ready to start the game. Type yes to start the game and no to end it. \n").lower().strip()
    # This takes user to the beginning of the game
    if answer == "yes":
        print("You made the right choice!")
        print("Welcome to ...")
        game_intro()
    elif answer =="no":
        print("We're sorry you weren't brave enough to play the game.")
        print("Now you can wake up, it was all a dream")
        time.sleep(2)
        
    else:
        #Print out the incorrect answer message
        print("This is an incorrect answer")
        print("You need to chose yes or no")
    
def game_intro():
    print("Welcome to the Enchanted Forest")
    print("\n The year is 1290, you are on the outskirts of the forest")
    print("You are picking mushrooms and berries")
    print("You are going further into the forest") 
    print("You don't realize it now but you are straying")
    print("away from your village")
    print("\n After a long time has passed, you try to get back to your village")
    print("You walk and realize that you are deep into the forest")
    print("Now you need to find a way out before it gets too dark and before the sun sets")
    print("You need to follow the prompts on the screen and make the right choice")
    print("\n You have 2 choices now, type yes if you want to leave the game or no if you want to get out of the forest")
        


start_game()







