import time 
import os 

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def clear_terminal():
    """
    Code for clearing the terminal
    Credit to Stack Overflow 
    https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
    """
    os.system('cls' if os.name=='nt' else 'clear')


# This is the start game function that also acts as an intro for the game
def start_game():
    print(Fore.GREEN + '''
            .        +          .      .          .
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
                   . (|::.     ,`               
                      |::.\  \ `.
                      |:::(\    |
              O       |:::/{ }  |                  (o
               )  ___/#\::`/ (O "==._____   O, (O  /`
          ~~~w/w~"~~,\` `:/,-(~`"~~~~~~~~"~o~\~/~w|/
''')
    # This takes user to type their name
    select_name = input(f"{Fore.BLUE}{Style.BRIGHT}Type your name or username to start the game\n").strip()
    print(Fore.GREEN + """
+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+-+ 
          |T|h|e| |E|n|c|h|a|n|t|e|d| |F|o|r|e|s|t|
+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+-+ 
    """)
    answer = input(f"{Fore.BLUE}Hello {select_name}, welcome to the Enchanted forest!\nType y to start the game and n to end it.\n").strip()
    if answer == "y":
        print(f"{Fore.GREEN}{Style.BRIGHT}You made the right choice!") 
        clear_terminal()
        game_intro()
    elif answer == "n":
        clear_terminal()
        print("Now you can wake up, it was all a dream.")
        game_over()
        play_again()
    else:
        #Let user know the answer is incorrect
        clear_terminal()
        print(f"{Fore.RED}This is an incorrect answer")
        time.sleep(2)
        answer = input(f"{Fore.RED}You need to type Y or N.\n")
        if answer == "y":
            print(f"{Fore.GREEN}You made the right choice!") 
            clear_terminal()
            game_intro()
        elif answer == "n":
            clear_terminal()
            print("Now you can wake up, it was all a dream.")
            game_over()
        else:
            #Let user know the answer is incorrect
            print(f"{Fore.RED}This is an incorrect answer.")
            print("Taking you to the beginning of the game")
            start_game()
        
def game_intro():
    print(f"{Fore.CYAN}\nThe year is 1290, you are on the outskirts of the forest")
    time.sleep(2)
    print(f"{Fore.CYAN}You are picking mushrooms and berries")
    time.sleep(2)
    print(f"{Fore.CYAN}You are going further into the forest") 
    time.sleep(2)
    print(f"{Fore.CYAN}And you are straying away from your village")
    time.sleep(2)
    print(f"{Fore.CYAN}After two hours, you want to go back home")
    time.sleep(2)
    print(f"{Fore.CYAN}You start walking back and realize that you are deep into the forest")
    time.sleep(2)
    print(f"{Fore.CYAN}And you don't know how to get back anymore")
    time.sleep(2)
    print(f"{Fore.CYAN}Now you need to find a way out before the sun sets")
    time.sleep(2)
    print(f"{Fore.CYAN}You need to follow the prompts on the screen to play this game.\n")
    time.sleep(2)
    print(f"{Fore.BLUE}Press C to continue the game and Q to quit")
    answer = input("").lower().strip()
    if answer == "c":
        time.sleep(2)
        clear_terminal()
        print(f"{Fore.GREEN}Great, you're brave enough to continue the game!")
        two_paths()

    elif answer == "q":
        print("Sorry to see you go!")
        game_over()
    
    else:
    #Let user know the answer is incorrect
        clear_terminal()
        print(f"{Fore.RED}This is an incorrect answer")
        time.sleep(2)
        answer = input(f"{Fore.RED}You need to type C or Q.\n")
        if answer == "c":
            time.sleep(2)
            clear_terminal()
            print(f"{Fore.GREEN}Great, you're brave enough to continue the game!")
            two_paths()
        elif answer == "q":
            print("Sorry to see you go!")
            game_over()
        else:
            #Let user know the answer is incorrect
            print(f"{Fore.RED}This is an incorrect answer.")
            print("Taking you to the beginning of the game")
            start_game()
        

def two_paths():
    print(f"{Fore.CYAN}\nYou come at a crossroads and you see two paths")
    print(f"{Fore.CYAN}Path number 1: Go on the straigh path across the forest")
    print(f"{Fore.CYAN}This path is lined with trees and is not well lit")
    print(f"{Fore.CYAN}But it's easily walkable even when it's dark.\n")
    time.sleep(2)

    print(f"{Fore.CYAN}Path number 2: this takes you on a narrow road down the slope in the mountains.")
    print(f"{Fore.CYAN}There are rocks and tree branches everywhere on this second path")
    print(f"{Fore.CYAN}On the upside, the path is well lit, you can see where you're walking\n")
    time.sleep(2)

    answer = input(f"{Fore.BLUE}Which path will you chose? Type 1 or 2.\n").lower().strip()
    if answer == "1":
        clear_terminal()
        print("\nExcellent choice!\n")
        time.sleep(2)
        meet_fairy()
    elif answer == "2":
        print("This is a good choice. Now let's see where it takes you")
        time.sleep(2)
        meet_stag()
    else:
        #Let user know the answer is incorrect
        clear_terminal()
        print(f"{Fore.RED}This is an incorrect answer")
        time.sleep(2)
        answer = input(f"{Fore.RED}You need to type Y or N.\n")
        if answer == "1":
            print(f"{Fore.GREEN}You made the right choice!") 
            clear_terminal()
            meet_fairy()
        elif answer == "2":
            print(f"{Fore.GREEN}This is a great choice, let's see who you're going to meet this time")
            clear_terminal()
            meet_stag()
        else:
            #Let user know the answer is incorrect
            print(f"{Fore.RED}This is an incorrect answer.")
            print("Taking you to the beginning of the game.")
            start_game()


def meet_fairy():
    print(f"{Fore.CYAN}After walking around half an hour")
    print(f"{Fore.CYAN}You meet a fairy. She's sitting on a tree log, playing a harph")
    print(f"{Fore.CYAN}She lights up everything around her\n")
    time.sleep(2)
    print(f"{Fore.CYAN}It's getting dark, and she offers to lead you through the forest")
    print(f"{Fore.CYAN}But you you see a big torch on the ground\n")

    answer = input(f"{Fore.BLUE}Which will you chose to guide you home? Type 1 for torch or 2 for fairy.\n").lower().strip()
    clear_terminal()
    if answer == "1":
        print(f"{Fore.RED}This is an unfortunate choice. You cannot survive alone in the forest")
        print(f"{Fore.RED}You meet a bear and wrestle with him and die")
        time.sleep(2)
        game_over()
        time.sleep(2)
        play_again()
    elif answer == "2":
        print(f"{Fore.GREEN}Fantastic choice, the forest fairies will always guide you find your way home")
        clear_terminal()
        meet_redhead_woman()
    else:
        #Let user know the answer is incorrect
        clear_terminal()
        print(f"{Fore.RED}This is an incorrect answer")
        time.sleep(2)
        answer = input(f"{Fore.RED}You need to type 1 or 2.\n")
        if answer == "1":
            print(f"{Fore.RED}This is an unfortunate choice. You cannot survive alone in the forest")
            print(f"{Fore.RED}You meet a bear and wrestle with him and die")
            game_over()
            play_again()
        elif answer == "2":
            time.sleep(2)
            clear_terminal()
            print(f"{Fore.GREEN}Fantastic choice, the forest fairies will always guide you find your way home")
            meet_redhead_woman()
        else:
            #Let user know the answer is incorrect
            print(f"{Fore.RED}This is an incorrect answer.")
            time.sleep(2)
            print("Taking you to the beginning of the game.")
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

    answer = input("Which do you chose? 1 - eat what's in the basket or 2 - eat the honey")
    if answer == "1":
        print("This is a bad choice. The readhead woman transforms into a witch.")
        print("The food from the basket was poisoned")
        print("You soon get sick and die")
        game_over()
        play_again()

    elif answer == "2":
        print("Great choice!")
        print("The honey is nutritious and will give you enough energy to continue your trip")
        


def meet_knight():
    print("You walk further along the path")
    print("You see a knight in his shiny armour mounted on his black horse")
    print("You know that it's the knights job to maintain law and order")
    print("The knight asks you who you are and what you're doing in the forest")
    print("You tell the knight you're trying to get home")
    print("The knight gives you two options\n")
    print("Option #1: You can ")
    


def game_over():    
    print(Fore.RED + """
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
        print(Fore.GREEN + """
                                                                     __ 
 _____ _           _          ___                _         _        |  |
|_   _| |_ ___ ___| |_ ___   |  _|___ ___    ___| |___ _ _|_|___ ___|  |
  | | |   | .'|   | '_|_ -|  |  _| . |  _|  | . | | .'| | | |   | . |__|
  |_| |_|_|__,|_|_|_,_|___|  |_| |___|_|    |  _|_|__,|_  |_|_|_|_  |__|
                                            |_|       |___|     |___|   
    """)  

    else:  
        #Let user know the answer is incorrect
        print("This is an incorrect answer")
        print("You need to type Y or N")
        print("You will now be directed to the beginning of the game")
        clear_terminal()
        start_game()
        


start_game()








    






