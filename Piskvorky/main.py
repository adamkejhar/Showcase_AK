def print_board(board):
    print("  A B C D E F G H")
    rows = len(board)
    columns = len(board[0])

    for j in range(columns):
        print(j + 1, end=" ")
        for i in range(rows):
            print(board[i][j], end=" ")
        print()
def convert_input_to_coordinates(input_str):
    # Convert player input, eg. 'A1', to row and column index
    col = ord(input_str[0].upper()) - ord('A')
    row = int(input_str[1]) - 1
    return col, row

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def check_winner(board, player):
    for i in range(8):
        for j in range(4):
            if board[i][j] == player and board[i][j + 1] == player and board[i][j + 2] == player and board[i][
                j + 3] == player and board[i][j + 4] == player:
                return True
    # vertikální kontrola
    for i in range(4):
        for j in range(8):
            if board[i][j] == player and board[i + 1][j] == player and board[i + 2][j] == player and board[i + 3][
                j] == player and board[i + 4][j] == player:
                return True
    # kontrola hlavní diagonály
    for i in range(4):
        for j in range(4):
            if board[i][j] == player and board[i + 1][j + 1] == player and board[i + 2][j + 2] == player and \
                    board[i + 3][j + 3] == player and board[i + 4][j + 4] == player:
                return True
    # kontrola vedlejší diagonály
    for i in range(4):
        for j in range(5, 8):
            if board[i][j] == player and board[i + 1][j - 1] == player and board[i + 2][j - 2] == player and \
                    board[i + 3][j - 3] == player and board[i + 4][j - 4] == player:
                return True
    return None



def play_game():
    current_player = 'X'
    board = [[' ' for i in range(8)] for i in range(8)]

    while True:
        print_board(board)
        user_input = input(f"Enter coordinates for player {current_player} (e.g., A1, B2) for {current_player}: ")

        if len(user_input) == 2 and user_input[0].upper() in 'ABCDEFGH' and user_input[1] in '12345678':
            row, col = convert_input_to_coordinates(user_input)

            if board[row][col] == ' ':
                board[row][col] = current_player

                if is_board_full(board):
                    print_board(board)
                    print("The board is full, game ends in a draw!")
                    break

                winner = check_winner(board, current_player)
                if winner:
                    print_board(board)
                    print(f"\n---!!! Player {current_player} is the winner!!!---\n")
                    break

                current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("\nThat position is already taken. Try again.")

        else:
            print("\nInvalid input. Please enter coordinates in the format A1, B2, etc.")

play_game()