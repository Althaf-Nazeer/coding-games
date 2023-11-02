#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int playerChoice, computerChoice;
    srand(time(0));

    printf("Welcome to Rock, Paper, Scissors Game!\n");
    printf("Choose:\n1 for Rock\n2 for Paper\n3 for Scissors\n");

    printf("Enter your choice: ");
    scanf("%d", &playerChoice);

    if (playerChoice < 1 || playerChoice > 3) {
        printf("Invalid choice!");
        return 1;
    }

    computerChoice = rand() % 3 + 1; // Generate a random choice for the computer

    if (playerChoice == computerChoice) {
        printf("It's a tie!\n");
    } else if ((playerChoice == 1 && computerChoice == 3) ||
               (playerChoice == 2 && computerChoice == 1) ||
               (playerChoice == 3 && computerChoice == 2)) {
        printf("You win!\n");
    } else {
        printf("Computer wins!\n");
    }

    return 0;
}
