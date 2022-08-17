import random
from Words import hangmanWords
import string


def get_valid_word(hangmanWords):
    print("This is a set", set())
    randomWord = random.choice(hangmanWords)  # random word from this list
    while '-' in randomWord or ' ' in randomWord:
        randomWord = random.choice(hangmanWords)
    return randomWord.upper()


def hangmanGame():
    guessWord = get_valid_word(hangmanWords) # this is the random word
    #guessWord = "Base"
    letters = set(guessWord)
    alphabet = set(string.ascii_uppercase)
    usedLetters = set()
    userLives = 6

    while len(guessWord) > 0 and userLives > 0:
        # Gets the users input
        print(f"You Currently have: {userLives} Lives \n"
              "Used Letters: ",  " ".join(usedLetters), "\n")
        wordCheck = [letters if letters in usedLetters else '-' for letters in guessWord]  # checks to see if the
        # letter in the used words if not then it uses dashes

        print("Current word: ", " ".join(wordCheck))
        userInput = input("Please guess a letter: ").upper()
        if userInput in alphabet - usedLetters:
            usedLetters.add(userInput)
            if userInput in guessWord:
                letters.remove(userInput)
            else:
                userLives = userLives - 1

        elif userInput in usedLetters:
            print("Letter has already been used please guess another letter")

        else:
            print("Invalid Letter")

        if userLives == 0:
            rematch = input("You died. Do you want to play again:").lower()
            if rematch == "y":
                hangmanGame()
            else:
                print("Game Over.")
        else:
            print("Congrats. You've guessed the word.")
hangmanGame()
