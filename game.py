def sum_line(a, b, c):
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
        if sum_line(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print("X Won the match")
            return 1
        if sum_line(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            print("O Won the match")
            return 0
    return -1

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1  # 1 for X and 0 for O
    print("Welcome to Tic Tac Toe")
    while True:
        printBoard(xState, zState)
        if turn == 1:
            print("X's Chance")
            value = int(input("Please enter a value: "))
            xState[value] = 1
        else:
            print("O's Chance")
            value = int(input("Please enter a value: "))
            zState[value] = 1
        cwin = checkWin(xState, zState)
        if cwin != -1:
            print("Match over")
            break
        turn = 1 - turn


