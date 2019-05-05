from itertools import permutations

clues = [
    2, 2, 1, 3,  
    2, 2, 3, 1,  
    1, 2, 2, 3,  
    3, 2, 1, 3
]

"""
sol = [
    [1, 3, 4, 2],
    [4, 2, 1, 3],
    [3, 4, 2, 1],
    [2, 1, 3, 4]
]

"""

def solved(clues, board):
    aux_board = board.copy()
    solve(clues, aux_board)
    return aux_board

def solve(clues, board):
    next = find_empty(board)
    if not next:
        return True
    else:
        row, col = next

    for i in range(1,5):
        if valid(clues, board, i, (row,col)):
            board[row][col] = i
            if solve(clues, board):
                return True
            else:
                board[row][col] = 0

    return False

def find_empty(board):
	for i in range(len(board)):
		for j in range(len(board)):
				if board[i][j] == 0:
					return (i,j)
	return None

def valid(clues, board, num, pos):
    row = [num if i == pos[1] else board[pos[0]][x] for i, x in enumerate(range(4))]
    col = [num if i == pos[0] else board[x][pos[1]] for i, x in enumerate(range(4))]

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
    clue = clues[pos[0]+4]
    if  clue != 0 and clue not in get_possible_clues_of_incompleted_row(row[::-1]):
        return False

    # Check if num satisfy the bot clue
    clue = clues[::-1][pos[1]+4]
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
    possible_rows = []
    d = list(set([1,2,3,4]) - set([x for x in incompleted_row if x != 0]))
    for perm in permutations(d):
        row = incompleted_row.copy()
        for e in perm:
            row[row.index(0)] = e
        possible_rows.append(row)
    possible_clues = set()
    for r in possible_rows:
        possible_clues.add(get_clue_of_completed_row(r))
    return list(possible_clues)

def ini_board():
    return [[0 for i in range(4)] for i in range(4)]

def print_board(clues, board):
    print()
    for i in range(8):
        if i == 0:
            print("    {} {} {} {}".format(*clues[:4]))
        elif i == 7:
            print("    {} {} {} {}".format(*clues[7:12][::-1]))
        elif i == 1 or i == 6:
            print("   ---------")
        else:
            print("{} | {} {} {} {} | {}".format(clues[::-1][i-2],*board[i-2],clues[i+2]))


print_board(clues, ini_board())
print_board(clues, solved(clues, ini_board()))