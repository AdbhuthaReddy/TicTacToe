from operator import iconcat

print("Hey, Welcome to the world of Tic Tac Toe. \n Let's play Tic Tac Toe.....!")
name1 = input("Enter the name of player 1: ")
name2 = input("Enter the name of player 2: ")
board = ["  " for i in range(9)]

def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):
    if icon == "x":
        print("It's your turn, " + name1)
    elif icon == "o":
        print("It's your turn, " + name2)

    choice = int(input("Enter your move (1-9): ").strip())
    if board[choice-1] == "  ":
        board[choice-1] = icon
    else:
        print("That position is occupied!!!!")
        player_move(icon)

def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
        (board[3] == icon and board[4] == icon and board[5] == icon) or \
        (board[6] == icon and board[7] == icon and board[8] == icon) or \
        (board[0] == icon and board[3] == icon and board[6] == icon) or \
        (board[1] == icon and board[4] == icon and board[7] == icon) or \
        (board[2] == icon and board[5] == icon and board[8] == icon) or \
        (board[0] == icon and board[4] == icon and board[8] == icon) or \
        (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

def is_draw():
    if "  " not in board:
        return True
    else:
        return False

print_board()
while True:
    player_move("x")
    print_board()
    if is_victory("x"):
        out1 = "Congrats {}. You have won 🥳".format(name1)
        print(out1)
        break
    elif is_draw():
        print("It's a TIE.....")
        break

    player_move("o")
    print_board()
    if is_victory("o"):
        out2 = "Congrats {}. You have won 🥳".format(name2)
        print(out2)
        break
    elif is_draw():
        print("It's a TIE.....")
        break