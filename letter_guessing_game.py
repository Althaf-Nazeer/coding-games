def letter_guessing_game():
    secret_word = "python"
    guessed_letters = []
    attempts = 6

    print("Welcome to Letter Guessing Game!")
    print(f"The word has {len(secret_word)} letters.")
    
    while attempts > 0 and not all(letter in guessed_letters for letter in secret_word):
        print("Word: " + ''.join(letter if letter in guessed_letters else '_' for letter in secret_word))
        letter = input("Guess a letter: ").lower()

        if letter in guessed_letters:
            print(f"You've already guessed the letter '{letter}'")
        elif letter in secret_word:
            print("Correct guess!")
            guessed_letters.append(letter)
        else:
            print("Incorrect guess!")
            attempts -= 1

    if all(letter in guessed_letters for letter in secret_word):
        print(f"Congratulations! You guessed the word: {secret_word}")
    else:
        print(f"Sorry, you're out of attempts! The word was: {secret_word}")

letter_guessing_game()
