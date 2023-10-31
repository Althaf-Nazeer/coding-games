import random

def roll_dice():
    while True:
        input("Press Enter to roll the dice, or type 'exit' to quit: ")
        roll = random.randint(1, 6)
        print(f"You rolled: {roll}")
        if input("Roll again? (yes/no): ").lower() != 'yes':
            break

roll_dice()
