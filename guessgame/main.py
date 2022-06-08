from art import logo
from random import randint
from replit import clear

easy_turn = 100
hard_turn = 5

def check_answer(guess, answer, turrns):
    if guess > answer:
        print("To high")
        return turrns -1
    elif guess < answer:
        print("Too Low")
        return turrns -1 
    else:
        print(f"you got it! the answer was{answer}")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return easy_turn
    else: return hard_turn
def game():
    print(logo)
    print("Wellcome to the Number Gues Game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1, 100)
    turns = set_difficulty()
    guess = 0

    while guess != answer:
        print(f"you have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You fail. See you later")
            break
        elif guess != answer:
            print("guess again!")

while input("do you want to play game again? TypeY or N ") =="Y":
    clear()
    game()

