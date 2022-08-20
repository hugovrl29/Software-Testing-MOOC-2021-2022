import random, math, copy, logging, sudoku_checker

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

"""
ill_formed = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9],  # <---
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return valid unchanged
valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return False
invalid = [[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,8,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return a 
# sudoku grid which passes a 
# sudoku checker. There may be
# multiple correct grids which 
# can be made from this starting 
# grid.
easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

# Note: this may timeout 
# in the Udacity IDE! Try running 
# it locally if you'd like to test 
# your solution with it.
# 
hard = [[1,0,0,0,0,7,0,9,0],
         [0,3,0,0,2,0,0,0,8],
         [0,0,9,6,0,0,5,0,0],
         [0,0,5,3,0,0,9,0,0],
         [0,1,0,0,8,0,0,0,2],
         [6,0,0,0,0,4,0,0,0],
         [3,0,0,0,0,0,0,1,0],
         [0,4,0,0,0,0,0,0,7],
         [0,0,7,0,0,0,3,0,0]]

def check_sudoku(grid):
    Check the validity of a sudoku
    #check parameter type
    if type(grid) != list:
        return None
        
    #check row sizes
    if len(grid) != 9:
        return False
        
    #check column sizes
    for row in grid:
        if len(row) != 9:
            return None

    #check that each grid element is a positive integer between 0 and 9
    for row in grid:
        for col in row:
            if (type(col) != int) or (col < 0) or (col not in range(10)):
                return None
    
    #check that there are 81 elements in grid
    nb_elt = 0
    for row in grid:
        for num in row:
            nb_elt += 1
    if nb_elt != 81:
        return None
        
    #check that each number appears once
    col_repeated_nb = False
    row_repeated_nb = False
    subg_repeated_nb = False

    #check for duplications in rows
    for row in grid:
        for num in row:
            if (row.count(num) > 1) and (num != 0):
                row_repeated_nb = True
        
    #check for duplications in columns
    revert_grid = list(zip(*grid))
    for col in revert_grid:
        for num in col:
            if (col.count(num) > 1) and (num != 0):
                col_repeated_nb = True
    
    
    #create a list stocking sub_grids
    sub_grids = [0*9]*9
    current_sub_grid = []
    
    #1st sub_grid
    for i in range(3):
        current_sub_grid.append(grid[0][i])
    for row in grid[1:3]:
        current_sub_grid.extend(row[:3])
    sub_grids[0] = current_sub_grid
    current_sub_grid = []
    
    #2nd sub_grid
    for i in range(3, 6):
        current_sub_grid.append(grid[0][i])
    for row in grid[1:3]:
        current_sub_grid.extend(row[3:6])
    sub_grids[1] = current_sub_grid
    current_sub_grid = []
    
    #3rd sub_grid
    for i in range(6, 9):
        current_sub_grid.append(grid[0][i])
    for row in grid[1:3]:
        current_sub_grid.extend(row[6:9])
    sub_grids[2] = current_sub_grid
    current_sub_grid = []
    
    #4th sub_grid
    for i in range(3):
        current_sub_grid.append(grid[3][i])
    for row in grid[4:6]:
        current_sub_grid.extend(row[:3])
    sub_grids[3] = current_sub_grid
    current_sub_grid = []
    
    #5th sub_grid
    for i in range(3, 6):
        current_sub_grid.append(grid[3][i])
    for row in grid[4:6]:
        current_sub_grid.extend(row[3:6])
    sub_grids[4] = current_sub_grid
    current_sub_grid = []
    
    #6th sub_grid
    for i in range(6, 9):
        current_sub_grid.append(grid[3][i])
    for row in grid[4:6]:
        current_sub_grid.extend(row[6:9])
    sub_grids[5] = current_sub_grid
    current_sub_grid = []
    
    #7th sub_grid
    for i in range(3):
        current_sub_grid.append(grid[6][i])
    for row in grid[7:9]:
        current_sub_grid.extend(row[:3])
    sub_grids[6] = current_sub_grid
    current_sub_grid = []
    
    #8th sub_grid
    for i in range(3, 6):
        current_sub_grid.append(grid[6][i])
    for row in grid[7:9]:
        current_sub_grid.extend(row[3:6])
    sub_grids[7] = current_sub_grid
    current_sub_grid = []
    
    #9th sub_grid
    for i in range(6, 9):
        current_sub_grid.append(grid[6][i])
    for row in grid[7:9]:
        current_sub_grid.extend(row[6:9])
    sub_grids[8] = current_sub_grid
    current_sub_grid = []
    
    #check for duplications in sub_grids
    for sub_grid in sub_grids:
        for num in sub_grid:
            if (sub_grid.count(num)) > 1 and (num != 0):
                subg_repeated_nb = True
                
    #return false if there are duplications        
    if (col_repeated_nb == True) or (row_repeated_nb == True) or (subg_repeated_nb == True):
        return False
        
    #return true if all is ok
    else:
        return True
"""

def solve_sudoku (grid):
    """Solve a given sudoku grid"""
     #check whether a grid is valid
    
    if sudoku_checker.check_sudoku(grid) == None:
        return None
    elif sudoku_checker.check_sudoku(grid) == False:
        return False
    else:
        _grid = copy.deepcopy(grid) # no overwrite the existing grids
        
        #change each 0 by an int and verify each time
        for row in range(9): #column
            for num in range(9): #line
                if  _grid[row][num] == 0:
                    # replace each 0 by {i | 0 < i < 10}
                    for i in range(1,10):
                        _grid[row][num] = i
                        if sudoku_checker.check_sudoku(_grid) == True: 
                            #verify that the grid is still correct
                            grid_return = solve_sudoku(_grid) # recursion
                            if solve_sudoku(_grid) != False:#backtracking point in case it is false
                                return grid_return
                    #replace by 0 if it's not correct
                    _grid[row][num] = 0
                    return False
    return _grid