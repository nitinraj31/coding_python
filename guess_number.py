# Build a terminal game where the user guesses a random number . Practice loops and conditions .

import random
def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Welcome to the Guess the Number Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while not guessed:
        user_input = input("Enter your guess (or type 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print(f"The number was {number_to_guess}. Thanks for playing!")
            break
        
        try:
            user_guess = int(user_input)
            attempts += 1
            
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")
                