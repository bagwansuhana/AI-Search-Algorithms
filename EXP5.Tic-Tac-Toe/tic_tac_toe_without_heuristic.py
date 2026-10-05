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


def tic_tac_toe():
    board = [' '] * 9
    player = 'X'

    for turn in range(9):
        print_board(board)

        position = int(input(f"Player {player}, enter position (1-9): ")) - 1

        if board[position] != ' ':
            print("Position already occupied.")
            continue

        board[position] = player

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            return

        player = 'O' if player == 'X' else 'X'

    print_board(board)
    print("Game is a draw!")


tic_tac_toe()
