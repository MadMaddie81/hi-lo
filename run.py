def introduction():
    """
    Displays the header art, and prints the initial information
    about the game to the player.
    """
    f = open('header.txt')
    lines = f.read()
    f.close()
    print(lines)
    print("\n")

    print("Hello and welcome to Hi-Lo!\n")
    print("In this game I will think of a number and your task is simply\nto guess what that number is.\n")
    print("If you can guess my number correctly in few enough tries\nI will give you a dragon.\n")

    print("First you need to pick your difficulty level.")
    print("Please answer with 1, 2 or 3\n")

    print("1. EASY - 1-10 - Guess my number within 3 tries to win the Small Dragon")
    print("2. NORMAL - 1-100 - Guess my number within 5 tries to win the Medium Dragon")
    print("3. HARD - 1-1000 - Guess my number within 10 tries to win the Big Dragon\n")


def main():
    """
    The main function that will be calling the other functions in 
    the correct order.
    """
    introduction()


main()
