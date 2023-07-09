# Import statements for external libraries and modules
import gspread
import random
import sys
from google.oauth2.service_account import Credentials
from art import *
from tabulate import tabulate
from words import word_list
from hangman_stages import stage

# List of the APIs the program will access.
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
# Variables used to store credentials for API authorization
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("hanged_man")


def read_txt_file(text):
    """Function opens a text file,
       and iterates through each line of the file.
       Content of the file is then printed out to the terminal.
    """
    try:
        with open(text, "r") as file:
            for line in file:
                print(line, end="")
            print()
    except FileNotFoundError:
        print(f"File {text} not found.")


def welcome_screen():
    """Function displays an ascii welcome logo and art piece using
    read_txt_file() and tprint. User is prompted to enter a username,
    which is then returned.
    """
    tprint("""Hangman's 
    Quest!""")
    read_txt_file("ascii_skull.txt")

    print("\n\nWelcome to Hangman's Quest!")
    while True:
        USER = input("\nPlease enter your name: \n").upper()
        if len(USER) == 0:
            print("You cannot enter a blank name. Please try again.")
        else:
            break
    tprint(f"""\nWelcome  
    {USER}!""")
    return USER


def main_menu(USER):
    """Function comprises the main menu. From here the user can select
    the option to view the game rules, start the game,
    or view the current scoreboard"
    """
    while True:
        print("""\nSelect from either option below:
1. Game Rules
2. Start Game
3. Show Scoreboard
4. Exit Game
        """)
        choice = input("Enter key: \n")

        if choice == '1':
            tprint("\nGAME RULES")
            print(f"""ALRIGHT {USER}, THE RULES ARE AS FOLLOWS:\n""")
            read_txt_file("game_rules.txt")
            continue
        elif choice == '2':
            break
        elif choice == '3':
            tprint("\nSCOREBOARD")
            display_wins_worksheet()
            continue
        elif choice == '4':
            sys.exit(f"""\nTHANKS FOR PLAYING {USER}!
GOODBYE.\n""")
        else:
            print('Please enter either "1", "2", "3" or "4"')
    print("\nNOW LET'S PLAY HANGMAN!")


def get_random_word():
    """Function pulls a randomized word from the word list
    and creates an obscured variant of word using dashes
    Both word and its hidden variant are returned.
    """
    random_word = random.choice(word_list)
    hidden_word = "-" * len(random_word)
    return random_word, hidden_word


def play_game(word, hidden, streak):
    """Function takes three arguments;
    random word and its hidden variant from get_random_word()
    Streak argument tracks successive player wins.
    If statements, and for loops, are used
    to control the flow of data and make
    logical decisions for correct or incorrect user guesses.
    """
    guessed = False
    lives = 6
    wrong_guess = []
    correct_guess = []
    print(display_hangman_stage(lives))
    print()
    print(hidden)

    # Run while the word has not been guessed, and the lives are greater than 0
    while not guessed and lives > 0:
        user_guess = input("\nEnter your guess: \n").lower()

        # Run if the user guess is a single alphabetical character
        if len(user_guess) == 1 and user_guess.isalpha():
            if user_guess in correct_guess or user_guess in wrong_guess:
                print("\nLetter already guessed. Please try another.")
                continue

            # Run if the user guesses correctly
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

            # Run if user guessed incorrectly
            else:
                print("\n\n\nThat letter is not in the word...\n")
                lives -= 1
                if user_guess not in wrong_guess:
                    wrong_guess.append(user_guess)
                print(f"Current lives remaining: {lives}")
                print(f"Incorrect guesses: {wrong_guess}")

            print(display_hangman_stage(lives))
            print()
            print(hidden)
        else:
            print("""\nNo blank entries, and single alphabetical characters only.
Please try again.""")

        if lives == 0:
            print(f"""\nYou have lost...
The word was: {word.upper()}""")
            streak = 0
        elif lives > 0 and guessed is True:
            print(f"""\nCongratulations! you have revealed the word!
The word was: {word.upper()}""")
            streak += 1
    return streak


def display_hangman_stage(lives):
    """Function returns the reversed order
       of the hang_stages.py file when called on.
    """
    return stage[::-1][lives]


def update_wins_worksheet(USER, streak):
    """Function appends the values stored within
    the USER and streak variables, and uploads them
    to the google drive worksheet
    """
    print("Updating your score...")
    try:
        wins_worksheet = SHEET.worksheet("Wins")
        wins_worksheet.append_row([USER, streak])
        print("Update successful!")
    except Exception as e:
        print(f"An error occurred while updating the score: {e}")


def display_wins_worksheet():
    """Function pulls data from the google drive worksheet.
    Data is formated with tabulate and printed to terminal
    to display the latest user scores.
    """
    try:
        scores = SHEET.worksheet("Wins").get_all_values()
        print(tabulate(
            scores, headers="firstrow", numalign="center", tablefmt="heavy_grid"))
    except Exception as e:
        print(f"An error occurred while displaying the scoreboard: {e}")


def main():
    """
    The main program function. Adhering to best pratices,
    this function contains all other central functions, as nested functions.
    From here these nested functions are called on when required.
    """
    USER = welcome_screen()
    streak = 0
    main_menu(USER)
    while True:
        retrieved_random_word, retrieved_hidden_word = get_random_word()
        streak = (play_game(
            retrieved_random_word, retrieved_hidden_word, streak))
        print("""\nEnd of the road...please choose from either option below:
1. Play again
2. Exit to main menu (THIS WILL RESET YOUR STREAK)""")
        while True:
            choice = input("\nEnter key: \n")
            if choice == "1":
                break
            elif choice == "2":
                update_wins_worksheet(USER, streak)
                streak = 0
                main_menu(USER)
                break
            else:
                print('\nPlease enter either "1" or "2"')
                continue


main()
