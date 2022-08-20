# CHALLENGE PROBLEM:
#
# Use your check_sudoku function as the basis for solve_sudoku(): a
# function that takes a partially-completed Sudoku grid and replaces
# each 0 cell with an integer in the range 1..9 in such a way that the
# final grid is valid.
#
# There are many ways to cleverly solve a partially-completed Sudoku
# puzzle, but a brute-force recursive solution with backtracking is a
# perfectly good option. The solver should return None for broken
# input, False for inputs that have no valid solutions, and a valid
# 9x9 Sudoku grid containing no 0 elements otherwise. In general, a
# partially-completed Sudoku grid does not have a unique solution. You
# should just return some member of the set of solutions.
#
# A solve_sudoku() in this style can be implemented in about 16 lines
# without making any particular effort to write concise code.

# solve_sudoku should return None

import random


ill_formed = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
              [6, 7, 2, 1, 9, 5, 3, 4, 8],
              [1, 9, 8, 3, 4, 2, 5, 6, 7],
              [8, 5, 9, 7, 6, 1, 4, 2, 3],
              [4, 2, 6, 8, 5, 3, 7, 9],  # <---
              [7, 1, 3, 9, 2, 4, 8, 5, 6],
              [9, 6, 1, 5, 3, 7, 2, 8, 4],
              [2, 8, 7, 4, 1, 9, 6, 3, 5],
              [3, 4, 5, 2, 8, 6, 1, 7, 9]]

# solve_sudoku should return valid unchanged
valid = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
         [6, 7, 2, 1, 9, 5, 3, 4, 8],
         [1, 9, 8, 3, 4, 2, 5, 6, 7],
         [8, 5, 9, 7, 6, 1, 4, 2, 3],
         [4, 2, 6, 8, 5, 3, 7, 9, 1],
         [7, 1, 3, 9, 2, 4, 8, 5, 6],
         [9, 6, 1, 5, 3, 7, 2, 8, 4],
         [2, 8, 7, 4, 1, 9, 6, 3, 5],
         [3, 4, 5, 2, 8, 6, 1, 7, 9]]

# solve_sudoku should return False
invalid = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
           [6, 7, 2, 1, 9, 5, 3, 4, 8],
           [1, 9, 8, 3, 8, 2, 5, 6, 7],
           [8, 5, 9, 7, 6, 1, 4, 2, 3],
           [4, 2, 6, 8, 5, 3, 7, 9, 1],
           [7, 1, 3, 9, 2, 4, 8, 5, 6],
           [9, 6, 1, 5, 3, 7, 2, 8, 4],
           [2, 8, 7, 4, 1, 9, 6, 3, 5],
           [3, 4, 5, 2, 8, 6, 1, 7, 9]]

# solve_sudoku should return a
# sudoku grid which passes a
# sudoku checker. There may be
# multiple correct grids which
# can be made from this starting
# grid.
easy = [[2, 9, 0, 0, 0, 0, 0, 7, 0],
        [3, 0, 6, 0, 0, 8, 4, 0, 0],
        [8, 0, 0, 0, 4, 0, 0, 0, 2],
        [0, 2, 0, 0, 3, 1, 0, 0, 7],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [1, 0, 0, 9, 5, 0, 0, 6, 0],
        [7, 0, 0, 0, 9, 0, 0, 0, 1],
        [0, 0, 1, 2, 0, 0, 3, 0, 6],
        [0, 3, 0, 0, 0, 0, 0, 5, 9]]

unsolvable = [[1, 2, 3, 7, 4, 5, 0, 0, 0],
        [4, 5, 6, 8, 2, 3, 0, 0, 0],
        [7, 8, 9, 6, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]


# Note: this may timeout
# in the Udacity IDE! Try running
# it locally if you'd like to test
# your solution with it.
#
hard = [[1, 0, 0, 0, 0, 7, 0, 9, 0],
        [0, 3, 0, 0, 2, 0, 0, 0, 8],
        [0, 0, 9, 6, 0, 0, 5, 0, 0],
        [0, 0, 5, 3, 0, 0, 9, 0, 0],
        [0, 1, 0, 0, 8, 0, 0, 0, 2],
        [6, 0, 0, 0, 0, 4, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 7, 0, 0, 0, 3, 0, 0]]

random1 = [[2, 4, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 6, 0, 0, 8, 0, 7, 0],
        [8, 1, 0, 0, 4, 0, 0, 0, 0],
        [0, 2, 0, 0, 3, 1, 0, 0, 7],
        [0, 0, 9, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 6, 0],
        [7, 0, 0, 0, 9, 0, 0, 0, 1],
        [0, 0, 1, 2, 0, 0, 7, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 5, 9]]

random2 = [[0, 0, 8, 0, 0, 7, 0, 0, 0],
        [0, 3, 0, 0, 6, 0, 0, 0, 8],
        [0, 0, 9, 1, 0, 0, 5, 0, 0],
        [0, 0, 5, 3, 0, 0, 9, 0, 0],
        [0, 1, 0, 0, 8, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 4, 0, 2, 0, 0, 0, 0, 7],
        [0, 0, 7, 0, 0, 0, 1, 0, 0]]

empty = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

none_empty = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, None, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

examples = [ill_formed, invalid, valid, easy, hard, random1, random2, empty]


def sanity(grid):
    if type(grid) is not list or len(grid) != 9:    # Is the grid a list of 9 "rows"?
        return None
    for row in grid:
        if type(row) is not list or len(row) != 9:  # Is each "row" a list of 9 elements?
            return None
        for element in row:
            if type(element) is not int or not 0 <= element <= 9:   # Is each element an integer between 0 and 9?
                return None
    return True


def check_sudoku(grid):

    # Sanity checking
    if sanity(grid) is None:
        return None

    # - each number in the range 1..9 occurs only once in each row
    testing = []    # array of each number we found
    for row in range(9):
        for column in range(9):
            integer = grid[row][column]
            if integer not in testing or integer == 0:  # Did we find this number in the same row already ?
                testing.append(integer)                 # no -> let's add it to the testing array
            else:
                return False                            # yes -> the grid is invalid
        testing = []                                    # resetting the array for each row

    for column in range(9):
        for row in range(9):
            integer = grid[row][column]
            if integer not in testing or integer == 0:  # Did we find this number in the same column already?
                testing.append(integer)                 # no -> let's add it to the testing array
            else:
                return False                            # yes -> the grid is invalid
        testing = []                                    # resetting the array for each column

    # - each number the range 1..9 occurs only once in each of the nine
    #   3x3 sub-grids, or "boxes", that make up the board
    down = 0                                            # initialising the row we're in
    for boxes in range(3):
        right = 0                       # once a row is completed, we check the left side first again
        for box in range(3):
            for row in range(3):
                for column in range(3):
                    integer = grid[row + (3 * down)][column + (3 * right)]
                    if integer not in testing or integer == 0:  # Did we find this number in the same box already?
                        testing.append(integer)
                    else:
                        return False
            testing = []                # resetting the array for the next box to test
            right += 1                  # testing the next box on the right
        down += 1                       # testing the next row
    return True


def solve_sudoku(grid, first=1):
    if first == 1:
        check = check_sudoku(grid)
        if check is None or check is False:     # if grid is invalid or if it isn't even a proper grid
            return check
    # Solve Sudoku
    for row in range(9):
        for column in range(9):
            if grid[row][column] == 0:
                for i in range(1, 10):
                    if i not in grid[row]:      # row check
                        if i not in (grid[0][column], grid[1][column], grid[2][column],
                                     grid[3][column], grid[4][column], grid[5][column],
                                     grid[6][column], grid[7][column], grid[8][column]):    # column check
                            if row % 3 == 0:
                                rows = (row+1, row+2)
                            elif row % 3 == 1:
                                rows = (row-1, row+1)
                            elif row % 3 == 2:
                                rows = (row-2, row-1)
                            if column % 3 == 0:
                                cols = (column + 1, column + 2)
                            elif column % 3 == 1:
                                cols = (column - 1, column + 1)
                            elif column % 3 == 2:
                                cols = (column - 2, column - 1)
                            if i not in (grid[rows[0]][cols[0]], grid[rows[0]][cols[1]],
                                         grid[rows[1]][cols[0]], grid[rows[1]][cols[1]]):   # box check
                                grid[row][column] = i
                                if solve_sudoku(grid, 0):
                                    if first == 1:
                                        return grid         # grid solved
                                    return True
                                grid[row][column] = 0       # going back to try other numbers
                return False
    if first == 1:                      # grid was full and valid
        return grid
    return True


def display_grid_solved(grid):
    solved = solve_sudoku(grid)
    if solved is None or solved is False:
        return solved
    print("---------------------------")
    for row in range(9):
        print(solved[row])
    print("---------------------------")
    return True


def random_tester(grid):
    method = random.randrange(3)
    zeros = random.uniform(0.75, 1)
    if method <= 1:
        # method 1: creating a new grid (Generative random testing)
        grid = []
        for i in range(9):
            grid.append([])
        for row in grid:
            for column in range(9):
                if random.uniform(0, 1) < zeros:
                    row.append(0)
                else:
                    row.append(random.randrange(1, 10))
    if method >= 1:
        # method 2: modifying an existing grid (Mutation-based random testing)
        repeat = random.randrange(1, 50)
        for times in range(repeat):
            if random.uniform(0, 1) < zeros:
                number = 0
            else:
                number = random.randrange(1, 10)
            x = random.randrange(len(grid))
            y = random.randrange(len(grid[x]))
            grid[x][y] = number
    return grid


#assert solve_sudoku(none_empty) is None
#assert solve_sudoku(None) is None
#assert solve_sudoku(ill_formed) is None
#assert solve_sudoku(invalid) is False
#assert display_grid_solved(easy) is True
#assert display_grid_solved(None) is None
#for ok in range(2, 8):
#    assert isinstance(solve_sudoku(examples[ok]), list)

#for test in range(1000):
#    example = random.randrange(len(examples))
#    result = random_tester(examples[example])
#    print(test, solve_sudoku(result))
print(solve_sudoku(unsolvable))
