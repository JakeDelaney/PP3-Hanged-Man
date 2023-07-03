from art import * #import all from the art module
from words import medium_word_list
import random

def welcome_screen_art():
    """This function displays an ascii welcome logo and art piece.
    The skull art is stored in a seperate text file and is called
    using the open function. A for loop is used to iterate over each line
    and print the contents into the run.py file.
    """
    tprint("Hangman's Quest!")
    with open("ascii_skull.txt", "r") as file:
        for line in file:
            print(line, end="")

def main_menu(choice):
    """This function comprises the main menu. From here the user can select 
    the option to view the game rules, or the option to start the game itself"
    """
    while True:
        if choice == '1':
            display_rules()
            break
        elif choice == '2':
            #start_game()
            break
        else:
            print('Please enter either "1" or "2"')
            choice = input("Enter key: ")

def display_rules():
    """This function displays game rules and information when called.
       The function also refers to the user by their name.
    """
    tprint("\n\nGAME RULES")
    print(f"""  ALRIGHT {USER}, LISTEN UP CAREFULLY...THE RULES ARE AS FOLLOWS:
        
    1. The game begins with a hidden word, each letter within this word is represented by a dash.
    2. Your objective is to guess the hidden word correctly by suggesting letters one at a time.
    3. If you correctly guess a letter in the hidden, all instances of that letter are revealed.
    4. If you guess an incorrect letter, you receive a strike, and one of the hanged man's body parts is revealed.
    5. You have a total of 6 guesses, failing to reveal the word within 6 tries will result in a loss.
""")
            
def get_random_word():
    random_word = random.choice(medium_word_list)
    hidden_word = "-" * len(random_word)
    return hidden_word

def main():
    welcome_screen_art()
    print("\n\nWelcome to Hangman's Quest!")
    global USER
    USER = input(str("Please enter your name: ")).upper()
    print(f"\nWelcome to the game {USER}!")
    print("""\nSelect from either option below:
    1. Game Rules
    2. Start Game
    """)
    menu_choice = input("Enter key: ")
    main_menu(menu_choice)
    retrieved_word = get_random_word()

#main()
retrieved_word = get_random_word()
print(retrieved_word)


