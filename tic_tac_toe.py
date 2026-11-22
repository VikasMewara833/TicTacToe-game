# TIC TAC TOE GAME - GROUP 14

FILE = "scoreboard.txt"


# Read previously saved player scores from the file
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


# Save updated player scores permanently in the file
def save_scores(scores):
    with open(FILE, "w") as f:
        for name, score in scores.items():
            f.write(name + "|" + str(score) + "\n")
    return True


# Display the current Tic Tac Toe board
def show_board(board):
    print("\n-------------")
    for row in board:
        for cell in row:
            print(cell, end=" | ")
        print("\n-------------")
    return board


# Check all rows, columns and diagonals for a winning combination

def check_winner(board, mark):
    for i in range(3):
        row = True
        col = True

        for j in range(3):
            if board[i][j] != mark:
                row = False
            if board[j][i] != mark:
                col = False

        if row or col:
            return True

    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True

    if board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
        return True

    return False


# Count empty spaces using recursion
def count_empty(board, index=0):
    if index == 9:
        return 0

    row = index // 3
    col = index % 3

    if board[row][col] not in ("X", "O"):
        return 1 + count_empty(board, index + 1)

    return count_empty(board, index + 1)


# Play one round
def play_game(p1, p2, scores):
    board = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]

    taken = set()
    moves = []
    players = ((p1, "X"), (p2, "O"))
    turn = 0

    while count_empty(board) > 0:
        show_board(board)

        name, mark = players[turn]
        pos = input(name + " (" + mark + "), enter position: ").strip()

        if not pos.isdigit() or int(pos) < 1 or int(pos) > 9:
            print("Invalid input! Enter 1 to 9.")
            continue

        pos = int(pos)
        row = (pos - 1) // 3
        col = (pos - 1) % 3

        move = (row, col)

        if move in taken:
            print("Position already taken!")
            continue

        taken.add(move)
        moves.append(move)
        board[row][col] = mark

        if check_winner(board, mark):
            show_board(board)
            print(name, "WINS!")
            scores[name] = scores.get(name, 0) + 1
            return scores

        turn = 1 - turn

    show_board(board)
    print("MATCH DRAW!")
    return scores


# Display scoreboard
def show_scoreboard(scores):
    print("\n===== SCOREBOARD =====")

    ranking = list(scores.items())
    ranking.sort(key=lambda x: x[1], reverse=True)

    for name, score in ranking:
        print(name, ":", score)

    return ranking


# Remove player score
def remove_player(scores):
    name = input("Enter player name: ").strip().title()

    if name in scores:
        scores.pop(name)
        print("Player removed!")
    else:
        print("Player not found!")

    return scores


# Main program
def main():
    scores = load_scores()

    p1 = input("Enter Player 1 name: ").strip().title()
    p2 = input("Enter Player 2 name: ").strip().title()

    while not p1 or not p2 or p1 == p2:
        print("Enter two different names!")
        p1 = input("Player 1: ").strip().title()
        p2 = input("Player 2: ").strip().title()

    print("\nWelcome", " vs ".join([p1, p2]))

    while True:
        print("\n===== MAIN MENU =====")
        print("1. Play Game")
        print("2. Show Scoreboard")
        print("3. Remove Player")
        print("4. Exit")

        choice = input("Enter choice: ").strip().lower()

        try:
            if choice == "1":
                scores = play_game(p1, p2, scores)
                save_scores(scores)

            elif choice == "2":
                show_scoreboard(scores)

            elif choice == "3":
                scores = remove_player(scores)
                save_scores(scores)

            elif choice == "4":
                save_scores(scores)
                print("Thanks for playing!")
                break

            else:
                print("Invalid choice!")

        except (ValueError, OSError):
            print("Something went wrong. Try again!")


main()
