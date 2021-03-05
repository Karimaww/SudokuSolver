# Board size
BOARD_SIZE = 9

board = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]

# Searching an empty cell function
def FindEmptyCell(board):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == 0:
                return i,j
    return None

def isValidNumber(board, line, column, number):
    for iter in range(BOARD_SIZE):
        #Checking line
        if column != iter and board[line][iter] == number:
            return False
        #Checking column
        if line != iter and board[iter][column] == number:
            return False

    #Coordinates in which block the number is
    boardX = column // 3
    boardY = line // 3

    #Checking block
    for i in range(boardY*3, boardY*3+3):
        for j in range(boardX*3, boardX*3+3):
            if board[i][j] == number and (i, j) != (line, column):
                return False

    return True

def SudokuSolver(board):
    find = FindEmptyCell(board)
    #Board is completed and there are not any empty cell
    if not find:
        return True
    else:
        #Return empty cell position
        line, column = find
    for i in range(1, 10):
        if isValidNumber(board, line, column, i):
            board[line][column] = i

            if SudokuSolver(board):
                return True

            board[line][column] = 0
    return False


def PrintBoard(board):
    for i in range(BOARD_SIZE):
        if i%3 == 0 and i!=0:
            print("-----------------------")
        for j in range(BOARD_SIZE):
            if j%3 == 0 and j!=0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

print(" Our Sudoku Board: ")
PrintBoard(board)
if not SudokuSolver(board):
    print(" There are not any possible solution! ")
print(" Solution: ")
PrintBoard(board)
