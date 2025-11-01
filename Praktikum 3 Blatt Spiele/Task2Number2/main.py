ticTacToeBoard1 = [0,0,0,0,0,0,0,0,0]
comparedNodes = 0
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
        sumM = 0
        for j in i:
            sumM += ticTacToeBoard[j]
        if sumM == 3:
            return 1
        if sumM == -3:
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

# Max node function
def Max(state,alpha,beta):
    global comparedNodes
    comparedNodes += 1
    endstate = utilityFunction(state)
    if endstate is not None:
        return endstate
    bestScore = float("-inf")
    # Action and subsequent state
    emptyPositions = countEmptyPositions(state)
    for i in emptyPositions:
        # make move
        state[i] = 1
        bestScore = max(bestScore, Min(state,alpha,beta))
        # undo move
        state[i] = 0
        if bestScore >= beta:
            return bestScore
        alpha = max(alpha, bestScore)
    return bestScore

# Min node function
def Min(state,alpha,beta):
    global comparedNodes
    comparedNodes += 1
    endstate = utilityFunction(state)
    if endstate is not None:
        return endstate
    bestScore = float("+inf")
    # Action and subsequent state
    emptyPositions = countEmptyPositions(state)
    for i in emptyPositions:
        # make move
        state[i] = -1
        bestScore = min(bestScore, Max(state,alpha, beta))
        # undo move
        state[i] = 0
        if bestScore <= alpha:
            return bestScore
        beta = min(beta, bestScore)
    return bestScore

# A node represents a game state
# We play alternating and Max starts
# Edges lead to new game states
# Purpose: Result of a game if both players play perfect

# result and initial call
print(Max(ticTacToeBoard1,float("-inf"),float("+inf")))
# Compared Nodes
print(comparedNodes)