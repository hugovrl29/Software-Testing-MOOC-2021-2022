from random import choice
from random import randint
from random import random
from sudoku_checker import check_sudoku
from sudoku_solver import backtrackingFunction, findPossibilities ,print_grid
import logging
import copy

emptyGrid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0]]

def solve_sudoku (grid):
    ###Your code here.
    """ This funtion solves some sudoku
        parameter:
        grid : the sudoku grid (list of list)
        
        this suduko solver is a good solver made on udacity
        """
    for row in range(9):

        for col in range(9):
            
            if grid[row][col] == 0: # check if the case is empty

                for i in range(1,10): #remplacing the empty case by 1, then 2 ,..., to 9

                    grid[row][col] = i
                    if check_sudoku(grid) == True: #check if the grid is valid
                        
                        new_grid = solve_sudoku(grid) # recursive function
                        
                        if new_grid != False:           

                            return new_grid
                
                grid[row][col]=0 # remplacing the bad value by 0 

                return False
                

    return grid


def random_grid(emptyGrid):

    a_emptyGrid = copy.deepcopy(emptyGrid) #make a copy to protect the original grid

    #complete randomly a cell in each sub-grid

    a_emptyGrid[0][0] = randint(1,9)
    a_emptyGrid[8][8] = randint(1,9)
    a_emptyGrid[4][1] = randint(1,9)
    a_emptyGrid[2][4] = randint(1,9)
    a_emptyGrid[5][5] = randint(1,9)
    a_emptyGrid[7][2] = randint(1,9)
    a_emptyGrid[4][6] = randint(1,9)
    a_emptyGrid[1][7] = randint(1,9)
    a_emptyGrid[6][3] = randint(1,9)
    
    #complete all cells 
    new_grid = solve_sudoku(a_emptyGrid)
            
    nb_cell_empty = randint(17,64) #  number of empties cells
    result = copy.deepcopy(new_grid)

    case = 0
    while case < nb_cell_empty:

        #randomly empty some cells
        row = randint(0,8)
        col = randint(0,8)

        new_grid[row][col] = 0
        
        case +=1

    aGrid = new_grid   

    #return the grid and the solution
    return aGrid,result


def random_tester():
    #record the testing in a file.log 
    logging.basicConfig(filename="randomTester.log",format='%(asctime)s %(message)s', level=logging.DEBUG)
    logging.basicConfig(datefmt='%m/%d/%Y %I:%M:%S %p')
    
    grid,result = random_grid(emptyGrid) #create a random valid grid and his solution
    logging.debug("The sudoku's grid is : ")
    logging.debug(grid)
    print_grid(grid)
    
    print("\n Solution")
    #resolve the sudoku
    tab_of_possiblities = findPossibilities(grid)
    new_grid = backtrackingFunction(grid,tab_of_possiblities)
    
    # check if the result is the same as the result of the Udacity course
    assert new_grid == result 

    if type(new_grid) != list:
        print("The sudoku don't have a solution")
        logging.debug("The sudoku don't have a solution")
        logging.debug("\n")

    else:
        print_grid(new_grid)
        logging.debug("The result is : ")
        logging.debug(new_grid)
        logging.debug("\n")
    print("---------------------- \n \n \n")    

def sudokuTester(numOfTest):
    count = 0
    while count < numOfTest :
        print("---------Test %s---------"%str(count+1))
        random_tester()
        
        count +=1

sudokuTester(5)
