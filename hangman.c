#include <stdio.h>
#include <string.h>
#include <ctype.h>

void hangman(int attempts) {
    if (attempts == 0) {
        printf("_____\n");
        printf("|   |\n");
        printf("|\n");
        printf("|\n");
        printf("|\n");
        printf("|\n");
    } else if (attempts == 1) {
        printf("_____\n");
        printf("|   |\n");
        printf("|   O\n");
        printf("|\n");
        printf("|\n");
        printf("|\n");
    } else if (attempts == 2) {
        printf("_____\n");
        printf("|   |\n");
        printf("|   O\n");
        printf("|   |\n");
        printf("|   |\n");
        printf("|\n");
    } else if (attempts == 3) {
        printf("_____\n");
        printf("|   |\n");
        printf("|   O\n");
        printf("|  \\|\n");
        printf("|   |\n");
        printf("|\n");
    } else if (attempts == 4) {
        printf("_____\n");
        printf("|   |\n");
        printf("|   O\n");
        printf("|  \\|/\n");
        printf("|   |\n");
        printf("|\n");
    } else if (attempts == 5) {
        printf("_____\n");
        printf("|   |\n");
        printf("|   O\n");
        printf("|  \\|/\n");
        printf("|   |\n");
        printf("|  / \n");
    } else {
        printf("_____\n");
        printf("|   |\n");
        printf("|   O\n");
        printf("|  \\|/\n");
        printf("|   |\n");
        printf("|  / \\\n");
    }
}

int main() {
    char word[20], display[20], guessedLetters[26];
    int attempts = 0, length, guessed = 0;
    int i, j;

    printf("Enter the word for the hangman game (in lowercase): ");
    scanf("%s", word);
    length = strlen(word);

    for (i = 0; i < length; i++) {
        display[i] = '_';
    }
    display[i] = '\0';

    printf("Let's play Hangman!\n");

    while (attempts < 6 && !guessed) {
        printf("Word to guess: %s\n", display);
        printf("Enter a letter to guess: ");
        char letter;
        scanf(" %c", &letter);
        letter = tolower(letter);

        int found = 0;
        for (j = 0; j < length; j++) {
            if (word[j] == letter && display[j] == '_') {
                display[j] = letter;
                found = 1;
            }
        }

        if (!found) {
            int letterFound = 0;
            for (j = 0; j < guessed; j++) {
                if (guessedLetters[j] == letter) {
                    letterFound = 1;
                    break;
                }
            }

            if (!letterFound) {
                guessedLetters[guessed++] = letter;
                hangman(attempts);
                attempts++;
            }
        }

        int allFound = 1;
        for (j = 0; j < length; j++) {
            if (display[j] == '_') {
                allFound = 0;
                break;
            }
        }

        if (allFound) {
            printf("Congratulations! You guessed the word: %s\n", word);
            guessed = 1;
        }
    }

    if (attempts == 6 && !guessed) {
        printf("Sorry, you ran out of attempts. The word was: %s\n", word);
    }

    return 0;
}
