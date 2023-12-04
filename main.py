#Zubair Dawd 101128532
import random

def roll_dice():
    # Generate a random number between 1 and 6
    return random.randint(1, 6)

def main():

    print("Welcome to the Rolling Dice Simulator!")

    while True:
        input("Press Enter to roll the dice...")

        # Call the roll_dice function to get a random number
        dice_result = roll_dice()

        print(f"You rolled: {dice_result}")

        play_again = input("Do you want to roll the dice again? (yes/no): ").lower()

        if play_again != 'yes':
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()

