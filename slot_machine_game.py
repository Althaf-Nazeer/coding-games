import random

def slot_machine():
    symbols = ["Cherry", "Bell", "Lemon", "Orange", "Star", "Diamond"]
    wallet = 100

    while True:
        input("Press Enter to play the slot machine. Each play costs $10.")
        if wallet < 10:
            print("Insufficient funds. Game over.")
            break

        wallet -= 10
        spin = [random.choice(symbols) for _ in range(3)]
        print(f"Spinning... {spin[0]} - {spin[1]} - {spin[2]}")

        if spin[0] == spin[1] == spin[2]:
            earnings = 50 if spin[0] == "Diamond" else 10
            wallet += earnings
            print(f"Jackpot! You won ${earnings}. Your wallet: ${wallet}")
        else:
            print("No match. Try again.")

slot_machine()
