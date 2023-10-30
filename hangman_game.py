import random

def hangman():
    words = ["apple", "banana", "orange", "grape", "strawberry"]  # Add more words here
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        display = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display += letter
            else:
                display += "_"
        print(display)

        if display == secret_word:
            print("Congratulations! You've guessed the word.")
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in secret_word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess. Attempts left: {attempts}")

    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The word was '{secret_word}'.")

hangman()
