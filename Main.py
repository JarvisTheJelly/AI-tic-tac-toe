def print_board(b):
	print b[0], b[1], b[2], "|", 0, 1, 2
	print b[3], b[4], b[5], "|", 3, 4, 5
	print b[6], b[7], b[8], "|", 6, 7, 8
	print ""

def check_if_won(b, player):
	possible_wins = [(0, 1, 2), (0, 3, 6), (0, 4, 8),
			 (1, 4, 7), (2, 5, 8), (2, 4, 6),
			 (3, 4, 5), (6, 7, 8)]
	
	for win in possible_wins:
		for position in win:
			if b[position] != player:
				break
			if win.index(position) == 2:
				return True

	return False
		
		

def main():
	board = ["-", "-", "-",
		 "-", "-", "-",
		 "-", "-", "-"]
	
	won = False
	while not won:
		print_board(board)
		# Player X play
		valid_move = False
		while not valid_move:
			move = input("Enter move: ")
			try:
				if board[move] == "-":
					board[move] = "X"
					valid_move = True
			except Exception:
				print "Not a valid move!"
		# Check if won
		if check_if_won(board, "X"):
			won = True
			print "X Wins!"
			continue
		
		print ""
		print_board(board)
		#Player O play
		valid_move = False
		while not valid_move:
			move = input("Enter move for O: ")
			try:
				if board[move] == "-":
					board[move] = "O"
					valid_move = True
			except Exception:
				print "Not a valid move!"
		# Check if won
		if check_if_won(board, "O"):
			won = True
			print "O Wins!"

	print_board(board)

if __name__ == "__main__":
	main()
