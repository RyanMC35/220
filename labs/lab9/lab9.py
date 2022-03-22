"""
Name: Ryan Campbell
lab9.py
Problem Description- create a tic tak toe game
I Ryan Campbell certify this assignment is entirely my own work.
"""
# must display instructions for the game first
import string


def build_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board


def print_board(board):
    """ prints the values of board """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    # takes board and position checks value to see if space taken and returns value
    value_number = str(board[int(position) - 1]).isnumeric()
    if value_number:
        return True
    else:
        return False


def fill_spot(board, position, character):
    board[int(position) - 1] = character.strip().lower()
    # marks space in board with x or o


def winning_game(board):
    if board[0] == "x" and board[1] == "x" and board[2] == "x":
        return True
    elif board[0] == "o" and board[1] == "o" and board[2] == "o":
        return True
    elif board[3] == "x" and board[4] == "x" and board[5] == "x":
        return True
    elif board[3] == "o" and board[4] == "o" and board[5] == "o":
        return True
    elif board[6] == "x" and board[7] == "x" and board[8] == "x":
        return True
    elif board[6] == "o" and board[7] == "o" and board[8] == "o":
        return True
    elif board[0] == "x" and board[3] == "x" and board[6] == "x":
        return True
    elif board[0] == "o" and board[3] == "o" and board[6] == "o":
        return True
    elif board[1] == "x" and board[4] == "x" and board[7] == "x":
        return True
    elif board[1] == "o" and board[4] == "o" and board[7] == "o":
        return True
    elif board[2] == "x" and board[5] == "x" and board[8] == "x":
        return True
    elif board[2] == "o" and board[5] == "o" and board[8] == "o":
        return True
    elif board[0] == "x" and board[4] == "x" and board[8] == "x":
        return True
    elif board[0] == "o" and board[4] == "o" and board[8] == "o":
        return True
    elif board[2] == "x" and board[4] == "x" and board[6] == "x":
        return True
    elif board[2] == "o" and board[4] == "o" and board[6] == "o":
        return True
    else:
        return False
    # game_is_won


def game_over(board):
    # checks if someone has won, if there are no spaces left, or if there are spaces left
    if winning_game(board):
        return True
    for i in range(0, 9):
        if str(board[i]).isnumeric():
            return False
    return True


def get_winner(board):
    # sometimes it will return none or the string of the winner x or o
    if board[0] == "x" and board[1] == "x" and board[2] == "x":
        return "x"
    elif board[0] == "o" and board[1] == "o" and board[2] == "o":
        return "o"
    elif board[3] == "x" and board[4] == "x" and board[5] == "x":
        return "x"
    elif board[3] == "o" and board[4] == "o" and board[5] == "o":
        return "o"
    elif board[6] == "x" and board[7] == "x" and board[8] == "x":
        return "x"
    elif board[6] == "o" and board[7] == "o" and board[8] == "o":
        return "o"
    elif board[0] == "x" and board[3] == "x" and board[6] == "x":
        return "x"
    elif board[0] == "o" and board[3] == "o" and board[6] == "o":
        return "o"
    elif board[1] == "x" and board[4] == "x" and board[7] == "x":
        return "x"
    elif board[1] == "o" and board[4] == "o" and board[7] == "o":
        return "o"
    elif board[2] == "x" and board[5] == "x" and board[8] == "x":
        return "x"
    elif board[2] == "o" and board[5] == "o" and board[8] == "o":
        return "o"
    elif board[0] == "x" and board[4] == "x" and board[8] == "x":
        return "x"
    elif board[0] == "o" and board[4] == "o" and board[8] == "o":
        return "o"
    elif board[2] == "x" and board[4] == "x" and board[6] == "x":
        return "x"
    elif board[2] == "o" and board[4] == "o" and board[6] == "o":
        return "o"
    else:
        return None


def play(board):
    print("Tic-Tak-Toe")
    print("Enter in an integer between 1 and 9 to choose position on board.")
    print("Type y if you wish to play and n if you do not wish to play.")
    print_board(board)
    input_user = input("Do you wish to play?")
    while input_user[0] == "y":
        i = 0
        while i <= 9 and not game_over(board):
            character = ""
            if (i % 2) == 0:
                character = character + "x"
            elif (i % 2) == 1:
                character = character + "o"
            user_input = input("{}'s, chose a position:".format(character))
            while not is_legal(board, user_input):
                user_input = input("position already filled chose a new position:")
            fill_spot(board, user_input, character)
            print_board(board)
            i = i + 1
            if game_over(board):
                if get_winner(board) == "x":
                    print("x wins!")
                elif get_winner(board) == "o":
                    print("o wins!")
                else:
                    print("Tie!")
        input_user = input("Do you wish to play again?")
        board = build_board()


def main():
    play(build_board())


if __name__ == '__main__':
    main()

