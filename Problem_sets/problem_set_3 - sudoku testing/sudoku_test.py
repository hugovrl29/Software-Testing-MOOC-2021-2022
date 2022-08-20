import random, logging
from copy import deepcopy

import sudoku_checker
import sudoku_solver

def sudoku_generator():
    """Generate a random sudoku grid"""
    grid = [[random.randint(0, 9) for i in range(9)] for j in range(9)] # génération d'une grille avec des nombres aléatoires
    return grid


def display_grid(grid):
    """Write a sudoku grid in the terminal and in the log file
    Author: Blckknght"""
    if sudoku_checker.check_sudoku(grid) is not None:
        logging.debug("_"*37)
        for i, j in enumerate(grid):
            logging.debug(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in j]))
            if i == 8:
                logging.debug("-"*37)
            elif i % 3 == 2:
                logging.debug("|" + "---+"*8 + "---|")
            else:
                logging.debug("|" + "   +"*8 + "   |")
    else:
        logging.debug('Ce sudoku n\'a pas de solution')

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ TEST ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓

sudoku_list = {}
sudoku_counter = 0

logging.basicConfig(filename="problem_set_3 - sudoku testing\\tests_output.log", format='%(asctime)s %(message)s', level=logging.DEBUG)
logging.basicConfig(datefmt='%m/%d/%Y %I:%M:%S %p')

logging.debug('Debut du testing\n')
logging.debug('1: Blackbox testing')

for grid in [(sudoku_checker.ill_formed, 'mal concu'), (sudoku_checker.valid, 'valide'), (sudoku_checker.invalid, 'invalide'), (sudoku_checker.easy, 'facile'), (sudoku_checker.hard, 'facile')]:
    sudoku_list['sudoku '+str(sudoku_counter)] = {'base_grid':  grid[0], 'solved_grid': sudoku_solver.solve_sudoku(grid[0]) if sudoku_solver.solve_sudoku(grid[0]) not in [None, False] else "Pas de solution"} # clé contenant chaque grille
    logging.debug(grid[1])
    display_grid(grid[0]) # display the grid
    if grid[1] not in [None, False]:
        display_grid(sudoku_solver.solve_sudoku(grid[0])) # display the solved grid
    else:
        logging.debug('Pas de solution')