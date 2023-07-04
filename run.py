from art import * #import all from the art module
from words import medium_word_list # import our wordlist from the words.py file
import random


def read_txt_file(text):
    """This function open a text file, and iterates through each line of the file.
       The content of this file are then printed out to the terminal.
    """
    with open(text, "r") as file: 
        for line in file:
            print(line, end="")
        print()


def welcome_screen():
    """This function displays an ascii welcome logo and art piece.
    The skull art is stored in a seperate text file and is called
    using the open function. A for loop is used to iterate over each line
    and print the contents into the run.py file.
    """
    tprint("Hangman's Quest!")
    read_txt_file("ascii_skull.txt")


def main_menu(choice, USER):
    """This function comprises the main menu. From here the user can select 
    the option to view the game rules, or the option to start the game itself"
    """
    while True:
        if choice == '1':
            tprint("\n\nGAME RULES")
            print(f"ALRIGHT {USER}, LISTEN UP CAREFULLY...THE RULES ARE AS FOLLOWS:\n")
            read_txt_file("game_rules.txt")
            break
        elif choice == '2':
            get_random_word()
            break
        else:
            print('Please enter either "1" or "2"')
            choice = input("Enter key: ")
            

def get_random_word():
    """This function pulls a randomized word from the word list
    and creates ann obscured variant of that word using dashes
    Both the randomized word and its hidden equivalent are then return.
    """
    random_word = random.choice(medium_word_list)
    hidden_word = "-" * len(random_word)
    return random_word, hidden_word


def main():
    welcome_screen()
    print("\n\nWelcome to Hangman's Quest!")
    USER = input(str("Please enter your name: ")).upper()
    print(f"\nWelcome to the game {USER}!")
    print("""\nSelect from either option below:
    1. Game Rules
    2. Start Game
    """)
    menu_choice = input("Enter key: ")
    main_menu(menu_choice, USER)

    retrieved_random_word, retrieved_hidden_word = get_random_word()
    print (retrieved_hidden_word)
    print (retrieved_random_word)

main()




