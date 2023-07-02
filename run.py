from art import * #import all from the art module

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

def main():
    welcome_screen_art()
    print("\n\nWelcome to Hangman's Quest!")
    USER = input(str("Please enter your name: "))
    print(f"Welcome to the game {USER}!")

main()
