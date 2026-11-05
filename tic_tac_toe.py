import doctest

SCORE_FILE = "scoreboard.txt"
EMPTY = " "


def create_board():
    """Create an empty 3x3 board."""
    return [[EMPTY for _ in range(3)] for _ in range(3)]


def display_board(board):
    """Display the board in Tic-Tac-Toe format."""
    print()
    for row in range(3):
        print(" " + " | ".join(board[row]))
        if row < 2:
            print("---+---+---")
    print()


def count_empty(board, position=0):
    """
    Recursively count empty squares.

    >>> count_empty([[" ", "X", " "], ["O", " ", " "], ["X", "O", " "]])
    5
    """
    if position == 9:
        return 0

    row = position // 3
    col = position % 3

    if board[row][col] == EMPTY:
        return 1 + count_empty(board, position + 1)

    return count_empty(board, position + 1)


def get_occupied_squares(board):
    """Return a set of occupied (row, column) tuples."""
    occupied = set()

    for row in range(3):
        for col in range(3):
            if board[row][col] != EMPTY:
                occupied.add((row, col))

    return occupied


def check_winner(board, mark):
    """
    Check whether the given mark has won.

    >>> check_winner([["X", "X", "X"], [" ", "O", " "], ["O", " ", " "]], "X")
    True
    >>> check_winner([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]], "X")
    False
    """
    # Check rows and columns using nested loops
    for i in range(3):
        if all(board[i][j] == mark for j in range(3)):
            return True

        if all(board[j][i] == mark for j in range(3)):
            return True

    # Check both diagonals
    if all(board[i][i] == mark for i in range(3)):
        return True

    if all(board[i][2 - i] == mark for i in range(3)):
        return True

    return False


def get_move(board, player_name, mark):
    """Ask for a valid row and column, then return them as a tuple."""
    occupied = get_occupied_squares(board)

    while True:
        try:
            print(f"{player_name} ({mark}), enter your move.")
            row = int(input("Row (1-3): ")) - 1
            col = int(input("Column (1-3): ")) - 1

            if row not in range(3) or col not in range(3):
                print("Please enter numbers from 1 to 3.")
                continue

            if (row, col) in occupied:
                print("That square is already occupied. Try again.")
                continue

            return (row, col)

        except ValueError:
            print("Invalid input. Please enter a number.")


def play_round(player1, player2, scores):
    """Play one round and update the scoreboard."""
    board = create_board()
    players = [(player1, "X"), (player2, "O")]
    turn = 0

    while count_empty(board) > 0:
        display_board(board)

        name, mark = players[turn]
        row, col = get_move(board, name, mark)
        board[row][col] = mark

        if check_winner(board, mark):
            display_board(board)
            print(f"{name} wins this round!")

            scores[name] = scores.get(name, 0) + 1
            return

        turn = 1 - turn

    display_board(board)
    print("It's a draw!")


def load_scoreboard():
    """Load scores from the text file into a dictionary."""
    scores = {}

    try:
        with open(SCORE_FILE, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                try:
                    name, score = line.rsplit(",", 1)
                    scores[name] = int(score)
                except ValueError:
                    print(f"Skipping invalid scoreboard line: {line}")

    except FileNotFoundError:
        # The file will be created when the scores are saved.
        pass

    return scores


def save_scoreboard(scores):
    """Save the scoreboard dictionary to a text file."""
    try:
        with open(SCORE_FILE, "w", encoding="utf-8") as file:
            for name, score in scores.items():
                file.write(f"{name},{score}\n")

    except OSError as error:
        print("Could not save the scoreboard:", error)


def show_scoreboard(scores):
    """Display all player scores."""
    print("\n--- Scoreboard ---")

    if not scores:
        print("No scores recorded yet.")
        return

    for name, score in scores.items():
        print(f"{name}: {score} win(s)")


def get_player_names():
    """Ask for two player names."""
    while True:
        player1 = input("Enter Player 1 name: ").strip()
        player2 = input("Enter Player 2 name: ").strip()

        if not player1 or not player2:
            print("Names cannot be empty. Please try again.")
        elif player1.lower() == player2.lower():
            print("Please enter two different names.")
        else:
            return player1, player2


def show_rules():
    """Display the game rules."""
    print("\n--- Game Rules ---")
    print("1. The game is played on a 3x3 board.")
    print("2. Player 1 uses X and Player 2 uses O.")
    print("3. Players take turns choosing a row and column.")
    print("4. The first player to make a line of three wins.")
    print("5. If the board fills with no winner, the round is a draw.")


def main():
    """Run the main menu."""
    scores = load_scoreboard()

    while True:
        print("\n===== TIC-TAC-TOE =====")
        print("1. Start New Game")
        print("2. View Scoreboard")
        print("3. View Game Rules")
        print("4. Reset Scoreboard")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            player1, player2 = get_player_names()

            while True:
                play_round(player1, player2, scores)
                save_scoreboard(scores)

                again = input("Play another round? (y/n): ").strip().lower()
                if again != "y":
                    break

        elif choice == "2":
            show_scoreboard(scores)

        elif choice == "3":
            show_rules()

        elif choice == "4":
            confirm = input("Are you sure you want to reset scores? (y/n): ")
            if confirm.strip().lower() == "y":
                scores.clear()
                save_scoreboard(scores)
                print("Scoreboard has been reset.")

        elif choice == "5":
            save_scoreboard(scores)
            print("Thanks for playing!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    # Run the doctests before starting the game.
    doctest.testmod()
    main()