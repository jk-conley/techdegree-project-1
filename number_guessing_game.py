"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
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

# Validates guess and handles exceptions
def initialize_guess(msg_to_user):
    while True:
        try:
            ini_guess = int(input(msg_to_user))
            validate_number_range(ini_guess)
            break
        except ValueError:
            print("Not a valid value, please use a number between 1-10")
    return ini_guess

# Checks Number Range and Validates
def validate_number_range(user_guess):
    if user_guess < 1 or user_guess > 10:
        raise ValueError

# Starts and runs the game
def start_game():

    # Initialize high score for start game
    high_score = 10

    # intro on start of game
    intro_message(high_score)

    # Get start game's random number
    random_number_selected = get_random_num(1, 10)

    # Here for testing purposes
    print(random_number_selected)

    # Initialize count of guesses
    count = 0

    # Get first guess
    guess = initialize_guess("Please guess a number between 1-10: ")

    # While loop to continously ask player for guesses until they get it right
    while True:
        # If the player guesses too high and check if guess is within range
        if guess > random_number_selected:
            guess = initialize_guess("The number is lower than your guess, please try again: ")
            count += 1
            continue
        # If the player guesses too low
        elif guess < random_number_selected:
            guess = initialize_guess("The number is higher than your guess, please try again: ")
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
            while True:
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
                    guess = initialize_guess("Please guess a number between 1-10: ")
                    continue
                elif another_game.lower() == "no":
                    print("Thank you for playing, Goodbye!")
                    break
                else:
                    print("That is not valid, please use yes or no")
                    continue



# Kick off the program by calling the start_game function.
start_game()
