import random

def choose_word():
    words = ["python", "hangman", "programming", "developer", "coding", "challenge", "intern"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    max_attempts = 6
    word_to_guess = choose_word().lower()
    guessed_letters = []
    incorrect_attempts = 0

    print("**WELCOME TO HANGMAN**!")
    
    while True:
        print("\nWord:", display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You've already guessed that letter. Try again.")
            elif guess in word_to_guess:
                print("Good guess🤩!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess😞.")
                incorrect_attempts += 1
                guessed_letters.append(guess)

            if set(word_to_guess) == set(guessed_letters):
                print("\nCongratulations! You guessed the word:", word_to_guess)
                print("The word is:",word_to_guess)
                break
            elif incorrect_attempts == max_attempts:
                print("\nSorry, you've reached the maximum number of incorrect attempts.")
                print("The word was:", word_to_guess)
                break
        else:
            print("Invalid input. Please enter a single letter.")

if __name__ == "__main__":
    hangman()
