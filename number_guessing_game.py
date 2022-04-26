"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
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
    # write your code inside this function.

    # Intro Message and high score
    high_score = 10
    print("***Welcome to the Number Guessing Game!***")
    print("Instructions: A Random number is selected from the range 1-10.")
	print("You guess a number within that range and try your best to guess the random number. Try your best to beat the high score!")
	print("*****************************************************************")
	print(f"The current record breaker for number of guesses is {high_score}")
	print("*****************************************************************")

    # set random number
	random_number_selected = random.randrange(1, 10)

    # Here for testing purposes to test random numbers being selected
	print(random_number_selected)

    # While loop to continously ask player for guesses until they get it right
	while True:
    	count = 0
    	guess = int(input("Please guess a number between the range you selected: "))

    	if guess > random_number_selected:
            guess = int(input("The number is lower than your guess, please try again: "))
            count += 1
        elif guess < random_number_selected:
            guess = int(input("The number is higher than your guess, please try again: "))
            count += 1
        elif guess == random_number_selected:
            print(f"Congratulations! You guessed the correct number in {count} guesses!")
			#Check high score against count
			if count < high_score:
				print("You set a new record!")
				high_score = count
				print(f"the new record is {high_score}!")
				break
			else:
				break



# Kick off the program by calling the start_game function.
start_game()
# Ask for another game or End it
another_game = input("Do you want to play another game? (yes/no) ")
if another_game.lower() == "yes":
	start_game()
elif another_game.lower() == "no":
	print("Thank you for playing, Goodbye!")
