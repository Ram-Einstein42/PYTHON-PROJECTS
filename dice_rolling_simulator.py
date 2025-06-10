import random
 
# Dice Rolling Simulator
print("🎲 Welcome to the Dice Rolling Simulator!")

while True:
    input("Press Enter to roll the dice...")
    dice_roll = random.randint(1, 6)
    print(f"You rolled a {dice_roll}!")


    # Show ASCII art for dice
    dice_faces = {
        1: """1
         -----
        |     |
        |  *  |
        |     |
         -----
        """,
        2: """
         -----
        | *   |
        |     |
        |   * |
         -----
        """,
        3: """
         -----
        | *   |
        |  *  |
        |   * |
         -----
        """,
        4: """
         -----
        | * * |
        |     |
        | * * |
         -----
        """,
        5: """
         -----
        | * * |
        |  *  |
        | * * |
         -----
        """,
        6: """
         -----
        | * * |
        | * * |
        | * * |
         -----
        """
    }
    print(dice_faces[dice_roll])

    roll_again = input("Do you want to roll again? (yes/no): ").strip().lower()
    if roll_again != 'yes':
        print("Thanks for playing!")
        break