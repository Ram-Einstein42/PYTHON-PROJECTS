import random

# Generate a number between 1 and 100
number_to_guess = random.randint(1, 100)

# Tracking the number of guesses
attempts = 0

while True:
    user_guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1

    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        break
    # Provide hints at specific attempts
    if attempts >= 10:
        print(f"You've used all your attempts. The number was {number_to_guess}.")
        break
    elif attempts == 5:
        print("Hint: The number is even." if number_to_guess % 2 == 0 else "Hint: The number is odd.")
    elif attempts == 3:
        print("Hint: The number is greater than 50." if number_to_guess > 50 else "Hint: The number is 50 or less.")
    
    
