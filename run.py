import gspread #Import entire gspread library
from google.oauth2.service_account import Credentials #import Credentials class from google auth library
from art import * #import all from the art module
from tabulate import tabulate
from words import medium_word_list # import our wordlist from the words.py file
from hangman_stages import stage #import our hangman ascii stages art from the hangman_stage.py
import random

#List of the APIs the program will access.
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json") 
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("hanged_man")

#wins = SHEET.worksheet("Wins")
#scores = wins.get_all_values()
#print(scores)

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

    print("\n\nWelcome to Hangman's Quest!")
    while True:
        USER = input("\nPlease enter your name: ").upper()
        if len(USER) == 0:
            print("You cannot enter a blank name. Please try again.")
        else:
            break
    tprint(f"\nWelcome   to     the     game   {USER}!")
    return USER


def main_menu(USER):
    """This function comprises the main menu. From here the user can select 
    the option to view the game rules, or the option to start the game itself"
    """
    print("""\nSelect from either option below:
    1. Game Rules
    2. Start Game
    """)
    choice = input("Enter key: ")
    while True:
        if choice == '1':
            tprint("\n\nGAME RULES")
            print(f"ALRIGHT {USER}, LISTEN UP CAREFULLY...THE RULES ARE AS FOLLOWS:\n")
            read_txt_file("game_rules.txt")
            break
        elif choice == '2':
            break
        else:
            print('Please enter either "1" or "2"')
            choice = input("Enter key: ")
            
    print ("\n\nNOW LET'S PLAY HANGMAN!")
            

def get_random_word():
    """This function pulls a randomized word from the word list
    and creates ann obscured variant of that word using dashes
    Both the randomized word and its hidden equivalent are then return.
    """
    random_word = random.choice(medium_word_list)
    hidden_word = "-" * len(random_word)
    return random_word, hidden_word

def play_game(word, hidden, streak):
    """This function takes two arguments; the random word and its hidden variant.
    The function uses if statements, and for loops, to control the flow of data and
    makes logical decisions in regards to correct and incorrect user guesses.
    """
    guessed = False
    lives = 6
    wrong_guess = []
    correct_guess = []
    print(display_hangman_stage(lives))
    print()
    print(hidden)
    print(word)

    while not guessed and lives > 0:
        user_guess = input("\nEnter your guess: ")

        if len(user_guess) == 1 and user_guess.isalpha():
            if user_guess in correct_guess or user_guess in wrong_guess:
                print("Letter already guessed. Please try another.")
                continue

            if user_guess in word:
                hidden = ""
                print("\n\n\n\n\n\nThat letter is in the word!\n")
                correct_guess.append(user_guess)
                print(f"Current lives remaining: {lives}")
                print(f"Incorrect guesses: {wrong_guess}")
                for letter in word:
                    if letter in correct_guess:
                        hidden += letter
                    else:
                        hidden += "_"
                if hidden == word:
                    guessed = True
            else:
                print("\n\n\n\n\n\nThat letter is not in the word....\n")
                lives -= 1
                if user_guess not in wrong_guess:
                    wrong_guess.append(user_guess)
                print(f"Current lives remaining: {lives}")
                print(f"Incorrect guesses: {wrong_guess}")

            print(display_hangman_stage(lives))
            print()
            print(hidden)
        else:
            print("Invalid entry: Only single alphabetical characters are accepted.")

        if lives == 0:
            print(f"""\nYou have lost...
The word was {word}""")
            streak = 0
        elif lives > 0 and guessed is True:
            print("Congratulations! you have discovered the word!")
            streak += 1
    return streak
    


def display_hangman_stage(lives):
    """This function returns the reversed order 
       of the hang_stages file when called on.
    """
    return stage[::-1][lives]

def update_wins_worksheet(USER, streak):
    print("Updating your score...")
    wins_worksheet = SHEET.worksheet("Wins")
    wins_worksheet.append_row([USER, streak])
    print("Update successful!")


def display_wins_worksheet():
    scores = SHEET.worksheet("Wins").get_all_values()
    print(tabulate(scores, headers="firstrow", numalign="center", tablefmt="heavy_grid"))

def main():
    USER = welcome_screen()
    streak = 0
    main_menu(USER)
    while True:
        retrieved_random_word, retrieved_hidden_word = get_random_word()
        streak = (play_game(retrieved_random_word, retrieved_hidden_word, streak))
        end = input(print("Play again?"))
        if end == "Y":
            continue
        else:
            update_wins_worksheet(USER, streak)
            break
#main()

display_wins_worksheet()





