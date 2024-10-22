import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100
    target_number = random.randint(lower_bound, upper_bound)
    
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
            attempts += 1
            
            if guess < lower_bound or guess > upper_bound:
                print(f"Please guess a number within the range of {lower_bound} to {upper_bound}.")
            elif guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
    if attempts == max_attempts:
        print(f"Sorry! You've used all your attempts. The number was {target_number}.")

if __name__ == "__main__":
    number_guessing_game()
