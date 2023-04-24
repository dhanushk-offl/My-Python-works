#---------------> Coded by Dhanush <---- 
#A game named Hangout (Word guessing and finding game) using the def function of python
import random

# A list of words to choose from (I give example name of cricketers)
words = ["Dhoni", "Kholi", "Pandiya", "Jadeja", "Rahane", "Gaikwad", "Rohit", "Pant"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(words)
# Function to play the game
def play(word):
    # Create a list of underscores with the same length as the word
    display = ["_" for letter in word]
    # Convert the list to a string
    display_word = "".join(display)
    # List to store the guessed letters
    guessed_letters = []
    # Counter for the number of incorrect guesses
    incorrect_guesses = 0
    # Maximum number of incorrect guesses allowed
    max_incorrect_guesses = 6

    # Loop until the word is guessed or the maximum number of incorrect guesses is reached
    while display_word != word and incorrect_guesses < max_incorrect_guesses:
        print(f"Word: {display_word}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        # Prompt the user to guess a letter
        guess = input("Guess a letter: ").lower()

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter!")
        # Check if the letter is in the word
        elif guess in word:
            # Update the display word with the guessed letter(s)
            for i, letter in enumerate(word):
                if letter == guess:
                    display[i] = letter
            display_word = "".join(display)
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print("Sorry, that letter is not in the word.")

        # Add the guessed letter to the list of guessed letters
        guessed_letters.append(guess)

    # Check if the word was guessed or the maximum number of incorrect guesses was reached
    if display_word == word:
        print(f"Congratulations, you guessed the Cricketer's name '{word}'!")
    else:
        print(f"Sorry, you ran out of guesses. The word was '{word}'.")

# Main function to start the game
def main():
    print("Vankkam da Mapla! Welcome to Hangman Game for Cricketers!  Valalama..")
    word = choose_word()
    play(word)

# Call the main function to start the game
if __name__ == "__main__":
    main()
