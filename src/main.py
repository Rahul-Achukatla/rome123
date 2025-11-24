import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Guess a number between 1 and 100 (or 'q' to quit): ")

        if guess.lower() == 'q':
            print("Goodbye!")
            break

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            break

number_guessing_game()
