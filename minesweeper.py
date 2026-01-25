import random

def CreateBoard(x, y, nullChar): # Takes int values in, returns an array
    nullFillValue = " "
    finalBoard = [[nullChar] * (x+2)]
    for yVal in range(0, y):
        toAdd = [nullChar]
        for xVal in range(0, x):
            toAdd.append("0")
        toAdd.append(nullChar)
        finalBoard.append(toAdd)
    finalBoard.append([nullChar] * (x+2))
    print(finalBoard)
    return(finalBoard)

def GetValuesAround(board, x, y, mineChar):
    minesAround = 0
    for xDiff in range(-1, 2):
        for yDiff in range(-1, 2):
            if board[x + xDiff][y + yDiff] == mineChar:
                minesAround += 1
    return(minesAround)
            

def PopulateBoard(board, mineNumber, x, y, mineChar):
    print(board[1][1], "!")
    if x * y < mineNumber:
        mineNumber = x*y
    for i in range(0, mineNumber):
        lookingForMine = True
        while lookingForMine:
            randomCoords = [random.randint(1, y), random.randint(1, x)]
            if board[randomCoords[0]][randomCoords[1]] != mineChar:
                board[randomCoords[0]][randomCoords[1]] = mineChar
                lookingForMine = False
    for xCell in range(1, x+1):
        for yCell in range(1, y+1):
            if board[yCell][xCell] != mineChar:
                board[yCell][xCell] = str(GetValuesAround(board, yCell, xCell, mineChar))
                
    return(board)

def PrintDebugBoard(board):
    yDim = len(board)
    xDim = len(board[0])
    output = ""
    for y in range(0, yDim):
        newRow = ""
        for x in range(0, xDim):
            newRow += board[y][x]
        newRow += "\n"
        output += newRow
    print(output)

def PrintRealBoard(board, revealedTiles):
    yDim = len(board)
    xDim = len(board[0])
    output = ""
    for y in range(1, yDim-1):
        newRow = ""
        for x in range(1, xDim-1):
            if [x, y] in revealedTiles:
                newRow += board[y][x]
            else:
                newRow += "."
        newRow += "\n"
        output += newRow
    print(output)

def CheckAnswer(board, x, y, revealedTiles, mineChar):
    if board[x][y] == mineChar:
        return(False, [0,0])
    elif board[x][y] != 0:
        return(True, [x, y])
    else:
        return(True, [x, y])
                
            

def CheckSurroundingValues(board, tile):
    pass

def Main():
    mineNumber = 5
    mineChar = "*"
    nullChar = "/"
    revealedTiles = []
    x = 5
    y = 10
    finalBoard = CreateBoard(x, y, nullChar)
    PrintDebugBoard(finalBoard)
    finalBoard = PopulateBoard(finalBoard, mineNumber, x, y, mineChar)
    playing = True
    while playing:
        PrintRealBoard(finalBoard, revealedTiles)
        guessX = int(input("X Row Guess? Must be between 1 and "+str(x)))
        guessY = int(input("Y Row Guess? Must be between 1 and "+str(y)))
        answers = CheckAnswer(finalBoard, guessX, guessY, revealedTiles, mineChar)
        playing = answers[0]
        revealedTiles.append(answers[1])
    PrintDebugBoard(finalBoard)

Main()
