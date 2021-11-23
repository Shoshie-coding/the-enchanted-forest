import time 

# This is the start game function that also acts as an intro for the game
def start_game():
    print('''
 +-+-+-+ +-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+
 |T|h|e| |E|n|c|h|a|n|t|e|d| |F|o|r|e|s|t|
 +-+-+-+ +-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+
''')

    
    # This takes user to type their name
    select_name = input("Type your name or username to start the game\n").strip()
       
    answer = input(f"Hello {select_name}, welcome to the Enchanted forest!\nType y to start the game and n to end it.\n").strip()
    if answer == "y":
        print("You made the right choice!")
        time.sleep(2)
        game_intro()
        
    elif answer =="n":
        print("Now you can wake up, it was all a dream")
        game_over()

    else:
        #Let user know the answer is incorrect
        print("This is an incorrect answer")
        print("You need to chose yes or no y/n")
        start_game()

    
def game_intro():
    print("\nThe year is 1290, you are on the outskirts of the forest")
    print("You are picking mushrooms and berries")
    print("You are going further into the forest") 
    print("You don't realize it now but you are straying")
    print("Away from your village")
    print("\nAfter a long time has passed, you try to get back to your village")
    print("You walk and realize that you are deep into the forest")
    print("And you don't know how to get back anymore")
    print("Now you need to find a way out before the sun sets")
    print("You need to follow the prompts on the screen")
    print("Press c to continue the game and q to quit")

    answer = input(">\n").lower().strip()

    if answer == "c":
        time.sleep(2)
        two_paths()
    
    elif answer == "q":
        start_game()

    else:
        """
        Let user know the answer is incorrect and takes 
        user to the start of the game
        """
        print("This is an incorrect answer")
        print("You need to chose yes or no")
        start_game()

 
def two_paths():
    print("\nYou come at a crossroads and you see twp paths")
    print("You need to chose one of these")
    print("Go left to the straigh path across the forest")
    print("This path is lined with trees and it's not well lit")
    print("The second path is on the right")
    print("This path takes you on a narrow road down the slope in the mountains")
    print("You need to be careful walking on this path")
    print("There are rocks and tree branches everywhere")
    print("On the upside, the path is well lit, you can see where you're walking")
    time.sleep(2)

    answer = input("Which path will you chose? Type l for left and r for right\n").lower().strip()
    if answer == "l":
        meet_fairy()
    elif answer == "r":
        print("Call function meet_wild_stag()")
    else:
        #Let user know the answer is incorrect
        print("This is an incorrect answer")
        print("You need to chose yes or no")
        start_game()

def meet_fairy():
    print("After walking around half an hour")
    print("You meet a fairy")
    print("She's sitting on a tree log, playing a harph")
    print("She lights up everything around her")
    print("It's getting dark, and she offers to lead you through the forest")

    
    answer = input("Which will you chose? Type lantern or fairy to select your choice.\n").lower().strip()
    if answer == "lantern":
        game_over("You cannot survive alone in the forest")
    elif answer == "fairy":
        print("Fantastic choice, the forest fairies will always guide you find your way home")
        meet_redhead_woman()
    else:
        #Let user know the answer is incorrect
        print("This is an incorrect answer")
        print("You need to chose yes or no")
        start_game()


def meet_redhead_woman():
    print("The fairy brings you to a clearing in the forest")
    print("You continue your journey through the woods,")
    print("thinking of the best way to get home to your village")
    print("But you get hungry and thristy")
    print("Now you hear water flowing in the distance")
    print("You walk toweards that direction")
    print("And you find a river and drink water from it")
    print("You see a young woman with long red hair")
    print("She's holding a basket with fruits and meat pies in it")
    print("You also see a beehive with honey in it")
    print("You have 2 options, type basket to east the contents of the basket")
    print("Type honey to eat the honey")
    



def game_over():
    print("\n" + "reason")
    print("Game over!")
    answer = input("Do you want to play again. Type y to play again")
    if answer == "y":
        start_game()
    else:  
        #Let user know the answer is incorrect
        print("This is an incorrect answer")
        print("You need to chose yes or no")
        start_game()

    


start_game()








    






