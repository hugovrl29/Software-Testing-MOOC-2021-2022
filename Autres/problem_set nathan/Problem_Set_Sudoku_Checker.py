def check_sudoku(grid):

    # Sanity checking
    if type(grid) is not list or len(grid) != 9:    # Is the grid a list of 9 "rows"?
        return None
    for row in grid:
        if type(row) is not list or len(row) != 9:  # Is each "row" a list of 9 elements?
            return None
        for element in row:
            if type(element) is not int or not 0 <= element <= 9:   # Is each element an integer between 0 and 9?
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
