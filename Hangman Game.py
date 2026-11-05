import random

# List of 5 predefined words
words = ["apple", "banana", "mango", "orange", "grapes", "papaya"]

# Randomly choose one word
word = random.choice(words)

# Store the letters guessed by the player
guessed_letters = []

# Maximum number of incorrect guesses
max_wrong_guesses = 6

# Count incorrect guesses
wrong_guesses = 0

print("Welcome to the Hangman Game!")
print("Guess the word one letter at a time.")
print("You can make a maximum of 6 incorrect guesses.")

# Game loop
while wrong_guesses < max_wrong_guesses:
    
    # Display the word with guessed letters
    display = " ".join(letter if letter in guessed_letters else "_" for letter in word)

    print("\nWord:", display)
    print(f"Wrong guesses: {wrong_guesses}/{max_wrong_guesses}")

    # Check if the whole word has been guessed
    if "_" not in display:
        print("Congratulations! You won!")
        print("The word was:", word)
        break

    # Ask the player for a letter
    guess = input("Guess a letter: ").lower()

    # Ckeck whether the input is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add the guess to guessed letter
    guessed_letters.append(guess)

    # Check whether the guessed letter is in the word
    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

# If the player uses all 6 incorrect guesses
else:
    print("\nGame over!")
    print("The word was:", word)    
