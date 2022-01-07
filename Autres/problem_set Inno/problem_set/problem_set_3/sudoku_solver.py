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


import copy
from sudoku_checker import check_sudoku

# solve_sudoku should return None
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
mygrid =[
        [0,0,3,1,0,0,8,5,9],
        [0,4,0,0,0,0,0,2,0],
        [9,0,6,0,0,0,0,0,0],
        [0,0,2,4,1,0,0,0,0],
        [0,0,8,0,0,0,5,0,2],
        [0,0,0,0,2,7,4,0,0],
        [0,0,0,0,0,0,3,0,5],
        [0,6,0,0,0,0,0,9,0],
        [5,2,9,0,0,1,6,0,0]]

def backtrackingFunction(grid, tab_of_possiblities):

    """ This funtion solves sudoku's grids with backtracking
        
        parameter:
        ----------
        grid : the sudoku grid (list of list)
        tab_of_possiblities : a grid with the possibilities of each case of the sudoku
        return:
        -------
        new_grid = the good grid(list of list)
        or new_grid = False (if the sudoku does'nt have any solution)
    """

    if check_sudoku(grid) != True: 

        print("The grid is invalid")
        print(grid)
        return False

    for row in range(9):

        for col in range(9):

            if grid[row][col] == 0: # check if the case is empty

                for i in tab_of_possiblities[row][col]: #remplacing the empty case by the some numbers

                    grid[row][col] = i
                    if check_sudoku(grid) == True: #check if the grid is valid

                        new_grid = backtrackingFunction(grid,tab_of_possiblities) # recursive function
                        
                        if new_grid != False:           

                            return new_grid
                
                    grid[row][col]=0 # remplacing the bad value by 0 
                
                return False # if there are no solutions
                

    return grid #if the grid is already complete



def findPossibilities (grid):
    """ This funtion solves some sudoku
        parameter:
        -----------
        grid : the sudoku grid (list of list)

        return:
        -------
        grid_of_possibilities : a list of 3 dimensions
        """
    tab_of_val = []
    for row in range(9):

        for col in range(9):

            if grid[row][col] == 0: # check if the case is empty
                tab = []
 
                for i in range(1,10): #remplacing the empty case by 1, then 2 ,..., to 9
                    grid[row][col] = i
                    if check_sudoku(grid) == True: #check if the grid is valid
                        tab.append(i) 
                        grid[row][col] = 0
                        
                    else:
                        grid[row][col] = 0
                
                tab_of_val.append(tab)

            else:
                tab_of_val.append([0]) 

    #make a 3 dimentions' list with the possibilities      
    nb_lin = 9
    nb_col = len(tab_of_val) //nb_lin
    tab_final = []
    pos = 0
    for i in range(nb_lin):
        row = []
        for j in range(nb_col):
            row.append(tab_of_val[pos])
            pos += 1
        tab_final.append(row)

    return tab_final


def print_grid(grid):
    """Print a valid sudoku grid.

    parameter:
    ---------
    grid : the grid to display (list of list)
    """
    for i, row in enumerate(grid):
        print(' {} {} {} | {} {} {} | {} {} {} '.format(*row))
        if i == 2 or i == 5:
            print('-------+-------+-------')

#tab_of_possiblities = findPossibilities(mygrid)
#print_grid(backtrackingFunction(mygrid, tab_of_possiblities))

