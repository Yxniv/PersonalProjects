import random


def guessNumber(number):
    randomNumber = random.randint(1, number)
    guess = 0
    while guess != randomNumber:
        guess = int(input(f"Guess a number between 1 and {number}: "))
        if guess < randomNumber:
            print("Sorry, Guess again. Too Low")
        elif guess > randomNumber:
            print("Guess it too high")
    print(f"Congrats you have guess the number {randomNumber} correctly.")


guessNumber(20)
