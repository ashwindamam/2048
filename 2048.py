import random

board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

def displayBoard():
    addDefault()
    for line in board:
        print(*line, end="\n")

def game_over():
    print("GAME OVER !.. you lose")
    exit()


def startPlay():
    print("-----------2048 GAME--------------")
    addDefault()
    displayBoard()
    win = True
    while win:
        try:
            print("\nFollowing are the directions: 1=LEFT , 2=RIGHT , 3=UP , 4=DOWN")
            direction = int(input("what is your direction\t"))
            if direction == 1:
                sumLeft()
                displayBoard()
            elif direction == 2:
                sumRight()
                displayBoard()
            elif direction == 3:
                sumUp()
                displayBoard()
            elif direction == 4:
                sumDown()
                displayBoard()
            else:
                print("DIRECTION NOT DEFINED ! RE-ENTER !")
        except ValueError:
            print("WRONG INPUT. PLEASE TYPE AGAIN!")
        for i in range(4):
            for j in range(4):
                if board[i][j] == 2048:
                    print("CONGRATULATIONS !!!! YOU WON")
                    win = False


def addDefault():
    gameOver = True
    for i in range(4):
        if board[i].count(0) != 0:
            gameOver = False
    if gameOver:
        game_over()
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    default = random.randint(1, 2) * 2

    if board[r][c] == 0:
        board[r][c] = default
    else:
        addDefault()


def swipeLeft():
    for i in range(4):
        for j in range(1, 4):
            if board[i][j] != 0 and j == 1:
                if board[i][0] == 0:
                    board[i][0] = board[i][j]
                    board[i][j] = 0
            if board[i][j] != 0 and j == 2:
                if board[i][1] == 0:
                    board[i][1] = board[i][j]
                    board[i][j] = 0
                if board[i][0] == 0:
                    board[i][0] = board[i][1]
                    board[i][1] = 0
            if board[i][j] != 0 and j == 3:
                if board[i][2] == 0:
                    board[i][2] = board[i][j]
                    board[i][j] = 0
                if board[i][1] == 0:
                    board[i][1] = board[i][2]
                    board[i][2] = 0
                if board[i][0] == 0:
                    board[i][0] = board[i][1]
                    board[i][1] = 0


def sumLeft():
    swipeLeft()
    for i in range(4):
        for j in range(1, 4):
            if board[i][j] == board[i][j - 1]:
                board[i][j - 1] = board[i][j] + board[i][j - 1]
                board[i][j] = 0
    swipeLeft()


def sumRight():
    for i in range(4):
        board[i].reverse()
    sumLeft()
    for i in range(4):
        board[i].reverse()


def swipeDown():
    for i in range(2, -1, -1):
        for j in range(4):
            if board[i][j] != 0 and i == 2:
                if board[3][j] == 0:
                    board[3][j] = board[i][j]
                    board[i][j] = 0
            if board[i][j] != 0 and i == 1:
                if board[2][j] == 0:
                    board[2][j] = board[i][j]
                    board[i][j] = 0
                if board[3][j] == 0:
                    board[3][j] = board[2][j]
                    board[2][j] = 0
            if board[i][j] != 0 and i == 0:
                if board[1][j] == 0:
                    board[1][j] = board[i][j]
                    board[i][j] = 0
                if board[2][j] == 0:
                    board[2][j] = board[1][j]
                    board[1][j] = 0
                if board[3][j] == 0:
                    board[3][j] = board[2][j]
                    board[2][j] = 0


def sumDown():
    swipeDown()
    for i in range(2, -1, -1):
        for j in range(4):
            if board[i][j] == board[i + 1][j]:
                board[i + 1][j] = board[i][j] + board[i + 1][j]
                board[i][j] = 0
    swipeDown()


def sumUp():
    board.reverse()
    sumDown()
    board.reverse()


def main():
    startPlay()


if __name__ == "__main__":
    main()