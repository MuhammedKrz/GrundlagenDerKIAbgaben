ticTacToeBoard = []
print("Bitte geben Sie die Größe der Tic-Tac-Toe Matrix ein:")
name = input()
input_a = int(name)

if input_a > 2:
    for i in range(input_a * input_a):
        ticTacToeBoard.append("#")

    for i in range(len(ticTacToeBoard)):
        if i % input_a == 0 and i != 0:
            print()
        print(ticTacToeBoard[i], end=" ")
else:
    print("Bitte geben Sie eine größere Matrixgröße an!")

