import time 
import os 


def clear_terminal():
    """
    Code for clearing the terminal
    Credit to Stack Overflow 
    https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
    """
    os.system('cls' if os.name=='nt' else 'clear')


# This is the start game function that also acts as an intro for the game
def start_game():
    print('''
 +-+-+-+ +-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+
 |T|h|e| |E|n|c|h|a|n|t|e|d| |F|o|r|e|s|t|
 +-+-+-+ +-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+

            .        +          .      .          .
     .            _        .                    .
  ,              /;-._,-.____        ,-----.__
 ((        .    (_:#::_.:::. `-._   /:, /-._, `._,
  `                 \   _|`"=:_::.`.);  \ __/ /
                      ,    `./  \:. `.   )==-'  .
    .      ., ,-=-.  ,\, +#./`   \:.  / /           .
.           \/:/`-' , ,\ '` ` `   ): , /_  -o
       .    /:+- - + +- : :- + + -:'  /(o-) \)     .
  .      ,=':  \    ` `/` ' , , ,:' `'--".--"---._/`7
   `.   (    \: \,-._` ` + '\, ,"   _,--._,---":.__/
              \:  `  X` _| _,\/'   .-'
.               ":._:`\____  /:'  /      .           .
                    \::.  :\/:'  /              +
   .                 `.:.  /:'  }      .
           .           ):_(:;   \           .
                      /:. _/ ,  |
                   . (|::.     ,`                  .
     .                |::.    {\
                      |::.\  \ `.
                      |:::(\    |
              O       |:::/{ }  |                  (o
               )  ___/#\::`/ (O "==._____   O, (O  /`
          ~~~w/w~"~~,\` `:/,-(~`"~~~~~~~~"~o~\~/~w|/~
          ~~~~~~~~~~~~~~~~~~~~~~~\\W~~~~~~~~~~~~\|/~~
''')
    # This takes user to type their name
    select_name = input("Type your name or username to start the game\n").strip()
    answer = input(f"Hello {select_name}, welcome to the Enchanted forest!\nType y to start the game and n to end it.\n").strip()
    if answer == "y":
        print("You made the right choice!")
        clear_terminal()
        game_intro()
    elif answer == "n":
        clear_terminal()
        print("Now you can wake up, it was all a dream.")
        game_over()
        play_again()
    else:
        #Let user know the answer is incorrect
        print("This is an incorrect answer")
        print("You need to chose yes or no y/n")
        start_game()

    
def game_intro():
    print("\nThe year is 1290, you are on the outskirts of the forest")
    time.sleep(2)
    print("You are picking mushrooms and berries")
    time.sleep(2)
    print("You are going further into the forest") 
    time.sleep(2)
    print("and you are straying away from your village")
    time.sleep(2)
    print("After two hours, you want to go back home")
    time.sleep(2)
    print("You start walking back and realize that you are deep into the forest")
    time.sleep(2)
    print("And you don't know how to get back anymore")
    time.sleep(2)
    print("Now you need to find a way out before the sun sets")
    time.sleep(2)
    print("You need to follow the prompts on the screen to play this game")
    time.sleep(2)
    print("Press c to continue the game and q to quit")

    answer = input("\n").lower().strip()
    if answer == "c":
        time.sleep(2)
        clear_terminal()
        two_paths()
    elif answer == "q":
        game_over()
    else:
        """
        Let user know the answer is incorrect and takes 
        user to the start of the game
        """
        print("This is an incorrect answer")
        print("You need to chose yes or no")
        start_game()

def two_paths():
    print("\nYou come at a crossroads and you see two paths")
    print("Path number 1: Go on the straigh path across the forest")
    print("This path is lined with trees and it's @not well lit")
    print("But it's very easy to walk on this path")
    print("Path number 2: this takes you on a narrow road down the slope in the mountains")
    print("There are rocks and tree branches everywhere on this second path")
    print("On the upside, the path is well lit, you can see where you're walking")
    time.sleep(2)

    answer = input("Which path will you chose? Type 1 or 2\n").lower().strip()
    if answer == "1":
        print("Excellent choice!")
        clear_terminal()
        meet_fairy()
    elif answer == "r2":
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

def meet_knight():
    print("You walk further along the path")
    print("You see a knight in his shiny armour mounted on his black horse")
    print("You know that it's the knights job to maintain law and order")
    print("The knight asks you who you are and what you're doing in the forest")
    print("You tell the knight you're trying to get home")
    print("The knight gives you two options")
    


def game_over():
    print("""
   _____                                            _ 
  / ____|                                          | |
 | |  __  __ _ _ __ ___   ___    _____   _____ _ __| |
 | | |_ |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__| |
 | |__| | (_| | | | | | |  __/ | (_) \ V /  __/ |  |_|
  \_____|\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|  (_)

  """)
                                                      
                                                      
def play_again():
    answer = input("Do you want to play again?\n Y / N\n").lower()
    if answer == "y":
        clear_terminal()
        start_game()
    elif answer == 'n':
        print("""
  _____ _                 _           __                    _             _             _ 
 |_   _| |__   __ _ _ __ | | _____   / _| ___  _ __   _ __ | | __ _ _   _(_)_ __   __ _| |
   | | | '_ \ / _` | '_ \| |/ / __| | |_ / _ \| '__| | '_ \| |/ _` | | | | | '_ \ / _` | |
   | | | | | | (_| | | | |   <\__ \ |  _| (_) | |    | |_) | | (_| | |_| | | | | | (_| |_|
   |_| |_| |_|\__,_|_| |_|_|\_\___/ |_|  \___/|_|    | .__/|_|\__,_|\__, |_|_| |_|\__, (_)
                                                     |_|            |___/         |___/   
    """)  

    else:  
        #Let user know the answer is incorrect
        print("This is an incorrect answer")
        print("You need to type Y or N")
        print("You will now be directed to the beginning of the game")
        clear_terminal()
        start_game()

    

start_game()








    






