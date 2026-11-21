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

def get_move(mark):
    while True:
        value = input(f"{mark}, enter a position (0-8): ").strip()
        if not value.isdigit() or int(value) > 8:
            print("Invalid input! Enter a number from 0 to 8.")
            continue
        return int(value)

def get_move(mark, xState, zState):
    while True:
        value = input(f"{mark}, enter a position (0-8): ").strip()
        if not value.isdigit() or int(value) > 8:
            print("Invalid input! Enter a number from 0 to 8.")
            continue
        value = int(value)
        if xState[value] or zState[value]:
            print("Position already taken!")
            continue
        return value

def is_draw(xState, zState):
    for i in range(9):
        if not xState[i] and not zState[i]:
            return False
    return True
        if is_draw(xState, zState):
            printBoard(xState, zState)
            print("MATCH DRAW!")
            break

def play_game(p1, p2, scores):
    xState = [0] * 9
    zState = [0] * 9
    turn = 1  # 1 for X (p1), 0 for O (p2)

    while True:
        printBoard(xState, zState)
        if turn == 1:
            value = get_move("X", xState, zState)
            xState[value] = 1
        else:
            value = get_move("O", xState, zState)
            zState[value] = 1

        result = checkWin(xState, zState)
        if result != -1:
            printBoard(xState, zState)
            winner = p1 if result == 1 else p2
            print(winner, "WINS!")
            scores[winner] = scores.get(winner, 0) + 1
            return scores

        if is_draw(xState, zState):
            printBoard(xState, zState)
            print("MATCH DRAW!")
            return scores

        turn = 1 - turn


if __name__ == "__main__":
    play_game("Player 1", "Player 2", {})

FILE = "scoreboard.txt"

def load_scores():
    scores = {}
    try:
        with open(FILE, "r") as f:
            for line in f:
                data = line.strip().split("|")
                if len(data) == 2 and data[1].isdigit():
                    scores[data[0]] = int(data[1])
    except FileNotFoundError:
        pass
    return scores

def save_scores(scores):
    with open(FILE, "w") as f:
        for name, score in scores.items():
            f.write(name + "|" + str(score) + "\n")

def show_scoreboard(scores):
    print("\n===== SCOREBOARD =====")
    ranking = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for name, score in ranking:
        print(name, ":", score)




