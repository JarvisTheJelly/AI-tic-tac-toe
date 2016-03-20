"""A tic-tac-toe program. I will be working to implement an ANN
   (Artificial Neural Network). Currently both inputs are manual."""

def print_board(brd):
    """Prints the current state of the board, brd."""

    print brd[0], brd[1], brd[2], "|", 0, 1, 2
    print brd[3], brd[4], brd[5], "|", 3, 4, 5
    print brd[6], brd[7], brd[8], "|", 6, 7, 8
    print ""

def check_if_won(brd, player):
    """Returns true if the input player has won on board, brd"""

    # List of all possible moves. Easier to code.
    possible_wins = [(0, 1, 2), (0, 3, 6), (0, 4, 8),
                     (1, 4, 7), (2, 5, 8), (2, 4, 6),
                     (3, 4, 5), (6, 7, 8)]

    for win in possible_wins:
        for position in win:
            if brd[position] != player:
                break
            if win.index(position) == 2:
                return True

    return False

def main():
    """Main code for program. Plays tic-tac-toe.
    Currently both players' moves are input manually."""

    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]

    won = False
    while not won:
        # Print the board
        print_board(board)

        # Player X play
        valid_move = False
        while not valid_move:
            move = input("Enter move: ")
            try:
                if board[move] == "-":
                    board[move] = "X"
                    valid_move = True
            except NameError:
                print "Not a valid move!"

        # Check if won
        if check_if_won(board, "X"):
            won = True
            print "X Wins!"
            continue

        # Print the board again (for player O)
        print ""
        print_board(board)

        # Player O play
        valid_move = False
        while not valid_move:
            move = input("Enter move for O: ")
            try:
                if board[move] == "-":
                    board[move] = "O"
                    valid_move = True
            except NameError:
                print "Not a valid move!"

        # Check if won
        if check_if_won(board, "O"):
            won = True
            print "O Wins!"
            continue

    print_board(board) # Print the board to show the win.

if __name__ == "__main__":
    main()
