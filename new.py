import random
print("Welcome to this wonderful guessing game")
print("""
There are 3 levels, Easy, Medium and Hard
Easy you get to choose between number 1-10 and guess limit of 6
Medium you get to guess between number 1-20 and guess limit of 4
Hard you get to guess between number 1-50 and guess limit of 3
    """)

level = input("Select level: ")


def easy():
    easy_range = random.randint(1, 10)
    guess_limit_easy = 6
    guess_count = 0
    while guess_count < guess_limit_easy:
        try:
            user_guess = int(input("Guess: "))
            guess_limit_easy -= 1
            print(f"You have {guess_limit_easy} guesses left")
            if user_guess == easy_range:
                print("You got it right")
                break
            else:
                print("You got it wrong")
        except ValueError:
            print("Only numbers are allowed")
    else:
        print("Game Over")
    exit()


def medium():
    medium_range = random.randint(1, 20)
    guess_limit_medium = 4
    guess_count = 0
    while guess_count < guess_limit_medium:
        try:
            user_guess = int(input("Guess: "))
            guess_limit_medium -= 1
            print(f"You have {guess_limit_medium} guesses left")
            if user_guess == medium_range:
                print("You got it right")
                break
            else:
                print("You got it wrong")
        except ValueError:
            print("Only numbers are allowed")
    else:
        print("Game Over")
    exit()


def hard():
    hard_range = random.randint(1, 50)
    guess_limit_hard = 3
    guess_count = 0
    while guess_count < guess_limit_hard:
        try:
            user_guess = int(input("Guess: "))
            guess_limit_hard -= 1
            print(f"You have {guess_limit_hard} guesses left")
            if user_guess == hard_range:
                print("You got it right")
                break
            else:
                print("You got it wrong")
        except ValueError:
            print("Only numbers are allowed")
    else:
        print("Game Over")
    exit()


while True:
    if level == "easy":
        easy()
    elif level == "medium":
        medium()
    elif level == "hard":
        hard()
    else:
        print("No level has been selected")
