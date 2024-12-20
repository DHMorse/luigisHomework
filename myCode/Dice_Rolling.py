import random
from typing import Dict

def rollD6() -> int:
    """Rolls a single six-sided die and returns the result."""
    return random.randint(1, 6)

def rollTwoD6() -> int:
    """Rolls two six-sided dice and returns their sum."""
    return rollD6() + rollD6()

def display_die(n: int) -> None:
    """Displays a visual representation of a die face based on the value."""
    die_faces: Dict[int, str] = {
        1: [
            " ------- ",
            "|       |",
            "|   o   |",
            "|       |",
            " ------- "
        ],
        2: [
            " ------- ",
            "| o     |",
            "|       |",
            "|     o |",
            " ------- "
        ],
        3: [
            " ------- ",
            "| o     |",
            "|   o   |",
            "|     o |",
            " ------- "
        ],
        4: [
            " ------- ",
            "| o   o |",
            "|       |",
            "| o   o |",
            " ------- "
        ],
        5: [
            " ------- ",
            "| o   o |",
            "|   o   |",
            "| o   o |",
            " ------- "
        ],
        6: [
            " ------- ",
            "| o   o |",
            "| o   o |",
            "| o   o |",
            " ------- "
        ]
    }

    face = die_faces.get(n)
    if face:
        for line in face:
            print(line)
    else:
        raise ValueError(f"Invalid die value: {n}. Must be between 1 and 6.")

def roll_many(num_rolls: int, display: bool = False) -> int:
    """Rolls a die multiple times, optionally displaying each roll, and returns the total."""
    total = 0
    for _ in range(num_rolls):
        roll = rollD6()
        if display:
            display_die(roll)
        total += roll
    return total

def main() -> None:
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        try:
            num_rolls = int(input("How many times would you like to roll the die? "))
            if num_rolls < 1:
                raise ValueError("Number of rolls must be at least 1.")
            total = roll_many(num_rolls, display=True)
            print(f"Total: {total}")
            break
        except ValueError as e:
            print(e)
            continue

if __name__ == '__main__':
    main()