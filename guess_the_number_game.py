import random

def guess_number():
    number = random.randint(1, 20)
    chances = 3

    print("Guess a number between 1 and 20.")
    while chances > 0:
        guess = int(input("Enter your guess: "))

        if guess == number:
            print("Congratulations! You guessed the correct number!")
            break
        elif guess < number:
            print("Guess a higher number.")
        else:
            print("Guess a lower number.")
        chances -= 1

    if chances == 0:
        print(f"Sorry, you've run out of chances. The number was {number}.")

guess_number()
