def print_board(board):
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i + 1], "|", board[i + 2])
        if i < 6:
            print("--+---+--")


def check_winner(board, player):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


def find_best_move(board, player, opponent):
    # Heuristic 1: Try to win
    for i in range(9):
        if board[i] == ' ':
            board[i] = player

            if check_winner(board, player):
                board[i] = ' '
                return i

            board[i] = ' '

    # Heuristic 2: Block opponent
    for i in range(9):
        if board[i] == ' ':
            board[i] = opponent

            if check_winner(board, opponent):
                board[i] = ' '
                return i

            board[i] = ' '

    # Heuristic 3: Take center
    if board[4] == ' ':
        return 4

    # Heuristic 4: Take a corner
    for i in [0, 2, 6, 8]:
        if board[i] == ' ':
            return i

    # Heuristic 5: Take any empty position
    for i in range(9):
        if board[i] == ' ':
            return i

    return -1


def tic_tac_toe():
    board = [' '] * 9

    for turn in range(9):
        print_board(board)

        if turn % 2 == 0:
            position = int(input("Player X, enter position (1-9): ")) - 1

            if board[position] != ' ':
                print("Position already occupied.")
                continue

            board[position] = 'X'

            if check_winner(board, 'X'):
                print_board(board)
                print("Player X wins!")
                return

        else:
            position = find_best_move(board, 'O', 'X')
            board[position] = 'O'

            print("Computer selected:", position + 1)

            if check_winner(board, 'O'):
                print_board(board)
                print("Computer wins!")
                return

    print_board(board)
    print("Game is a draw!")


tic_tac_toe()
