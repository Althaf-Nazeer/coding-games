import random

def generate_symbols():
    symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    return random.sample(symbols * 2, 8)

def display_board(board, revealed):
    for i, val in enumerate(board):
        if revealed[i]:
            print(val, end=' ')
        else:
            print('?', end=' ')
        if (i + 1) % 4 == 0:
            print()

def memory_puzzle():
    symbols = generate_symbols()
    revealed = [False] * 16
    turns = 0

    while not all(revealed):
        display_board(symbols, revealed)
        index1, index2 = map(int, input("Enter two positions (0-15) separated by a space: ").split())

        if symbols[index1] == symbols[index2]:
            revealed[index1] = revealed[index2] = True
            print("Match!")
        else:
            print("Not a match.")

        turns += 1

    print(f"Congratulations! You completed the game in {turns} turns.")

memory_puzzle()
