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

main()
