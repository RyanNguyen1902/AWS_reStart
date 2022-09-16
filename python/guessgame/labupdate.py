import random

number = random.randint(1,10)
isGuessRight = False

print("wellcome to game guess number")
mode = input("chose your mode do you want, hard, normal, easy:")
i=0

while mode == "hard" and isGuessRight != True and i <1: 
    guess = input("Guess a number between 1 and 10 (just one time): ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. you lose.".format(guess))
        i=i+1;

while mode == "normal" and isGuessRight != True and i <3: 
    guess = input("Guess a number between 1 and 10 (just three time): ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. you lose.".format(guess))
        i=i+1;

while  mode == "easy" and isGuessRight != True and i <6: 
    guess = input("Guess a number between 1 and 10 (just 6 time): ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. you lose.".format(guess))
        i=i+1;

        
