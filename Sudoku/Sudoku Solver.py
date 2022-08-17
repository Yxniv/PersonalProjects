def findEmptySpace(puzzle):

    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == -1:
                return row, column
    return None, None

# Checks to ensure that the number abides by the rules of the game
def isValid(puzzle, guess, row, column):

    # Checks each item in the row to see whether it matches
    rowValues = puzzle[row]
    if guess in rowValues:
        return False

    columnValues = [puzzle[index][column] for index in range(9)]
    # for index in range(9):
        # columnValues.append(puzzle[index,column])
    if guess in columnValues:
        return False

    rowStart = (row // 3) * 3
    columnStart = (column // 3) * 3

    for row in range(rowStart, rowStart + 3):
        for column in range(columnStart, columnStart + 3):
            if puzzle[row][column] == guess:
                return False

    return True


def sudokuSolver(puzzle):
    row, column = findEmptySpace(puzzle)

    if row is None:
        return True

    for guess in range(1, 10):
        if isValid(puzzle, guess, row, column):
            puzzle[row][column] = guess

            if sudokuSolver(puzzle):
                return True

        puzzle[row][column] = -1

    return False
