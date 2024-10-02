import random

def guessing_game():
    # Step 1: Choose a random number between 1 and 10
    number_to_guess = random.randint(1, 10)
    attempts = 3  # User has 3 attempts to guess the number

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 10. You have 3 chances to guess it!")

    # Step 2: Game loop with 3 attempts
    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))

        # Step 3: Check the user's guess using conditional statements
        if guess == number_to_guess:
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly!")
            break
        elif guess < number_to_guess:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        
        # Check if it's the last attempt
        if attempt == attempts:
            print(f"Sorry, you've used all your attempts. The correct number was {number_to_guess}.")

# Step 4: Test the game
guessing_game()
