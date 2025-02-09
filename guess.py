import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guess = None

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while guess != number_to_guess:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")

    print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")

number_guessing_game()
