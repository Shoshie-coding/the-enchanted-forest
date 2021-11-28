import time 
import os 
import colorama
from colorama import Fore, Style, Back

colorama.init(autoreset=True)


def clear_terminal():
    """
    Code for clearing the terminal
    Credit to Stack Overflow 
    https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
    """ 
    os.system('cls' if os.name == 'nt' else 'clear')


def start_game():
    """
    This function welcomes user to the game
    Asks user to enter a username
    And give the option to start the game
    Or quit if they want to do so
    """
    print(Fore.LIGHTGREEN_EX + '''
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

    name = input(f"{Fore.YELLOW}{Style.BRIGHT}Type a username to start the game\n")

    print(Fore.GREEN + """
+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+-+ 
          |T|h|e| |E|n|c|h|a|n|t|e|d| |F|o|r|e|s|t|
+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+-+-+-+ 
    """)
    print(f"{Fore.CYAN}Hello {name}, welcome to the Enchanted forest!")
    answer = input(f"{Fore.YELLOW}{Style.BRIGHT}Type S to start the game and E to end it.\n")
    if answer == "s":
        clear_terminal()
        game_intro()
    elif answer == "e":
        clear_terminal()
        print(f"{Fore.CYAN}Now you can wake up, it was all a dream.")
        game_over()
        play_again()
    else:
        """
        Let user know the answer is incorrect
        """
        clear_terminal()
        print(f"{Fore.WHITE}{Back.RED}This is an incorrect answer")
        time.sleep(2)
        answer = input(f"{Fore.WHITE}{Back.RED}You need to type S or E.\n")
        if answer == "s":
            print(f"{Fore.CYAN}You made the right choice!") 
            clear_terminal()
            game_intro()
        elif answer == "e":
            clear_terminal()
            print(f"{Fore.CYAN}Now you can wake up, it was all a dream.")
            game_over()
        else:
            """
            Let user know the answer is incorrect
            """
            print(f"{Fore.WHITE}{Back.RED}This is an incorrect answer.")
            print(f"{Fore.CYAN}Taking you to the beginning of the game")
            time.sleep(4)
            start_game()      


def game_intro():
    print(f"{Fore.CYAN}The year is 1290")
    print(f"{Fore.CYAN}You are on the outskirts of the forest")
    print(f"{Fore.CYAN}You are picking mushrooms and berries\n")
    time.sleep(2)
    print(f"{Fore.CYAN}You are going further into the forest") 
    print(f"{Fore.CYAN}And you are straying away from your village\n")
    time.sleep(2)
    print(f"{Fore.CYAN}After two hours, you want to go back home")
    print(f"{Fore.CYAN}You start walking back")
    print(f"{Fore.CYAN}And realize that you are deep into the forest\n")
    print(f"{Fore.CYAN}And you don't know how to get back anymore")
    time.sleep(2)
    print(f"{Fore.CYAN}Now you need to find a way out before the sun sets\n")
    print(f"{Fore.CYAN}You know it's not safe to be in the forest at night")
    print(f"{Fore.CYAN}This is when the forest comes alive!")
    print(f"{Fore.CYAN}And all kinds of creatures lurk around")
    time.sleep(2)
    print(f"{Fore.CYAN}Follow the prompts on the screen to play this game\n")
    print(f"{Fore.CYAN}And see if you can escape")
    print(f"{Fore.CYAN}From the forest before sunset")
    time.sleep(2)
    print(f"{Fore.YELLOW}{Style.BRIGHT}\nPress C to continue or Q to quit")
    answer = input("").lower().strip()
    if answer == "c":
        time.sleep(2)
        clear_terminal()
        print(f"{Fore.CYAN}Great, you're brave enough to continue the game!")
        two_paths()

    elif answer == "q":
        print(f"{Fore.CYAN}Sorry to see you go!")
        game_over()  
    else:
        """
        Lets user know the answer 
        is incorrect
        """
        clear_terminal()
        print(f"{Fore.WHITE}{Back.RED}This is an incorrect answer")
        time.sleep(2)
        answer = input(f"{Fore.WHITE}{Back.RED}You need to type C or Q.\n")
        if answer == "c":
            time.sleep(2)
            clear_terminal()
            print(f"{Fore.CYAN}Great, you're brave enough \
            to continue the game!")
            two_paths()
        elif answer == "q":
            print(f"{Fore.CYAN}Sorry to see you go!")
            game_over()
        else:
            """
            Lets user know the answer is incorrect
            and takes them to start_game()
            """
            print(f"{Fore.WHITE}{Back.RED}This is an incorrect answer.")
            print("Taking you to the beginning of the game")
            time.sleep(4)
            start_game()       


def two_paths():
    print(f"{Fore.CYAN}\nYou come at a crossroads and you see two paths")

    time.sleep(2)
    print(f"{Fore.CYAN}Path number 1: Go on the straight path")
    print(f"{Fore.CYAN}This path is lined with trees and is not well lit")
    print(f"{Fore.CYAN}But it's easily walkable even when it's dark.\n")
    time.sleep(2)

    print(f"{Fore.CYAN}Path number 2: this takes you on a narrow road")
    print(f"{Fore.CYAN}Down the slope in the mountains.")
    time.sleep(2)
    print(f"{Fore.CYAN}There are rocks and tree branches everywhere")
    print(f"{Fore.CYAN}On the upside, the path is well lit")
    print(f"{Fore.CYAN}And you can see where you're walking\n")
    time.sleep(2)

    answer = input(f"{Fore.YELLOW}{Style.BRIGHT}Which path will you chose?\
    Type 1 or 2.\n").lower().strip()
    if answer == "1":
        clear_terminal()
        print(f"{Fore.CYAN}\nExcellent choice!\n")
        time.sleep(2)
        meet_fairy()
    elif answer == "2":
        clear_terminal()
        print(f"{Fore.CYAN}\nThis is a good choice.")
        print(f"{Fore.CYAN}Now let's see where it takes you")
        time.sleep(5)
        clear_terminal
        meet_deer()
    else:
        """
        Lets user know the answer is incorrect
        """
        clear_terminal()
        print(f"{Fore.WHITE}{Back.RED}This is an incorrect answer")
        time.sleep(2)
        answer = input(f"{Fore.WHITE}{Back.RED}You need to type 1 or 2.\n")
        if answer == "1":
            print(f"{Fore.CYAN}You made the right choice!") 
            time.sleep(2)
            meet_fairy()
        elif answer == "2":
            print(f"{Fore.CYAN}This is a great choice")
            print(f"{Fore.CYAN}Let's see who you're going to meet this time")
            time.sleep(2)
            meet_deer()
        else:
            """
            Lets user know the answer is incorrect
            And takes them to start_game()
            """
            print(f"{Fore.WHITE}{Back.RED}This is an incorrect answer.")
            print(f"{Fore.CYAN}Taking you to the beginning of the game.")
            time.sleep(4)
            start_game()


def meet_fairy():
    print(f"{Fore.CYAN}After walking around half an hour")
    print(f"{Fore.CYAN}You meet a fairy.")
    print(f"{Fore.CYAN}She's sitting on a tree log, playing a harph")
    print(f"{Fore.CYAN}She lights up everything around her\n")
    time.sleep(2)
    print(f"{Fore.CYAN}It's getting dark, and she offers to show you")
    print(f"{Fore.CYAN}The way through the forest")
    print(f"{Fore.CYAN}But you you see a big torch on the ground\n")
    print(f"{Fore.CYAN}You have two options now")
    print(f"{Fore.CYAN}Option #1 pick up the torch and find your way home")
    print(f"{Fore.CYAN}Option #2 let the fairy guide you trhough the forest")

    answer = input(f"{Fore.YELLOW}{Style.BRIGHT}\nWhich will you chose: 1 or 2?")
    clear_terminal()
    if answer == "1":
        print(f"{Fore.WHITE}{Back.RED}This is an unfortunate choice.")
        print(f"{Fore.WHITE}{Back.RED}You cannot survive alone in the forest")
        print(f"{Fore.WHITE}{Back.RED}You meet a bear and wrestle with him and die")
        time.sleep(2)
        game_over()
        time.sleep(2)
        play_again()
    elif answer == "2":
        print(f"{Fore.CYAN}\nFantastic choice!")
        print(f"{Fore.CYAN}The forest fairies will always")
        print(f"{Fore.CYAN}Help you find your way home.\n")
        meet_redhead_woman()
    else:
        """
        Let user know the answer is incorrect
        """
        clear_terminal()
        print(f"{Fore.WHITE}{Back.RED}This is an incorrect answer")
        time.sleep(2)
        answer = input(f"{Fore.WHITE}{Back.RED}You need to type 1 or 2.\n")
        if answer == "1":
            print(f"{Fore.WHITE}{Back.RED}This is an unfortunate choice")
            print(f"{Fore.WHITE}{Back.RED}You cannot survive alone in the forest")
            print(f"{Fore.WHITE}{Back.RED}You meet a bear and wrestle with him and die")
            print()
            game_over()
            play_again()
        elif answer == "2":
            time.sleep(2)
            clear_terminal()
            print(f"{Fore.CYAN}\nFantastic choice!")
            print(f"{Fore.CYAN}The forest fairies will always")
            print(f"{Fore.CYAN}Help you find your way home.\n")
            meet_redhead_woman()
        else:
            """
            Lets user know the answer is incorrect 
            And takes them to start_game()
            """
            print(f"{Fore.WHITE}{Back.RED}This is an incorrect answer.")
            time.sleep(2)
            print(f"{Fore.CYAN}Taking you to the beginning of the game.")
            time.sleep(4)
            start_game()


def meet_deer():
    print(f"{Fore.CYAN}\nYou carefully walk down the mountains")
    print(f"{Fore.CYAN}And then up again until you come to a waterfall")
    time.sleep(2)
    print(f"{Fore.CYAN}You go there to drink some water")
    input(f"{Fore.YELLOW}{Style.BRIGHT}\nPress 'enter' to continue the game.\n")
    time.sleep(2)

    print(f"{Fore.CYAN}You notice a deer at the top of the waterfall")
    time.sleep(2)

    print(Fore.CYAN + """
     /|       |\
  `__\\       //__'
     ||      ||
   \__`\     |'__/
     `_\\   //_'
     _.,:---;,._
     \_:     :_/
       |@. .@|
       |     |
       ,\.-./ \
       ;;`-'   `---__________-----.-.
       ;;;                         \_\
       ';;;                         |
        ;    |                      ;
         \   \     \        |      /
          \_, \    /        \     |\
            |';|  |,,,,,,,,/ \    \ \_
            |  |  |           \   /   |
            \  \  |           |  / \  |
             | || |           | |   | |
             | || |           | |   | |
             |_||_|           |_|   |_|
            /_//_/           /_/   /_/ 

    """)
    time.sleep(2)
    print(f"{Fore.CYAN}You know these are ellusive animals")
    print(f"{Fore.CYAN}You see this as a good omen")
    time.sleep(2)
    print(f"{Fore.CYAN}The deer gets closer to you")
    print(f"{Fore.CYAN}And stands on its hind legs")
    print(f"{Fore.CYAN}As a sign for you to follow it")

    input(f"{Fore.YELLOW}{Style.BRIGHT}Press 'enter'to see where the deer leads you.\n")
    time.sleep(2)
    print(f"{Fore.CYAN}The deer leads you out of the valley")
    print(f"{Fore.CYAN}And into the forest")
    print(f"{Fore.CYAN}And leaves you near a tall old oak tree")
    time.sleep(2)
    print(f"{Fore.CYAN}You see a marking on its trunk")
    print(f"{Fore.CYAN}Indicating two roads")
    time.sleep(2)
    print(f"{Fore.CYAN}\nOption #1 - the first road leads to a river")
    print(f"{Fore.CYAN}You know this is the same river")
    print(f"{Fore.CYAN}That flows near your village")
    print(f"{Fore.CYAN}Option #2 - the second road leads you to a horse")

    answer = input(f"{Fore.YELLOW}{Style.BRIGHT}Which do you chose: 1 or 2?\n")
    if answer == "1":
        clear_terminal()
        print(f"{Fore.WHITE}{Back.RED}This is a bad choice")
        print(f"{Fore.RED}{Back.RED}It's too long for you to walk home\n")
        time.sleep(2)
        print(f"{Fore.RED}{Back.RED}You soon get too tired")
        print(f"{Fore.RED}{Back.RED}And are unable to walk home")
        print(f"{Fore.RED}{Back.RED}You lose the game")
        game_over()
        play_again()
    elif answer == "2":
        clear_terminal()
        print(f"{Fore.CYAN}This is a great choice!")
        print(f"{Fore.CYAN}You hop on the horse\n")
        time.sleep(2)
        print(f"{Fore.CYAN}And go back to the river")
        print(f"{Fore.CYAN}You reach your house before sunset")
        print(f"{Fore.CYAN}You reunite with your family")
        print(f"{Fore.CYAN}Who are happy to see you!")
        win_game()
        time.sleep(2)
        play_again()
    else:
        """
        Let user know the answer is incorrect
        """
        clear_terminal()
        print(f"{Fore.RED}{Back.RED}This is an incorrect answer")
        time.sleep(2)
        answer = input(f"{Fore.RED}{Back.RED}You need to type 1 or 2.\n")
        if answer == "1":
            clear_terminal()
            print(f"{Fore.RED}{Back.RED}This is a bad choice")
            print(f"{Fore.RED}{Back.RED}It's too long for you to walk home")
            print(f"{Fore.RED}{Back.RED}You soon get too tired")
            print(f"{Fore.RED}{Back.RED}And are unable to walk home")
            print(f"{Fore.RED}{Back.RED}You lose the game")
            game_over()
            play_again()
        elif answer == "2":
            clear_terminal()
            print(f"{Fore.CYAN}This is a great choice!")
            print(f"{Fore.CYAN}You hop on the horse")
            print(f"{Fore.CYAN}And go back to the river")
            print(f"{Fore.CYAN}You reach your house before sunset")
            print(f"{Fore.CYAN}You reunite with your family")
            print(f"{Fore.CYAN}Who are happy to see you!")
            win_game()
            time.sleep(2)
            play_again()
        else:
            """
            Lets user know the answer is incorrect
            And takes them to start_game()
            """
            print(f"{Fore.RED}{Back.RED}This is an incorrect answer.")
            time.sleep(2)
            print(f"{Fore.RED}{Back.RED}Taking you to the beginning of the game.")
            time.sleep(4)
            start_game()


def meet_redhead_woman():
    print(f"{Fore.CYAN}The fairy brings you to a clearing in the forest")
    print(f"{Fore.CYAN}You continue your journey through the woods,")
    print(f"{Fore.CYAN}Thinking of the best way")
    print(f"{Fore.CYAN}To get home to your village.\n")
    time.sleep(2)
    print(f"{Fore.CYAN}But you get hungry and thristy.")
    print(f"{Fore.CYAN}Now you hear water flowing in the distance")
    print(f"{Fore.CYAN}You walk towards that direction")
    print(f"{Fore.CYAN}You find a stream and drink water from it.\n")
    time.sleep(2)
    print(f"{Fore.CYAN}You see a young woman with long red hair")
    print(f"{Fore.CYAN}She's holding a basket with fruits and meat pies in it")
    print(f"{Fore.CYAN}You also see a beehive with honey")
    print(f"{Fore.CYAN}In the tree besides you.\n")
    print(f"{Fore.CYAN}You know have two options\n")
    print(f"{Fore.CYAN}In the tree besides you.\n") 
    print(f"{Fore.CYAN}Option #1 - eat what's in the basket")
    print(f"{Fore.CYAN}Option #2 - eat the honey.")
    answer = input(f"{Fore.YELLOW}{Style.BRIGHT}Which do you chose: 1 or 2?\n")
    if answer == "1":
        print(f"{Fore.RED}{Back.RED}This is a bad choice.")
        print(f"{Fore.RED}{Back.RED}The readhead woman transforms into a witch.")
        print(f"{Fore.RED}{Back.RED}The food from the basket was poisoned")
        print(f"{Fore.RED}{Back.RED}You soon get sick and die")
        game_over()
        play_again()

    elif answer == "2":
        clear_terminal()
        print(f"{Fore.CYAN}\nGreat choice!")
        print(f"{Fore.CYAN}The honey is nutritious")
        print(f"{Fore.CYAN}And will give you energy to continue your trip")
        meet_knight()
    else:
        """
        Let user know the answer is incorrect
        """
        clear_terminal()
        print(f"{Fore.RED}{Back.RED}This is an incorrect answer")
        time.sleep(2)
        answer = input(f"{Fore.RED}{Back.RED}You need to type 1 or 2.\n")
        if answer == "1":
            print(f"{Fore.RED}{Back.RED}This is a bad choice.")
            print(f"{Fore.RED}{Back.RED}The readhead woman transforms into a witch.")
            print(f"{Fore.RED}{Back.RED}The food from the basket was poisoned")
            print(f"{Fore.RED}{Back.RED}You soon get sick and die")
            game_over()
            play_again()
        elif answer == "2":
            print(f"{Fore.CYAN}Great choice!")
            print(f"{Fore.CYAN}The honey is nutritious")
            print(f"{Fore.CYAN}And will give you")
            print(f"{Fore.CYAN}Energy to continue your trip")
        else:
            """
            Lets user know the answer is incorrect
            And takes them to start_game()
            """
            print(f"{Fore.RED}{Back.RED}This is an incorrect answer.")
            time.sleep(2)
            print(f"{Fore.RED}{Back.RED}Taking you to the beginning of the game.")
            time.sleep(4)
            start_game()


def meet_knight():
    print(f"{Fore.CYAN}You walk further along the path")
    print(f"{Fore.CYAN}You see a knight in his shining armour")
    print(f"{Fore.CYAN}Mounted on his black horse\n")
    time.sleep(2)

    print(Fore.CYAN + """ 
     _   _   _   _+       
/_`-'_`-'_`-'_|  \+/  |
\_`M'_`D'_`C'_| _<=>_ |
  `-' `-' `-' 0/ \ / o=o
              \/\ ^ /`0
              | /_^_\
              | || ||
______________|_d|_|b____

    """)

    print(f"{Fore.CYAN}It's the knight's job to maintain law and order")
    print(f"{Fore.CYAN}The knight asks you what you're doing in the forest")
    print(f"{Fore.CYAN}You tell the knight you're trying to get home")
    print(f"{Fore.CYAN}The knight gives you two options\n")
    time.sleep(2)
    print(f"{Fore.CYAN}Option #1: He'll take you to your village")
    print(f"{Fore.CYAN}But you will forever be indebted to him")
    print(f"{Fore.CYAN}The knight is well known where you live")
    print(f"{Fore.CYAN}So there's no chance to escape the debt\n")
    time.sleep(2)
    print(f"{Fore.CYAN}Option #2: The Knight will tell you where to go")
    print(f"{Fore.CYAN}But you need to get there by yourself")
    print(f"{Fore.CYAN}You need to rememeber that it's getting dark")
    print(f"{Fore.CYAN}And there all kinds of wild animals waking up to hunt")

    answer = input(f"{Fore.YELLOW}{Style.BRIGHT}Which option do you chose")
    answer = input(f"{Fore.YELLOW}{Style.BRIGHT}Type 1 or 2")

    if answer == "1":
        print(f"{Fore.CYAN}Great choice!")
        print(f"{Fore.CYAN}The knight takes you to your village")
        print(f"{Fore.CYAN}You thank him for his kindness")
        print(f"{Fore.CYAN}And introduce him to your family")
        print(f"{Fore.CYAN}Your family prepare a feast for you")
        print(f"{Fore.CYAN}To celebrate your safe return")
        print(f"{Fore.CYAN}The knight said you're not indebted to him anymore")
        print(f"{Fore.CYAN}Instead you've become friends!")
        win_game()
        time.sleep(2)
        play_again

    elif answer == "2":
        print(f"{Fore.RED}{Back.RED}This is a bad choice.")
        print(f"{Fore.RED}{Back.RED}It's not a good idea")
        print(f"{Fore.RED}{Back.RED}To walk alone in the forest when it's dark.")
        print(f"{Fore.RED}{Back.RED}You thank the knight for the instructions")
        print(f"{Fore.RED}{Back.RED}And bid him farewell")
        print(f"{Fore.RED}{Back.RED}But a poisonous snake bites you and you die")
        game_over()
        play_again()
    else:
        """
        Let user know the answer is incorrect
        """
        clear_terminal()
        print(f"{Fore.RED}{Back.RED}This is an incorrect answer")
        time.sleep(2)
        answer = input(f"{Fore.RED}{Back.RED}You need to type 1 or 2.\n")
        if answer == "1":
            print(f"{Fore.RED}{Back.RED}This is a bad choice.")
            print(f"{Fore.RED}{Back.RED}It's not a good idea to walk alone")
            print(f"{Fore.RED}{Back.RED}In the forest when it's dark.")
            print(f"{Fore.RED}{Back.RED}You thank the knight for the instructions")
            print(f"{Fore.RED}{Back.RED}And bid him farewell")
            print(f"{Fore.RED}{Back.RED}But a poisonous snake bites you and you die")
            game_over()
            play_again()
        elif answer == "2":
            print(f"{Fore.CYAN}Great choice!")
            print(f"{Fore.CYAN}The knight takes you to your village")
            print(f"{Fore.CYAN}You thank him for his kindness")
            print(f"{Fore.CYAN}And introduce him to your family")
            print(f"{Fore.CYAN}Your family prepare a feast for you")
            print(f"{Fore.CYAN}To celebrate your safe return")
            print(f"{Fore.CYAN}The knight said you're not indebted to him")
            print(f"{Fore.CYAN}Instead you've become friends!")
            win_game()
            time.sleep(2)
            play_again
        else:
            """
            Lets user know the answer is incorrect
            And takes them to start_game()
            """
            print(f"{Fore.RED}{Back.RED}This is an incorrect answer.")
            time.sleep(2)
            print(f"{Fore.RED}{Back.RED}Taking you to the beginning of the game.")
            time.sleep(4)
            start_game()

    
def game_over():
    """
    This function is run when user decides to quit the game
    Or when they lose the game
    """
    print(Fore.RED + Style.BRIGHT + """
    _____                                            _ 
    / ____|                                          | |
    | |  __  __ _ _ __ ___   ___    _____   _____ _ __| |
    | | |_ |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__| |
    | |__| | (_| | | | | | |  __/ | (_) \ V /  __/ |  |_|
    \_____|\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|  (_)

    """)

                                                      
def play_again():
    """
    This function is run when game is over 
    regardless of whether user wins or not
    """

    answer = input(f"{Fore.YELLOW}{Style.BRIGHT}Do you want to play again?\
    Y / N\n").lower()
    if answer == "y":
        clear_terminal()
        start_game()
    elif answer == 'n':
        print(Fore.CYAN + """
                                                                     __ 
 _____ _           _          ___                _         _        |  |
|_   _| |_ ___ ___| |_ ___   |  _|___ ___    ___| |___ _ _|_|___ ___|  |
  | | |   | .'|   | '_|_ -|  |  _| . |  _|  | . | | .'| | | |   | . |__|
  |_| |_|_|__,|_|_|_,_|___|  |_| |___|_|    |  _|_|__,|_  |_|_|_|_  |__|
                                            |_|       |___|     |___|   
    """)  

    else:  
        """
        Let user know the answer is incorrect and takes user to start_game
        """
        print("This is an incorrect answer")
        print("You need to type Y or N")
        print("You will now be directed to the beginning of the game")
        start_game()


def win_game():
    """
    This function lets user know 
    that they won the game
    """
    print(Fore.MAGENTA + """        
        ░█──░█ █▀▀█ █──█ 　 █───█ ─▀─ █▀▀▄ █ 
        ░█▄▄▄█ █──█ █──█ 　 █▄█▄█ ▀█▀ █──█ ▀ 
        ──░█── ▀▀▀▀ ─▀▀▀ 　 ─▀─▀─ ▀▀▀ ▀──▀ ▄             
    """)    
    
        
start_game()
