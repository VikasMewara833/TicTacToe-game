def sum(a, b, c):
    return a + b + c

def printBoard(xState, zState):
    cells = []
    for i in range(9):
        if xState[i]:
            cells.append('X')
        elif zState[i]:
            cells.append('O')
        else:
            cells.append(str(i))
    print(f"{cells[0]} | {cells[1]} | {cells[2]}")
    print("--|---|---")
    print(f"{cells[3]} | {cells[4]} | {cells[5]}")
    print("--|---|---")
    print(f"{cells[6]} | {cells[7]} | {cells[8]}")


def checkWin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print("X Won the match")
            return 1
        if sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            print("O Won the match")
            return 0
    return -1
