#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int playerCards[9], dealerCards[9], playerTotal = 0, dealerTotal = 0;
    int playerCardsCount = 0, dealerCardsCount = 0, cardIndex = 0;

    srand(time(NULL));

    // Function to draw a card
    int drawCard() {
        return (rand() % 13) + 1; // Generating a card value from 1 to 13 (simplified deck)
    }

    // Initial draw for player and dealer
    playerCards[playerCardsCount++] = drawCard();
    dealerCards[dealerCardsCount++] = drawCard();

    playerCards[playerCardsCount++] = drawCard();
    dealerCards[dealerCardsCount++] = drawCard();

    // Function to calculate total value of cards
    int calculateTotal(int cards[], int count) {
        int total = 0;
        for (int i = 0; i < count; i++) {
            if (cards[i] > 10) {
                total += 10; // Face cards value set to 10
            } else {
                total += cards[i];
            }
        }
        return total;
    }

    playerTotal = calculateTotal(playerCards, playerCardsCount);
    dealerTotal = calculateTotal(dealerCards, dealerCardsCount);

    printf("Player's Cards: %d, %d\n", playerCards[0], playerCards[1]);
    printf("Dealer's Card: %d\n", dealerCards[0]);

    while (1) {
        if (playerTotal == 21) {
            printf("Blackjack! You win!\n");
            break;
        } else if (playerTotal > 21) {
            printf("Bust! You lose!\n");
            break;
        }

        char choice;
        printf("Do you want to hit (h) or stand (s)? ");
        scanf(" %c", &choice);

        if (choice == 'h') {
            playerCards[playerCardsCount++] = drawCard();
            playerTotal = calculateTotal(playerCards, playerCardsCount);
            printf("Your new card: %d\n", playerCards[playerCardsCount - 1]);
            printf("Player's total: %d\n", playerTotal);
        } else if (choice == 's') {
            while (dealerTotal < 17) {
                dealerCards[dealerCardsCount++] = drawCard();
                dealerTotal = calculateTotal(dealerCards, dealerCardsCount);
            }
            printf("Dealer's Cards: ");
            for (int i = 0; i < dealerCardsCount; i++) {
                printf("%d ", dealerCards[i]);
            }
            printf("\n");
            printf("Dealer's total: %d\n", dealerTotal);

            if (dealerTotal > 21) {
                printf("Dealer busts! You win!\n");
            } else if (dealerTotal >= playerTotal) {
                printf("Dealer wins!\n");
            } else {
                printf("You win!\n");
            }
            break;
        }
    }

    return 0;
}
