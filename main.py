import math

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def evaluate(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return 1 if board[i][0] == 'X' else -1
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return 1 if board[0][i] == 'X' else -1

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return 1 if board[0][0] == 'X' else -1

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return 1 if board[0][2] == 'X' else -1

    # Check for a tie
    for row in board:
        for cell in row:
            if cell == ' ':
                return 0  # Game not over

    return 0.5  # Tie

def minimax(board, depth, maximizing_player):
    score = evaluate(board)

    if score != 0:
        return score

    if maximizing_player:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval

    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)

        player_row = int(input("Enter row (0, 1, or 2): "))
        player_col = int(input("Enter column (0, 1, or 2): "))

        if board[player_row][player_col] == ' ':
            board[player_row][player_col] = 'O'
        else:
            print("Cell already occupied. Try again.")
            continue

        result = evaluate(board)
        if result != 0:
            print_board(board)
            if result == 1:
                print("You win!")
            elif result == -1:
                print("You lose!")
            else:
                print("It's a tie!")
            break

        print("Computer's turn...")
        computer_row, computer_col = find_best_move(board)
        board[computer_row][computer_col] = 'X'

        result = evaluate(board)
        if result != 0:
            print_board(board)
            if result == 1:
                print("You win!")
            elif result == -1:
                print("You lose!")
            else:
                print("It's a tie!")
            break

if __name__ == "__main__":
    main()
