import random

def roll_dice(num_dice, sides):
    """Simulate rolling 'num_dice' dice with 'sides' number of sides."""
    rolls = []
    for _ in range(num_dice):
        roll = random.randint(1, sides)
        rolls.append(roll)
    return rolls

def main():
    print("Welcome to the D&D Dice Roller!")

    while True:
        print("\nOptions:")
        print("1. Roll dice")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            num_dice = int(input("Enter the number of dice to roll: "))
            sides = int(input("Enter the number of sides on each die: "))
            rolls = roll_dice(num_dice, sides)
            total = sum(rolls)
            print(f"\nYou rolled: {', '.join(map(str, rolls))}")
            print(f"Total: {total}")
        elif choice == '2':
            print("Exiting the D&D Dice Roller. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()