#include <stdio.h>

char board[3][3] = { { '1', '2', '3' }, { '4', '5', '6' }, { '7', '8', '9' } };
int currentPlayer = 1;

void drawBoard() {
    printf("Tic-Tac-Toe Game\n");
    printf("Player 1 (X)  -  Player 2 (O)\n\n");

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf(" %c ", board[i][j]);
            if (j < 2) {
                printf("|");
            }
        }
        printf("\n");
        if (i < 2) {
            printf("-----------\n");
        }
    }
}

int checkWin() {
    for (int i = 0; i < 3; i++) {
        if (board[i][0] == board[i][1] && board[i][1] == board[i][2]) {
            return 1;
        }
        if (board[0][i] == board[1][i] && board[1][i] == board[2][i]) {
            return 1;
        }
    }

    if (board[0][0] == board[1][1] && board[1][1] == board[2][2]) {
        return 1;
    }

    if (board[0][2] == board[1][1] && board[1][1] == board[2][0]) {
        return 1;
    }

    return 0;
}

int main() {
    int choice, row, col;
    int gameOver = 0;
    drawBoard();

    while (!gameOver) {
        currentPlayer = (currentPlayer % 2) ? 1 : 2;

        printf("Player %d, enter a number: ", currentPlayer);
        scanf("%d", &choice);

        row = --choice / 3;
        col = choice % 3;

        if (choice < 0 || choice > 8 || board[row][col] == 'X' || board[row][col] == 'O') {
            printf("Invalid move. Try again.\n");
            currentPlayer--;
        } else {
            board[row][col] = (currentPlayer == 1) ? 'X' : 'O';
            drawBoard();
            if (checkWin()) {
                printf("Player %d wins!\n", currentPlayer);
                gameOver = 1;
            } else if (currentPlayer == 9) {
                printf("It's a draw!\n");
                gameOver = 1;
            }
        }
        currentPlayer++;
    }
    return 0;
}
