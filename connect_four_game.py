def print_board(board):
    for row in board:
        print(' '.join(row))

def connect_four():
    rows = 6
    cols = 7
    board = [['.'] * cols for _ in range(rows)]
    player = 'X'

    def check_winner():
        # Check for a winner - logic for Connect Four game

    while True:
        print_board(board)
        col = int(input(f"Player {player}, choose a column (0-6): "))
        for row in range(rows - 1, -1, -1):
            if board[row][col] == '.':
                board[row][col] = player
                break
        else:
            print("Column is full. Choose another column.")
            continue

        if check_winner():
            print(f"Player {player} wins!")
            break

        player = 'O' if player == 'X' else 'X'

connect_four()
