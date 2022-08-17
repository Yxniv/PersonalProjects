import random


def game():
    userInput = input("Rock(R), Paper(P), or Scissors(S): ").lower()
    computerChoice = random.choice(["R", "P", "S"]).lower()

    if userInput == computerChoice:
        print("It is a Tie")
        return game()

    if is_win(userInput, computerChoice):
        print("You win")

    if not is_win(userInput, computerChoice):
        rematch = input("You lose. Play again? ").lower()
        if rematch == 'y':
            game()
        else:
            print("Game over")


def is_win(player, computer):
    # returns true if the player wins
    # r>s,s>p,p>r
    if (player == "r" and computer == "s") or (player == "s" and computer == "p") \
            or (player == "p" and computer == "r"):
        return True


game()
