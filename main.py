import random

# This function plays a single round of the game
def play_round():
  # Generate a random number between 1 and 100
  secret_number = random.randint(1, 100)
  
  # Ask the user to guess the number
  guess = int(input("Guess a number between 1 and 100: "))
  
  # Keep track of the number of guesses
  guesses = 1
  
  # Keep guessing until the user gets it right
  while guess != secret_number:
    # If the guess is too low, tell the user to guess higher
    if guess < secret_number:
      print("Guess higher.")
    # If the guess is too high, tell the user to guess lower
    else:
      print("Guess lower.")
      
    # Get the user's next guess
    guess = int(input("Guess a number between 1 and 100: "))
    
    # Increment the number of guesses
    guesses += 1
  
  # If the user has guessed the number, congratulate them
  print(f"Congratulations! You guessed the number in {guesses} guesses.")

# Play 5 rounds of the game
for i in range(5):
  play_round()
