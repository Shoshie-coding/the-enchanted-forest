# This is the start game function that also acts as an intro for the game

def start_game():
    print('''
 +-+-+-+ +-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+
 |T|h|e| |E|n|c|h|a|n|t|e|d| |F|o|r|e|s|t|
 +-+-+-+ +-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+
''')
    
    # This takes user to the beginning of the game
    answer = input("Are you ready to start the game. Type y to start the game and n to end it.\n").lower().strip()
    if answer == "y":
        print("You made the right choice!")
        time.sleep(2)
        game_intro()
        
    elif answer =="n":
        print("It seems you weren't brave enough to play the game.")
        print("Now you can wake up, it was all a dream")
       
    else:
        #Let user know the answer is incorrect
        print("This is an incorrect answer")
        print("You need to chose yes or no")
        start_game()

    
def game_intro():
    print("Welcome to the Enchanted Forest")
    print("\n The year is 1290, you are on the outskirts of the forest")
    print("You are picking mushrooms and berries")
    print("You are going further into the forest") 
    print("You don't realize it now but you are straying")
    print("away from your village")
    print("\nAfter a long time has passed, you try to get back to your village")
    print("You walk and realize that you are deep into the forest")
    print("Now you need to find a way out before it gets too dark and before the sun sets")
    print("You need to follow the prompts on the screen")
    print("And make the right choice")
    
def two_paths():
    print("\nYou come at a crossroads")
    print("There are two paths - you need to chose one of these")
    print("Go left to the straigh path across the forest")
    print("This path is lined with trees and it's not well lit")
    print("The second path is on the right")
    print("This path takes you on a narrow road down the slope in the mountains")
    print("You need to be careful walking on this path")
    print("There are rocks and tree branches everywhere")
    print("On the upside, the path is well lit, you can see where you're walking")
    time.sleep(2)

    answer = input("Which path will you chose? Type l for left and r for right").lower().strip()
    if answer == "l":
        meet_fairy()
    elif answer == "r":
        meet_wild_stag
    else:
         #Let user know the answer is incorrect
        print("This is an incorrect answer")
        print("You need to chose yes or no")
        start_game()








    






