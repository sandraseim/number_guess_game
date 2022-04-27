from random import randint

EASY = 10
HARD = 5


def check_answer(guess, answer, turns):
    """"checks answerr against guess."""
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"Got it right. The answer is {answer}")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard':  ")
    if level == "easy":
        return EASY
    else:
        return HARD


def game():
    print("Guessing game! Guess the number between 1 and 100")
    answer = randint(1, 100)

    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("you lose")
            return
        elif guess != answer:
            print("guess again")


game()
