"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""
"""Psuedo-code Hints

When the program starts, we want to:
------------------------------------
1. Display an intro/welcome message to the player.
2. Store a random number as the answer/solution.
3. Continuously prompt the player for a guess.
  a. If the guess greater than the solution, display to the player "It's lower".
  b. If the guess is less than the solution, display to the player "It's higher".

4. Once the guess is correct, stop looping, inform the user they "Got it"
     and show how many attempts it took them to get the correct number.
5. Let the player know the game is ending, or something that indicates the game is over.

( You can add more features/enhancements if you'd like to. )
"""

import random

# Intro Message
def intro_message(score):
    print("***Welcome to the Number Guessing Game!***")
    print("*****************************************************************")
    print("***Instructions: A Random number is selected from the range 1-10.")
    print("You guess a number within that range and see if it is the randomly selected number.\nTry to beat the current record by guessing the number in as few tries as possible!***")
    print("*****************************************************************")
    print(f"The current record breaker for number of guesses is {score} guesses")
    print("*****************************************************************")

# Set Random Number from Range
def get_random_num(num1, num2):
    return random.randrange(num1, num2)

# Ended up writing this code twice so to follow DRY made it into a definition
def initialize_guess():
    return int(input("Please guess a number between 1-10: "))

def start_game():

    # Initialize high score for start game
    high_score = 10

    # intro on start of game
    intro_message(high_score)

    # Get start game's random number
    random_number_selected = get_random_num(1, 10)

    # Here for testing purposes to test random numbers being selected
    # to make sure there are no repeats
    print(random_number_selected)

    # Initialize count of guesses
    count = 0

    # Get first guess
    guess = initialize_guess()

    # While loop to continously ask player for guesses until they get it right
    while True:
        # If the player guesses too high
        if guess > random_number_selected:
            guess = int(input("The number is lower than your guess, please try again: "))
            count += 1
            continue
        # If the player guesses too low
        elif guess < random_number_selected:
            guess = int(input("The number is higher than your guess, please try again: "))
            count += 1
            continue
        # Player guesses right
        elif guess == random_number_selected:
            count += 1
            print(f"Congratulations! You guessed the correct number in {count} guesses!")

            # Check high_score to see if player broke record
            if count < high_score:
                high_score = count
                print(f"You set a new record at {high_score} guesses, Awesome job!")

            # Check if the player wants to play another game
            another_game = input("Do you want to play another game? (yes/no) ")
            if another_game.lower() == "yes":
                # Set new random number and check it does not repeat from last game
                new_random_num = get_random_num(1, 10)
                while True:
                    if new_random_num == random_number_selected:
                        new_random_num = get_random_num(1, 10)
                        continue
                    else:
                        random_number_selected = new_random_num
                        break
                # Get their first guess to start another game and reset count
                count = 0
                print(f"The current record to beat is {high_score}")
                guess = initialize_guess()
                continue
            elif another_game.lower() == "no":
                print("Thank you for playing, Goodbye!")
                break



# Kick off the program by calling the start_game function.
start_game()
