from itertools import permutations

clues = [
    2, 2, 1, 3,  
    2, 2, 3, 1,  
    1, 2, 2, 3,  
    3, 2, 1, 3
]

ini = [[0]*4]*4

sol = [
    [1, 3, 4, 2],
    [4, 2, 1, 3],
    [3, 4, 2, 1],
    [2, 1, 3, 4]
]

def valid(clues, board, num, pos):

    # Check if num is not repeated in the row

    # Check if num is not repeated in the column

    # Check if num satisfy the top clue

    # Check if num satisfy the right clue

    # Check if num satisfy the bot clue

    # Check if num satisfy the left clue

    return True

def get_clue_of_row(row):
    v = 0
    m = 0
    for i, x in enumerate(row):
        if m < x:
            v += 1
        m = max(m, x)
    return v

def print_board(clues, board):
    print()
    for i in range(8):
        if i == 0:
            print("    {} {} {} {}".format(*clues[:4]))
        elif i == 7:
            print("    {} {} {} {}".format(*clues[::-1][7:12]))
        elif i == 1 or i == 6:
            print("   ---------")
        else:
            print("{} | {} {} {} {} | {}".format(clues[::-1][i-2],*board[i-2],clues[i+2]))

print_board(clues, ini)
