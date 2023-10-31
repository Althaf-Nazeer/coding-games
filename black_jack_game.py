import random

def blackjack():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    player_hand = []
    dealer_hand = []

    def deal_card(hand):
        hand.append(random.choice(cards))

    deal_card(player_hand)
    deal_card(player_hand)
    deal_card(dealer_hand)
    print(f"Your cards: {player_hand}")
    print(f"Dealer's cards: {dealer_hand[0]}")

    while sum(player_hand) < 21:
        action = input("Do you want to hit or stand? ").lower()
        if action == 'hit':
            deal_card(player_hand)
            print(f"Your cards: {player_hand}")
        elif action == 'stand':
            break

    while sum(dealer_hand) < 17:
        deal_card(dealer_hand)

    print(f"Your cards: {player_hand}")
    print(f"Dealer's cards: {dealer_hand}")
    
    player_sum = sum(player_hand)
    dealer_sum = sum(dealer_hand)

    if player_sum > 21:
        print("You bust! Dealer wins.")
    elif dealer_sum > 21 or player_sum > dealer_sum:
        print("You win!")
    elif player_sum == dealer_sum:
        print("It's a tie!")
    else:
        print("Dealer wins!")

blackjack()
