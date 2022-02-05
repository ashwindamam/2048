import random


board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


def displayBoard():
    addDefault()
    for line in board:
        print(*line, end="\n")


def startPlay():
    
    print("-----------2048 GAME--------------")
    addDefault()
    displayBoard()
    win = True
    while win:
        print("\nFollowing are the directions: 1=LEFT , 2=RIGHT ")
        direction = int(input("what is your direction\t"))
        if direction == 1:
            sumLeft()
            displayBoard()
        elif direction == 2:
            sumRight()
            displayBoard()


def addDefault():
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


def main():
    startPlay()


if __name__ == "__main__":
    main()