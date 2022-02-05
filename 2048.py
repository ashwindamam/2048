def displayBoard(board):
    for line in board:
        print(*line, end="\n")


def startPlay():
    board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    print("-----------2048 GAME--------------")
    displayBoard(board)

def main():
    startPlay()


if __name__ == "__main__":
    main()
