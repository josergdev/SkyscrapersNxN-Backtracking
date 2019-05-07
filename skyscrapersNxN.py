from itertools import permutations

def solved(clues, board):
	aux_board = board.copy()
	solve(clues, aux_board)
	return aux_board

def solve(clues, board):
	n = len(board)
	next = find_empty(board)
	if not next:
		return True
	else:
		row, col = next

	for i in range(1,n+1):
		if valid(clues, board, i, (row,col)):
			board[row][col] = i
			if solve(clues, board):
				return True
			else:
				board[row][col] = 0

	return False

def find_empty(board):
	n = len(board)
	for i in range(n):
		for j in range(n):
			if board[i][j] == 0:
				return (i,j)
	return None

def valid(clues, board, num, pos):
	n = len(board)
	row = [num if i == pos[1] else board[pos[0]][i] for i in range(n)]
	col = [num if i == pos[0] else board[i][pos[1]] for i in range(n)]

	# Check if num is not repeated in the row
	if row.count(num) > 1:
		return False

	# Check if num is not repeated in the column
	if col.count(num) > 1:
		return False
	
	# Check if num satisfy the top clue
	clue = clues[pos[1]]
	if clue != 0 and clue not in get_possible_clues_of_incompleted_row(col):
		return False

	# Check if num satisfy the right clue
	clue = clues[pos[0]+n]
	if  clue != 0 and clue not in get_possible_clues_of_incompleted_row(row[::-1]):
		return False

	# Check if num satisfy the bot clue
	clue = clues[::-1][pos[1]+n]
	if clue != 0 and clue not in get_possible_clues_of_incompleted_row(col[::-1]):
		return False

	# Check if num satisfy the left clue
	clue = clues[::-1][pos[0]]
	if  clue != 0 and clue not in get_possible_clues_of_incompleted_row(row):
		return False
	
	return True

def get_clue_of_completed_row(row):
	v = 0
	m = 0
	for x in row:
		if m < x:
			v += 1
		m = max(m, x)
	return v

def get_possible_clues_of_incompleted_row(incompleted_row):
	n = len(incompleted_row)
	possible_rows = []
	d = list(set([x for x in range(1,n+1)]) - set([x for x in incompleted_row if x != 0]))
	for perm in permutations(d):
		row = incompleted_row.copy()
		for e in perm:
			row[row.index(0)] = e
		possible_rows.append(row)
	possible_clues = set()
	for r in possible_rows:
		possible_clues.add(get_clue_of_completed_row(r))
	return list(possible_clues)

def ini_board(n):
	return [[0 for i in range(n)] for i in range(n)]

def print_board(clues, board):
	n = len(board)
	print()
	for i in range(n+4):
		if i == 0:
			print("    {}".format(" ".join(str(x) for x in clues[:n])))
		elif i == n+3:
			print("    {}".format(" ".join(str(x) for x in clues[n*2:n*3][::-1])))
		elif i == 1 or i == n+2:
			print("   {}".format("".join("-" for x in range(n*2+1))))
		else:
			print("{} | {} | {}".format(clues[::-1][i-2], " ".join(str(x) for x in board[i-2]), clues[i+n-2]))
