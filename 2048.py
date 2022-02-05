import random


def displayBoard(board):
    for line in board:
        print(*line, end="\n")


def startPlay():
    board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    print("-----------2048 GAME--------------")
    addDefault(board)
    addDefault(board)
    displayBoard(board)

def addDefault(board):
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    default = random.randint(1, 2) * 2

    if board[r][c] == 0:
        board[r][c] = default
    else:
        addDefault(board)


def main():
    startPlay()


if __name__ == "__main__":
    main()