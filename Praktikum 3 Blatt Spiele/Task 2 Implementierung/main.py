ticTacToeBoard1 = [0,0,0,0,0,0,0,0,0]
# Given Tic-Tac-Toe boards for test purposes
ticTacToeBoard2 = [1,0,0,0,1,0,0,0,0]
ticTacToeBoard3 = [0,0,0,0,-1,0,0,0,-1]

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
    print()

def utilityFunction(ticTacToeBoard):
    for i in winCombinations:
        sum = 0
        for j in i:
            sum += ticTacToeBoard[j]
        if sum == 3:
            return 1
        if sum == -3:
            return -1
    if 0 not in ticTacToeBoard:
        return 0
    return None

def countEmptyPositions(state):
    emptyPositions = []
    for j in range(len(state)):
        if state[j] == 0:
            emptyPositions.append(j)
    return emptyPositions

# Max Node
def Max(state):
    endstate = utilityFunction(state)
    if endstate is not None:
        return endstate
    bestScore = float("-inf")
    # Action and subsequent state
    emptyPositions = countEmptyPositions(state)
    for i in emptyPositions:
        state[i] = 1
        bestScore = max(bestScore, Min(state))
        state[i] = 0
    return bestScore

# Min node function
def Min(state):
    endstate = utilityFunction(state)
    if endstate is not None:
        return endstate
    bestScore = float("+inf")
    # Action and subsequent state
    emptyPositions = countEmptyPositions(state)
    for i in emptyPositions:
        state[i] = -1
        bestScore = min(bestScore, Max(state))
        state[i] = 0
    return bestScore

# A node represents a game state
# We play alternating and Max starts
# Edges lead to new game states
# Purpose: Result of a game if both players play perfect

printBoard(ticTacToeBoard1)
# result 1
print(Max(ticTacToeBoard1))

printBoard(ticTacToeBoard2)
# result 2
print(Max(ticTacToeBoard2))

printBoard(ticTacToeBoard3)
# result 3
print(Max(ticTacToeBoard3))

