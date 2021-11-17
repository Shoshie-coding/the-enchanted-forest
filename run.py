# This is the start game function

def start_game():
    print("Welcome to the Enchanted Forest")
    print("\n The year is 1290, you are on the outskirts of the forest")
    print("\n You are picking mushrooms and berries")
    print("\n You are going further into the forest") 
    print("\n You don't realize it now but you are straying")
    print("\n away from your village")
    print("After a long time has passed, you try to get back to your village")
    print("You walk and realize that you are deep into the forest")
    print("Now you need to find a way out before it gets too dark and before the sun sets")
    print("You need to follow the prompts on the screen and make the right choice")
    print("\n You have 2 choices now, type yes if you want to leave the game or no if you want to get out of the forest")
     

answer = input(">").lower()

if answer == "yes":
    print("You made the right choice")
    meet_witch()

elif answer =="no":
    print("We're sorry you weren't brave enough to play the game.")
    print("Now you can wake up, it was all a dream")
    time.sleep(2)
    start_game()
else:
    answer == 
    #Print out the incorrect answer message
    print("\n This is an incorrect answer")
    print("You need to chose yes or no")
    end_game()

start_game()


