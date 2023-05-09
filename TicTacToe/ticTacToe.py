import os

grid = [[' ', '|', ' ', '|', ' '],
           ['-', '+', '-', '+', '-'],
           [' ', '|', ' ', '|', ' '],
           ['-', '+', '-', '+', '-'],
           [' ', '|', ' ', '|', ' ']]

players = ['X', 'O']

def main():
    try:
        x = int(input('1 or 2 player? '))
    except KeyboardInterrupt:
        print('Program executed')
        return
    except:
        print('Enter a 1 or a 2')
        main()
    if x == 2:
        ticTacToe()
    elif x == 1:
        printMap()
    else:
        print('Enter 1 or 2')
        main()

def ticTacToe():
    printMap()
    print('Player 1 starts')
    winner = 0
    counter = False
    while(winner == 0):
        coordinates = convertMoveToCoordinate(getUserInput(counter))
        if checkCoordinates(coordinates):
            grid[coordinates[0]][coordinates[1]] = ['O','X'][counter == 0]
            counter = not counter
        winner = checkForWinner()
        printMap()
    if winner == 3:
        print("It's a Tie")
    else:
        print(f'Player {winner} won!')

def getUserInput(playerNumber):
    move = ''
    while not(checkUserInput(move)):
        move = input(f"Enter player {playerNumber + 1}'s move (1-9): ")
    return int(move)

def checkUserInput(string:str):
    if not(string.isdigit()):
        return 0
    else:
        return int(string) >= 0 and int(string) < 10

def convertMoveToCoordinate(move):
    return [[4, 2, 0][-(-move // 3) - 1], [4, 0, 2][move % 3]] if move in list(range(0,10)) else 0
    # validMoves = list(range(0,9))
    # if (move in validMoves):
    #     #return [[4,0],[4,2],[4,4],[2,0],[2,2],[2,4],[0,0],[0,2],[0,4]][move-1]
    #     return [[4, 2, 0][-(-move // 3) - 1], [4, 0, 2][move % 3]]

def checkCoordinates(coordinates):
    return grid[coordinates[0]][coordinates[1]] == ' '

def checkForWinner():
    return next((func() for func in [checkRow, checkColumn, checkDiagonal, boardIsFull] if func()), 0)

    # for function in checks:
    #     if function():
    #         return function()

def boardIsFull():
    return next((0 for row in grid if next((0 for item in row if item == ' '), None) is not None), 3)

def checkRow():
    return getPlayerNumber(next((grid[i][0] for i in [0,2,4] if (len(set(grid[i][0:5:2])) == 1 and grid[i][0] in players)),''))
    # for i in range(0,5,2):
    #     if all([item == grid[i][0] != ' ' for item in grid[i][2:5:2]]):
    #         return getPlayerNumber(grid[i][0])

def checkColumn():
    return getPlayerNumber(next((grid[0][i] for i in [0,2,4] if (len(set(row[i] for row in grid[0:5:2])) == 1 and grid[0][i] in players)), ''))
    
    # player = ''
    # if grid[0][0] == grid[2][0] and grid[0][0] == grid[4][0] and grid[0][0] in players:
    #     player = grid[0][0]
    # elif grid[0][2] == grid[2][2] and grid[0][2] == grid[4][2] and grid[0][2] in players:
    #     player = grid[0][2]
    # elif grid[0][4] == grid[2][4] and grid[0][4] == grid[4][4] and grid[0][4] in players:
    #     player = grid[0][4]
    # return getPlayerNumber(player)

def checkDiagonal():
    player = ''
    if grid[0][0] == grid[2][2] and grid[0][0] == grid[4][4] and grid[0][0] in players:
        player = grid[0][0]
    elif grid[4][0] == grid[2][2] and grid[4][0] == grid[0][4] and grid[4][0] in players:
        player = grid[4][0]
    return getPlayerNumber(player)

def getPlayerNumber(playerChar):
    if playerChar == 'X':
        return 1
    elif playerChar == 'O':
        return 2
    else:
        return 0

def printMap():
    os.system('cls')
    for item in grid:
        print(" ".join(item))

if __name__ == "__main__":
    main()
