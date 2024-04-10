import random
from typing import List

def roll_dice(num_dice: int, sides: int) -> List[int]:
    """Simulate rolling 'num_dice' dice with 'sides' number of sides."""
    rolls: List[int] = []
    for _ in range(num_dice):
        roll: int = random.randint(1, sides)
        rolls.append(roll)
    return rolls

def main() -> None:
    print("Welcome to the D&D Dice Roller!")

    while True:
        print("\nOptions:")
        print("1. Roll dice")
        print("2. Exit")

        choice: str = input("Enter your choice: ")

        if choice == '1':
            num_dice: int = int(input("Enter the number of dice to roll: "))
            sides: int = int(input("Enter the number of sides on each die: "))
            rolls: List[int] = roll_dice(num_dice, sides)
            total: int = sum(rolls)
            print(f"\nYou rolled: {', '.join(map(str, rolls))}")
            print(f"Total: {total}")
        elif choice == '2':
            print("Exiting the D&D Dice Roller. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
