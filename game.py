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
