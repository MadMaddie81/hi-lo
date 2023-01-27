"""
WELCOME TO HI-LO!
A number-guessing game that oozes 80's nostalgia in every line.

- A number will be randomly generated depending on the chosen difficulty level.
- The goal is to guess the number in as few tries as possible, with the help
  of 'higher-than' and 'lower-than' hints.
- If the player manage to guess the correct number in few enough tries they
  will be rewarded with some classic ASCII-art.

ENJOY!

"""
import random
import os


def introduction():
    """
    Clears the screen before running the game.
    Displays the header art, and prints the initial information
    about the game to the player.
    """
    os.system('clear')
    print_txt('header.txt')

    print("Hello and welcome to Hi-Lo!\n")
    print("In this game I will think of a number and your task is simply")
    print("to guess what that number is.\n")
    print("If you can guess my number correctly in few enough tries,")
    print("I will give you a dragon.\n")

    print("First you need to pick your difficulty level.")
    print("Please answer with 1, 2 or 3\n")

    print("1. EASY - 1-10 - Guess my number within 3 tries to win a dragon")
    print("2. NORMAL - 1-100 - Guess my number within 6 tries to win a dragon")
    print(
        "3. HARD - 1-1000 - Guess my number within 10 tries to win a dragon\n"
        )
    print("-----------------------------------------------------------")
    print("IF YOU AT ANY POINT WISH TO EXIT THE GAME, PLEASE ENTER 'E'")
    print("-----------------------------------------------------------")


def print_txt(file):
    """
    Open, read, print and close the desired txt-file.
    """
    f = open(file)
    lines = f.read()
    f.close()
    print(lines)
    print("\n")


def exit_game():
    """
    Ends the game on player's request.
    """
    os.system('clear')
    print_txt('game-over.txt')

    print("THANK YOU FOR PLAYING HI-LO!")
    print("Have a nice day :)")
    raise SystemExit()


def play_again():
    """
    Gives the player the option to play the game again.
    Clears the screen before running the game once more.
    """
    restart = input("Would you like to play again? [Y/N]\n")
    yes = ['y', 'y', 'yes', 'Yes', 'YES']
    no = ['n', 'N', 'no', 'NO']
    if restart in yes:
        main()
    elif restart in no or restart == "E" or restart == "e":
        exit_game()
    else:
        print("I'm just going to ask one more time.")
        try_again = input('Do you wish to play again? Enter "Y" or "N".\n')
        if try_again in yes:
            main()
        else:
            exit_game()


def validate_choice(choice):
    """
    Tries to convert the input string to integer.
    Raises ValueError if the string cannot be converted to int,
    or if the choice isn't 1, 2 or 3.
    Also ends the game on player's request
    """
    if choice == "e" or choice == "E":
        exit_game()
    try:
        choice = int(choice)
        if choice < 1 or choice > 3:
            raise ValueError
    except ValueError:
        print('Umm... There are 3 difficulty levels.')
        print(f'What do you mean by "{choice}"?')
        print('Please type 1, 2 or 3.\n')
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


def validate_guess(guess, top, used):
    """
    Tries to convert the player's guess to an integer.
    Retuns False if:
      - The guessed number is below 1 or above the highest
        number for the chosen level.
      - The number has already been guessed before.
      - ValueError is found.
    Also ends the game on player request.
    """
    if guess == "e" or guess == "E":
        exit_game()
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
        elif guess in used:
            print("--------------------------------------------------")
            print(f"You have already guessed {guess}")
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


def get_guess(top, used):
    """
    - Collects a guess from the player.
    - Sends the guess as well as a list of used guesses to
      a validating function.
    - Runs a loop until a valid guess is provided.
    - Returns the guess as an integer.
    """
    while True:
        guess = input("What is my number?\n")
        if validate_guess(guess, top, used):
            break
    return int(guess)


def play_game(answer, top):
    """
    - Takes the player's guess and compares it to the correct answer
      in a while loop until the correct answer is given.
    - Keeps count on the number of guesses by adding +1 to a variable
      for every iteration of the loop.
    - Saves all used guesses in a list to prevent the same number
      from being guessed twice.
    """
    print(f"I'm thinking of a number between 1 and {top}.")
    print(answer)
    tries = 0
    used_guesses = []
    intermission_points = [10, 20, 30]
    while True:
        if tries in intermission_points:
            intermission(tries, answer, top)
        guess = get_guess(top, used_guesses)
        tries += 1
        used_guesses.append(guess)
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


def intermission(tries, answer, top):
    """
    Pauses the game when the player has made too many guesses
    to ask if the player wish to give up.
    """

    if tries == 30:
        print("Ok, this is getting ridiculous")
        print(f"You have tried guessing this number {tries} times now.")
        print("I'm putting an end to this farse.")
        print(f"I was thinking of {answer}.")
        play_again()

    print("Stop for a moment.")
    print(f"You have now tried to guess this number {tries} times.")

    response = input("Do you wish to continue? [Y/N]\n")
    yes = ['y', 'y', 'yes', 'Yes', 'YES']
    no = ['n', 'N', 'no', 'NO']
    if response in yes:
        print("Ok, I was just checking.")
        print("Let's continue then...")
        print("--------------------------------------------------")
        print(f"I'm thinking of a number between 1 and {top}.")
    elif response in no:
        print("Ok, let's end this then.")
        print(f"I was thinking of {answer}")
        play_again()
    else:
        print("I was asking you a question.")
        response = input("Do you wish to continue? [Y/N]\n")
        if response in yes:
            print("Ok, I was just checking.")
            print("Let's continue then...")
            print("--------------------------------------------------")
            print(f"I'm thinking of a number between 1 and {top}.")
        else:
            print("Ok, let's end this then.")
            print(f"I was thinking of {answer}")
            play_again()


def result(answer, rounds, level):
    """
    Clears the screen
    Congratulates the player for correctly guessing the right number.
    Displays ASCII-art if the player finished in few enough tries.
    """
    os.system('clear')
    print("YOU GOT IT!")
    print(f"I was thinking of {answer}.")
    print(f"You got the answer in {rounds} tries.")

    if level == 3 and rounds == 1:
        print_txt("first_try.txt")
        print("YOU ARE A LEGEND!")
        print("You got the correct number between 1 and 1000 in the first try")
        print("I have a special dragon just for you.")
        print("\n")
    elif level == 1 and rounds <= 3:
        print_txt("dragon1.txt")
        print("CONGRATULATIONS!")
        print("YOU WON THE LEVEL 1 DRAGON!")
        print("\n")
    elif level == 2 and rounds <= 6:
        print_txt("dragon2.txt")
        print("CONGRATULATIONS!")
        print("YOU WON THE LEVEL 2 DRAGON!")
        print("\n")
    elif level == 3 and rounds <= 10:
        print_txt("dragon3.txt")
        print("CONGRATULATIONS!")
        print("YOU WON THE LEVEL 3 DRAGON!")
        print("\n")
    else:
        print("I'm sorry, you didn't win a dragon this time.")
        print("\n")


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
    result(answer, rounds, level)
    play_again()


main()
