''' Little Linux Assistant Minigames Library
         * * * * * * * * * * * * * * 
    This is a library that is going to contain some minigames. 
    Each game will be a function that can be imported into files. '''
import os as sh 
import random 
from sources import * 
# * * * * * * * * * * * * * *
# functions
# * * * * * * * * * * * * * *
def sleeping_machines():
    slpm = 'sleep 1'
    sh.system(slpm) 
def guess_the_number():
    ''' This function represents a "Guess the Number" game that can be imported and played. 
        The program will assign a random number between 1-10 to a var called "randomNum".
        A var, "gameCounter", will go up by one each time the player takes a turn. 
        The player will have 3 chances to guess the number until the Game Counter runs out.'''
    gameCounter = 1 # gameCounter starts at 1, can go up and down 
    g1 = "Welcome to Guess the Number!"
    title = f'cowsay "Guess The Numbers Game with {asstName} and {userName}!"'
    r1 = "I'm going to choose a random number, then you get three turns to guess it!" 
    r2 = "Ready to get started? Types 'Yes' or 'No' to get going!\n"
    sh.system(title) 
    sleeping_machines()
    print(r1)
    sleeping_machines()
    gameStart = input(r2) 
    # now we need to define a few functions real quick that will run depending on the gameStart var
    gcStatus = "Current Game Counter Status" # var for displaying current point status
    def countChecker():
        if (gameCounter == 3):
            print("Your Game Counter has went over 3. You lose.")
            sleeping_machines()
            print("Exiting...")
            sleeping_machines()
            exit()
        elif (gameCounter == 0):
            print("Your Game Counter has reached zero. You lose.")
            sleeping_machines()
            print("Exiting...")
            sleeping_machines()
            exit()
        else:
            pass
    def gcUp(): # it means 'game counter up', sends gameCounter up one int
        gameCounter += 1
        gcNotify = 'notify-send "Little Linux Assistant" "The GameCounter increased by one."'
        print(f'{gcStatus}: {gameCounter}')
        sh.system(gcNotify)
        countChecker()  # run countChecker to eval score
    def gcDown(): # it means 'game counter down', sends gameCounter down one int
        gameCounter -= 1
        gcNotify2 = 'notify-send "Little Linux Assistant" "The GameCounter decreased by one."'
        print(f'{gcStatus}: {gameCounter}')
        sh.system(gcNotify2)
        countChecker() # run countChecker to eval score
    ##########################################################
    ''' We need to make a function for the game logic. 
    It will run if the user selects 'Yes' to the above.
    A random number var should be set to randomNum. 
    gameCounter should be increased or decreased each turn. 
    Coming back to work on this part soon. '''
    ##########################################################
    # def game_logic:
         # statements
    if (gameStart == "Yes"):
        # insert logic here later. 
        # we will probably need a function for the actual gameplay. 
        # that function would be invoked here, since the user said "yes" to playing.
        gameOn = "Alright, let's get started!" 
        print(gameOn)  
    elif (gameStart == "No"):
        gs1, gs2 = "Okay, no problem.", "Exiting..." 
        print(gs1)
        sleeping_machines()
        print(gs2)
        sleeping_machines()
        exit()
    else:
        invalidKey = "Invalid key pressed. Exiting." 
        print(invalidKey)
        sleeping_machines()
        exit()
# add things here so they are protected from being ran on import until called 
if __name__ == '__main__':
    guess_the_number()
''' NOTES:
  **********
  We're not done with this library yet - gonna be adding some more games over time. 
  Some code might be incomplete. I just startd this library and wanted to save it. 
  If something is incomplete, feel free to let me know or submit a PR if you want to fix it! :) '''