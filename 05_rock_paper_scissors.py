import random

CHOICES = ["rock", "paper", "scissors"]
WINS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

def main():
    you = bot = 0
    while True:
        p = input("rock / paper / scissors (q to quit): ").lower()
        if p == "q":
            break
        if p not in CHOICES:
            print("Invalid choice.")
            continue
        c = random.choice(CHOICES)
        print("Computer:", c)
        if p == c:
            print("Draw")
        elif WINS[p] == c:
            you += 1
            print("You win")
        else:
            bot += 1
            print("You lose")
        print(f"Score -> You: {you}  Computer: {bot}")

if __name__ == "__main__":
    main()
