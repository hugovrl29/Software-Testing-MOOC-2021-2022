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

from copy import deepcopy
import random, time

grids = {
    'Number Missing': [  # -> None
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9],  # <---
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ],

    'Valid': [  # -> True
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ],

    'Invalid': [  # -> False
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 8, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ],

    'Easy': [  # -> True
        [2, 9, 0, 0, 0, 0, 0, 7, 0],
        [3, 0, 6, 0, 0, 8, 4, 0, 0],
        [8, 0, 0, 0, 4, 0, 0, 0, 2],
        [0, 2, 0, 0, 3, 1, 0, 0, 7],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [1, 0, 0, 9, 5, 0, 0, 6, 0],
        [7, 0, 0, 0, 9, 0, 0, 0, 1],
        [0, 0, 1, 2, 0, 0, 3, 0, 6],
        [0, 3, 0, 0, 0, 0, 0, 5, 9]
    ],

    'Hard': [  # -> True
        [1, 0, 0, 0, 0, 7, 0, 9, 0],
        [0, 3, 0, 0, 2, 0, 0, 0, 8],
        [0, 0, 9, 6, 0, 0, 5, 0, 0],
        [0, 0, 5, 3, 0, 0, 9, 0, 0],
        [0, 1, 0, 0, 8, 0, 0, 0, 2],
        [6, 0, 0, 0, 0, 4, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 7, 0, 0, 0, 3, 0, 0]
    ]
}


def check_sudoku(grid):
    """Determine whether a given sudoku grid is valid and correct.

    To be valid, a grid must be a 9x9 list of lists made of ints in the range 0..9.

    To be correct, a grid must respect the following rules:
    * each number in the range 1..9 occurs only once in each row;
    * each number in the range 1..9 occurs only once in each column;
    * each number the range 1..9 occurs only once in each of the nine 3x3 sub-grids, or "boxes", that make up the board.

    :param grid: the grid to check
    :return: None if the grid is invalid, False if it's incorrect and True otherwise
    """
    # Check validity
    if not isinstance(grid, list) or len(grid) != 9:                                # Checking if the grids is an instance of list and that the length of the gris is 9
        return None                                                                 # Otherwise return None (First return case)

    for row in grid:                                                                # Checking each row on the grid
        if not isinstance(row, list) or len(row) != 9 or \
                any(number not in range(10) for number in row):                     # If each row is not an instance of a list or if the length of the row not 9 or if there is any number higher than 10 in the row
            return None                                                             # Then it return None (First return case)

    # To keep track of the numbers we are checking, we are going to use sets
    # If a number is already found in a given set then it will return False
    # As the grid would be incorrect (2 same numbers on the same row/subgrid/column)
    column_numbers = [set() for i in range(9)]                                      # Making a list of 9 sets (9 columns)
    subgrid_numbers = [                                                             # Making a subgrid display to keep track later the numbers in each subgrid
        [set(), set(), set()],
        [set(), set(), set()],
        [set(), set(), set()]
    ]

    for row_index, row in enumerate(grid):                                          # Looping through each grid and getting the lists of row
        row_numbers = set()                                                         

        for column_index, number in enumerate(row):                                 # Looping throught the column by getting the row values => We loop horizontally
            if number in row_numbers or \
                    number in column_numbers[column_index] or \
                    number in subgrid_numbers[row_index // 3][column_index // 3]:   # Here we check if the number is already in a colum, a row or in a subgrid. To get the good subgrid, we divide by 3 because there a 3 colums in a subgrid, so dividing by 3 gives us the right subgrid index
                return False                                                        # Return False if any of those conditions are true, which means the grid is incorrect but not invalid.

            if number != 0:
                row_numbers.add(number)                                             # Here we keep track of the row values of the number we just tested
                column_numbers[column_index].add(number)                            # Here we keep track of the column values of the number we just tested
                subgrid_numbers[row_index // 3][column_index // 3].add(number)      # Here we keep track of the subgrid values of the number we just tested
    return True                                                                     # Returning true meaning the grid is correct


def solve_sudoku(original_grid):
    """Solve an incomplete sudoku grid.

    In an incomplete grid, empty cells are represented by zeroes.

    Also note that the original grid stays untouched: a new one is created when solved.

    :param original_grid: the grid to solve
    :return: None if the grid is invalid, False if it's incorrect or a resolved grid otherwise
    """
    # Simple, naive and unefficient backtracking algorithm
    # (based on https://en.wikipedia.org/wiki/Sudoku_solving_algorithms)

    # Ensure that the input grid is valid and correct
    check = check_sudoku(original_grid)
    if not check:
        return check

    # Solve it
    grid = deepcopy(original_grid)                                                  # We get a copy of the grid to solve

    empty_cells = []                                                                # Stack to track last visited empty cells
    cell_found = False                                                              # Whether the algorithm is searching for an empty cell or not

    row_index = 0                                                                       
    while row_index < 9:                                                            # Looping throught the rows

        column_index = 0
        while column_index < 9:                                                     # Looping throught the columns

            if cell_found or grid[row_index][column_index] == 0:                    # Checking into the grid if we have already found a cell or if the cell in the grid is equals to 0
                cell_found = True                                                   # In which case you have found a cell

                if grid[row_index][column_index] < 9:                               # Trying every number for this cell
                    grid[row_index][column_index] += 1                              # By adding one to the actual cell number

                    if check_sudoku(grid):                                          # Now we recheck the new grid to see if it's still valid
                        empty_cells.append((row_index, column_index))               # If so, we keep track of that number we just tested and add it to the stack
                        cell_found = False                                          # We then do it multiple times
                        column_index += 1                                           # For each column

                else:
                    grid[row_index][column_index] = 0                               # If we can't find a solution, we go back from the beginning
                    row_index, column_index = empty_cells.pop()                     # And we go to the previous solution to change it by iterating from the previous solution

            else:
                column_index += 1                                                   # Checking an other column by adding one to the column index

        row_index += 1                                                              # Checking an other row by adding one to the row index
    return grid                                                                     # We reached the end of grid


def print_grid(grid):
    """Print a valid sudoku grid.

    :param grid: the grid to display (must be valid)
    """
    for i, row in enumerate(grid):
        print(' {} {} {} | {} {} {} | {} {} {} '.format(*row))                      # Unpack the row to fit the format slots
        if i == 2 or i == 5:
            print('-------+-------+-------')


#This function generate randomly a valid completed sudoku
def generate_sudoku_grid():
    grid = [[]]*9                                                                   # Generating an empty grid
    for i in range(9):                                                              # Looping throught the grid
        grid[i] = [0]*9                                                             # Filling the grid with zeroes
    grid[0] = [i for i in range(1, 10)]                                             # Filling the first row with numbers from 1 - 9
    random.shuffle(grid[0])                                                         # Shuffling the numbers in the first line

    def add_next_item(grid, row, col):                                              # Making a nested function to call it recursively later
        valids = [i for i in range(1, 10)]                                          # Get the numbers that can be placed at grid[row][col]
        subgrid_coords = (row - (row % 3), col - (col % 3))                         # Getting the coords of the subgrids
        for i in range(9):                                                          # Looping through the grid
            lst = [
                grid[row][i],
                grid[i][col], 
                grid[ subgrid_coords[0] + i//3 ][ subgrid_coords[1] + (i%3) ]
            ]
            for itm in lst:                                                         # Looping through the item in the list
                if itm in valids:                                                   # Checking it the item is one element of the valids elements
                    valids.remove(itm)                                              # If so, removing it from the valids elements as it's already placed

        if row == 8 and col == 8:                                                   # If we are filling the last box of the grid
            if len(valids) == 0:                                                    # And the valid list is empty
                return False                                                        # Then the row generated is wrong (it lacks one number)
            else:
                grid[row][col] = valids[0]                                          # Else, there is only an element left in the valid list
                return True                                                         # The row is correct
        next_case = (row, col+1) if col<8 else (row+1, 0)                           # Getting the coordinates of the next subgrid to fill

        random.shuffle(valids)                                                      # Mixing the numbers list, to avoid choosing always the smallest numbers first
        for itm in valids:                                                          # Put the number in the grid, and try to solve this new grid by calling add_next_item()
            grid[row][col] = itm
            if add_next_item(grid, next_case[0], next_case[1]):                     # If the function return True, the grid is valid, return True
                return True
        grid[row][col] = 0                                                          # If we get here, the grid is not solvable, so return False
        return False

    add_next_item(grid, 1, 0)                                                       # First call of the nested function
    return grid                                                                     # Return a completed valid grid


def random_tester(n, print_grid_bool):
    amount_of_tests = n
    tests_failed = 0
    some_test_failed = False

    for i in range(amount_of_tests):
        failed = False                                                                                   # Value to know if a test as failed

        grid = generate_sudoku_grid()                                                                    # Here we generate a complete valid grid 
        
        amount_to_remove = random.randrange(5,20) if i<amount_of_tests/3 else random.randrange(10,50)    # Here we get the number of numbers that will be removed from the grid
        a = [i for i in range(0, 9*9)]                                                                   # Here we get the number of numbers that will be removed from the gri
        random.shuffle(a)                                                                                # Here we shuffle the numbers we got in a
        to_remove = a[0:amount_to_remove]                                                                # Here we truncate the numbers to the amount of numbers to remove. Each number in a is an index in the grid
        for j in to_remove:                                                                              # Looping through all the numbers in a
            grid[int(j/9)][j%9] = 0                                                                      # Replacing numbers in the j index with 0 to be solved later

        solved = solve_sudoku(grid)                                                                      # Trying to solve the sudoku

        
        is_original_like = True                                                                          # Check that the non-zero numbers of the original grid are still there in the solved grid

        for row in range(9):                                                                             # Looping through the rows
            for col in range(9):                                                                         # Looping through the columns from the row index (Horizontally)
                if grid[row][col] != 0 and grid[row][col] != solved[row][col]:                           # Checking that the number in the solved grid is equal to the original grid
                    is_original_like = False                                                             # If not then return false for the is_original_like value

        if not is_original_like:                                                                         # If not like the original then it's a fail
            print("Test failed: the solver edited non-zero numbers on the original grid !")
            failed = True
            tests_failed += 1

        if not check_sudoku(solved):                                                                     # If it hasn't solved the sudoku, it's also a fail
            print("Test failed: the solver did not return a valid grid")
            failed = True
            tests_failed += 1

        if failed:                                                                                       # If there is a fail, it prints out the failed grid
            print("    ->input grid: "+str(grid))
            some_test_failed = True
        elif print_grid_bool:                                                                            # Else it prints the solved grid and the unsolved one if we said to at the begining
            print_grid(grid)                                                                             # Unsolved grid
            print()                                                                                      # New Line
            print_grid(solved)                                                                           # Solved grid
            print()                                                                                      # New Line

    if some_test_failed:
        print("{} test(s) failed !".format(tests_failed))
        print("Success rate of {}%".format(((amount_of_tests - tests_failed)/amount_of_tests)*100))
    else:
        print("No test failed !")
        print("Success rate of {}%".format(((amount_of_tests - tests_failed)/amount_of_tests)*100))

test_start = int(round(time.time() * 1000))                                                             # Getting the current time in millis
print("Starting testing...")
random_tester(20, False)
print("Testings done in {} ms !".format(int(round(time.time() * 1000)) - test_start))                   # Printing how much time it has passed since the begining of the test