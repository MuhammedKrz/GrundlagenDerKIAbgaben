# Don't forget -> always alternating
ticTacToeBoard = [1, 1, -1,
                   1,-1, 0,
                  -1, 0, 0]

winCombinations = [
    # diagonals
    [0, 4, 8],
    [2, 4, 6],
    # rows
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    # columns
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8]
]

def printBoard(ticTacToeBoard):
    for i in range(len(ticTacToeBoard)):
        if i % 3 == 0 and i != 0:
            print()
        if ticTacToeBoard[i] == 1:
            print("X", end=" ")
        elif ticTacToeBoard[i] == -1:
            print("O", end=" ")
        else:
            print("#", end=" ")

def calculateBoard(ticTacToeBoard):
    for i in winCombinations:
        sum = 0
        for j in i:
            sum += ticTacToeBoard[j]
        if sum == 3:
            return "Player 1 wins"
        if sum == -3:
            return "Player 2 wins"
    return None

print(calculateBoard(ticTacToeBoard))
printBoard(ticTacToeBoard)

