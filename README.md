# Hangman's Quest
"Hangman's Quest" is a Python-coded game that brings the classic word-guessing experience to life through a command line interface. This text-based game offers an engaging challenge for players of all ages.

Hangman is a game that has entertained and challenged players for generations. It tests your vocabulary knowledge, word recognition, and deductive reasoning skills. It's a simple yet addictive game that can be enjoyed by players of all ages.

The game is built using Python programming language, showcasing its versatility and power in creating interactive experiences. The command line interface provides a straightforward and intuitive way to play, without the need for complex graphics or fancy visuals.

![image](https://github.com/JakeDelaney/PP3-Hanged-Man/assets/76518393/4773b0f0-60ef-4cf6-9edd-dac9af1b4351)

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

## Design
### Flowchart

The below flowchart was created prior to the development of the application. This flowchart was used to serve as a foundation for the final deployed project.
With the exception of some minor changes brought about due to scope increase, the final project does largely mirror the data flow and structure depicted within the flowchart.

![Blank board](https://github.com/JakeDelaney/PP3-Hanged-Man/assets/76518393/603a695b-ae65-477e-b9eb-91f50f9a7665)

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

The program also includes support for Google Drive API, which allows for the import/export of the 'user'and 'streak' values to an external spreadsheet named 'hanged_man.' This spreadsheet is stored within a google drive account.
Whenever the scoreboard is shown to the user, the values have been imported from this sheet.

![image](https://github.com/JakeDelaney/PP3-Hanged-Man/assets/76518393/24c30cfa-4d3e-4cb2-a54c-fecd3eb75742)

<br>

### Exit Game
Selecting the 'Exit Game' option will terminate the program, and will also display a final goodbye message directed towards the user.

![image](https://github.com/JakeDelaney/PP3-Hanged-Man/assets/76518393/2aa74972-f67c-496b-ad1d-f4662713ad0f)

<br>

### Future features to implement
* Importing additional libraries to implement colour and animations within the program.
* Including more ascii art when appropriate to improve the user experience and emotional reponse
* An option for the user to select program difficulty, this in turn will decide the length/complexity of the words they must guess.
* Some form of multiplayer mode that allows two users to take turns guessing words, and updating their scores individually.
* The ability to allow the user to select specific words from the word list that they wish to encounter while playing

<br>

## Testing
### Program Functionality

The below tests were carried out to verify the functionality of the program. All tests carried out received a passing grade, and all applications functions have been confirmed as working.

![image](https://github.com/JakeDelaney/PP3-Hanged-Man/assets/76518393/c3226158-7a19-45fa-9e75-76150e725f80)

<br>

### CI Python Linter Validator

The run.py file of the program was validated through the CI Python Linter Validator. During this test, no outstanding issues were found.

![image](https://github.com/JakeDelaney/PP3-Hanged-Man/assets/76518393/13b35641-c942-4611-9a3b-c38a8d281dab)

<br>

### Identified bugs

Several bugs were recorded during the development of the application. A record of these bugs can be found in the below table.

![image](https://github.com/JakeDelaney/PP3-Hanged-Man/assets/76518393/330c69a9-f9d9-4241-9424-37bcd35da9dd)

<br>

## Deployment

### How to deploy this site

* Navigate to the Heroku dashboard and click "New" in the top right corner.
* Choose "Create New App" from the drop-down menu.
* Provide a name for the appe (must be uniqure) and select a region.
* Click the option to "Create App."
* Navigate to the project's Deploy Tab, go to Settings and scroll down to Config Vars.
* Click "Reveal Config Vars" and add "CREDS" as the Key and the contents of the "creds.json" file as the value.
* Scroll down to the Build pack section, click "Add Build pack," select "Python," and "Node.js" and save.
* Return to the top of the page and go to the Deploy tab.
* Choose GitHub as the deployment method and confirm the connection.
* Search for the repository name and click "Connect."
* Scroll to the bottom of the deploy page and select the preferred deployment type.
* choose "Enable Automatic Deploys" which will  automatically build/rebuild the deployment when commits are pushed to the repository.

### How to clone this site
* Navigate to the main page of the desired repository.
* Click the "Code" option above the list of files.
* Copy the repository URL, and then open up Git Bash.
* Change the current working directory to a location for the cloned directory.
* Enter the command 'git clone' and paste the copied URL.
* Press enter to create a local clone.

<br>
 
 ## Credits
 ### Technologies Used
* Python

 ### Code
 * "Love Sandwhiches" project ------ for help with Google Drive API and Google auth credentials
 * art==6.0 ------ library for ascii message banners
 * https://ascii.co.uk/art/skulls ------ for the ascii skull image
 * https://www.freecodecamp.org/news/how-to-read-a-file-line-by-line-in-python/ ------ for iterating and printing through text files
 * https://pypi.org/project/tabulate/ ---------- For understanding the tabulate library
 * https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c ---------- ascii hangman art stages
 
 ### Applications / Libraries
* Gitpod for the development environment.
* Git for version control.
* Github for file and website hosting.
* lucidspark for the flowchart
* art==6.0
* cachetools==5.3.1
* google-auth==2.21.0
* google-auth-oauthlib==1.0.0
* gspread==5.10.0
* oauthlib==3.2.2
* pyasn1==0.5.0
* pyasn1-modules==0.3.0
* requests-oauthlib==1.3.1
* rsa==4.9
* tabulate==0.9.0
 
 ### Acknowledgements
* My tutor Derek McCaudley for his support during the course
