import random

def word_jumble():
    words = ['python', 'gaming', 'code', 'hangman', 'computer']
    chosen_word = random.choice(words)
    jumbled = ''.join(random.sample(chosen_word, len(chosen_word)))

    print("Welcome to Word Jumble!")
    print(f"Unscramble the letters to make a word. Your jumbled word is: {jumbled}")

    guess = input("Your guess: ").lower()

    if guess == chosen_word:
        print("Congratulations! That's correct.")
    else:
        print(f"Sorry, that's incorrect. The word was: {chosen_word}")

word_jumble()
