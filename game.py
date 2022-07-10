# helper function 1:
def print_board(entries):
    line = "+---+---+---+"
    output = line
    n = 0
    for entry in entries:
        if n % 3 == 0:
            output = output + "\n| "
        else:
            output = output + " | "
        output = output + str(entry)
        if n % 3 == 2:
            output = output + " |\n"
            output = output + line
        n = n + 1
    print(output)
    print()

# helper function 2:
def game_over(b, i):
    print_board(b)
    print('GAME OVER')
    print(b[i], "has won")
    exit()

# group helper functions:
def is_row_winner(b, i):
    return board[i] == board[i+1] and board[i+1] == board[i+2]

def is_col_winner(b, i):
    return board[i] == board[i+3] and board[i+3] == board[i+6]

def is_dia1_winner(b, i): # 1 5 9
    return board[i] == board[i+4] and board[i+4] == board[i+8]

def is_dia2_winner(b, i): #  3 5 7
    return board[i] == board[i+2] and board[i+2] == board[i+4]


# game:
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
current_player = "X"

for move_number in range(1, 10):
    print_board(board)
    response = input("Where would " + current_player + " like to move? ")
    space_number = int(response) - 1
    board[space_number] = current_player

    if is_row_winner(board, 0):
        game_over(board, 0)
    elif is_row_winner(board, 3):
        game_over(board, 3)
    elif is_row_winner(board, 6):
        game_over(board, 6)
    elif is_col_winner(board, 0):
        game_over(board, 0)
    elif is_col_winner(board, 1):
        game_over(board, 1)
    elif is_col_winner(board, 2):
        game_over(board, 2)
    elif is_dia1_winner(board, 0):
        game_over(board, 0)
    elif is_dia2_winner(board, 2):
        game_over(board, 2)

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

print("It's a tie!")

