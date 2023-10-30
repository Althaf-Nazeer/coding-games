def print_board(board):
    for row in board:
        print(" ".join(row))

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    print("Welcome to Tic Tac Toe!")

    for _ in range(9):
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn")

        while True:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))

            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("That spot is already taken. Try again.")

        if check_win(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            return

        turn += 1

    print_board(board)
    print("It's a tie!")

tic_tac_toe()
