# Hangman's Quest
"Hangman's Quest" is a Python-coded game that brings the classic word-guessing experience to life through a command line interface. This text-based game offers an engaging challenge for players of all ages.

Hangman is a game that has entertained and challenged players for generations. It tests your vocabulary knowledge, word recognition, and deductive reasoning skills. It's a simple yet addictive game that can be enjoyed by players of all ages.

The game is built using Python programming language, showcasing its versatility and power in creating interactive experiences. The command line interface provides a straightforward and intuitive way to play, without the need for complex graphics or fancy visuals.

![image](https://github.com/JakeDelaney/PP3-Hanged-Man/assets/76518393/5e8d0c2f-c2e5-42e3-9cd7-e0e4ca664ee3)

<br>

## Table of Contents
 * User Experience (UX)
 * Features
 * Technologies Used
 * Testing
 * Deployment
 * Credits

<br>

## User Experience (UX)
* **First Time Visitor Goals**
  * As a first time visitor, I want to enter a username into the program, and have that name referenced throughout.
  * As a first time visitor, I would like to navigate through the program using an intuitive menu.
  * As a first time visitor, I would like any invalid data entries of mine that may crash the program, to be handled and prevented.
  * As a first time visitor, I would like to view the rules relating to the program.
  * As a first time visitor, I would like my see how many attempts I have left at guessing, and how many incorrect words I have guessed so far.
  * As a first time visitor, I would like the program to query If I am finished playing after each word reveal.

* **Returning Visitor Goals**
  * As a returning visitor, I would like to receive a randomly selected word from the program.
  * As a returning visitor, I would like my score to be tracked and displayed within a scoreboard for viewing.
  * As a returning visitor, I would like to improve my knowledge of word guessing through repeated error free use.

* **Frequent User**
  * As a frequent user, I would like to access the scoreboard for long term comparisons of my word knowledge.
  * As a frequent user, I would like an enjoyable and easy experience that encourages repeated use of the program.
  * As a frequent user, I would like to improve my overall skillset and competency for hangman related games.

<br>

## Features
### Welcome Page
The user is welcomed to the program through an ascii banner displaying the game name, and an ascii art piece of a skeleton skull.
It is at the welcome page that the user is also prompted to enter a username. The username name prompt will accept both alphanumeric, and special characters.

![image](https://github.com/JakeDelaney/PP3-Hanged-Man/assets/76518393/8474b6da-b39b-4ec0-8df1-f1048af8b5f7)

<br>

### Main Menu
After entering a username, the user is immediately transported to the main menu, and their entered name is displayed in enlarged ascii text.
There are 4 options the users can choose from:
1. Game Rules
2. Start Game
3. Show Scoreboard
4. Exit Game

![image](https://github.com/JakeDelaney/PP3-Hanged-Man/assets/76518393/d4584272-0f26-4b01-a540-af105c4d0aeb)

<br>

### Game Rules
Selecting the 'Game Rules' option will pull the rules from a seperate 'game_rules.txt' file and print them to the terminal. 
The program will also loop back to the start of the main menu function and request another input (this is done for every option.)

![image](https://github.com/JakeDelaney/PP3-Hanged-Man/assets/76518393/894184ea-1d98-4967-b616-4fd7b1be28d7)

<br>

### Start Game
The 'Start Game' option calls the the play_game function and begins the main game loop. Here the initial ascii hanging pole from the 'hangmang_stages.py' file is pulled and printed.
A random word is also pulled from the wordlist, obfuscated, and then displayed beneath the ascii hangman art.

Once the user has entered a single alphabetical character (I.e made their guess,) the lives variable and wrong_guess list are displayed to aid the user in keeping track of their current progress.

![image](https://github.com/JakeDelaney/PP3-Hanged-Man/assets/76518393/8925e99a-a8e6-4307-b11a-b1c48aa84909)

<br>

### Scoreboard

Choosing the 'Scoreboard' option will display a list of all previous users, and their highest 'streak' acheived. The streak values represents how many successive reveals the users has had without failing. If the user fails to reveal a word, the streak variable is reset to 0.

![image](https://github.com/JakeDelaney/PP3-Hanged-Man/assets/76518393/57294d6a-a01e-4d5b-ad8f-c04611b22706)

<br>

### Exit Game
Selecting the 'Exit Game' option will terminate the program, and will also display a final goodbye message directed towards the user.

![image](https://github.com/JakeDelaney/PP3-Hanged-Man/assets/76518393/2aa74972-f67c-496b-ad1d-f4662713ad0f)

<br>


### Future features to implement
* Lorem ipsum

<br>

## Testing
### Identified bugs

<br>
 
 ## Credits
 ### Technologies Used
* Python
     
 ### Code
 
 ### Applications
 
 ### Acknowledgements
* My tutor Derek McCaudley for guidance during the project.
