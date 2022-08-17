import random


def comGuess(x):
    lowerNum = 1
    higherNum = x
    feedback = ""
    while feedback != "c":
        if lowerNum != higherNum:
            guess = random.randint(lowerNum, higherNum)
        else:
            guess = higherNum
        feedback = input(f'Is {guess} too high (H), too low (L), or correct(C): ').lower()
        if feedback == "h":
            higherNum = guess - 1
        elif feedback == "l":
            lowerNum = guess + 1
    print("Yay, the computer guessed the number correctly")

comGuess(10)