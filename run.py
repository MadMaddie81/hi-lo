import random


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
    print("If you can guess my number correctly in few enough tries,\nI will give you a dragon.\n")

    print("First you need to pick your difficulty level.")
    print("Please answer with 1, 2 or 3\n")

    print("1. EASY - 1-10 - Guess my number within 3 tries to win the Small Dragon")
    print("2. NORMAL - 1-100 - Guess my number within 6 tries to win the Medium Dragon")
    print("3. HARD - 1-1000 - Guess my number within 10 tries to win the Big Dragon\n")


def validate_choice(choice):
    """
    Inside the try, convert the input string to integer.
    Raises ValueError if the string cannot be converted to int,
    or if the choice isn't 1, 2 or 3.
    """
    try:
        choice = int(choice)
        if choice < 1 or choice > 3:
            raise ValueError
    except ValueError:
        print(f'Umm... There are 3 difficulty levels.\nWhat do you mean by "{choice}"?\nPlease type 1, 2 or 3.\n')
        return False
    return True


def get_difficulty():
    """
    Get difficulty level choice from the player.
    Runs a while-loop to get a valid answer from the player,
    which has to be 1, 2 or 3.
    The loop will keep asking for a difficulty level,
    until a valid number is entered.
    Returns the input as an integer.
    """
    while True:
        choice = input("Choose difficulty level:\n")
        if validate_choice(choice):
            print("Thank you!\n")
            break
    return int(choice)


def get_max(level):
    """
    Decides the highest possible number to be generated and guessed,
    depending on the chosen difficulty level.
    """
    if level == 1:
        top = 10
    elif level == 2:
        top = 100
    elif level == 3:
        top = 1000
    return top


def randomize_answer(top):
    """
    Randomizes the correct answer depending on the chosen difficulty level.
    """
    answer = random.randrange(1, top)
    return answer


def validate_guess(guess, top):
    """
    Tries to convert the player's guess to an integer.
    Raises ValueError if conversion isn't possible.
    """
    try:
        guess = int(guess)
        if guess < 1 or guess > top:
            print("--------------------------------------------------")
            print(f"I told you to guess a number between 1 and {top},")
            print(f"and you chose {guess}?")
            print("I'm not going to count that as a guess.")
            print("Try again!")
            print("--------------------------------------------------")
            return False
    except ValueError:
        print("--------------------------------------------------")
        print(f'{guess}? What kind of answer is that?')
        print("That's not even a number.")
        print("Are these rules to difficult for you?")
        print("Try again!")
        print("--------------------------------------------------")
        print(f"I'm thinking of a number between 1 and {top}")
        return False
    return True


def get_guess(top):
    """
    Collects a guess from the player.
    Runs a loop until a valid guess is provided.
    Returns the guess as an integer.
    """
    while True:
        guess = input("What is my number?\n")
        if validate_guess(guess, top):
            break
    return int(guess)


def play_game(answer, top):
    """
    Takes the player's guess and compares it to the correct answer
    in a while loop until the correct answer is given.
    Keeps count on the number of guesses by adding +1 to a variable
    for every iteration of the loop.
    """
    print(f"I'm thinking of a number between 1 and {top}.")
    tries = 0
    while True:
        guess = get_guess(top)
        tries += 1
        if guess < answer:
            print(f"My number is higher than {guess}")
            print("--------------------------------------------------")
        elif guess > answer:
            print(f"My number is lower than {guess}")
            print("--------------------------------------------------")
        elif guess == answer:
            print(f"You got it!\nI was thinking of {answer}")
            break
    return tries


def main():
    """
    The main function that will be calling the other functions in
    the correct order.
    """
    introduction()
    level = get_difficulty()
    highest_no = get_max(level)
    answer = randomize_answer(highest_no)
    rounds = play_game(answer, highest_no)
    print(f"Number of tries: {rounds}")


main()
