import sys
from translators import translator_input
from combinations import generate_possibilities

from pysat.solvers import Solver

def main():
    filename = sys.argv[1]
    (n, m, row_clues, column_clues) = translator_input(filename)

    s = Solver(name='g421')
    (CNF_variables, possibilities_variables) = generate_possibilities(row_clues, column_clues, n, m)
    #s.append_formula(formula)

    #if not s.solve():
    #    print("No hay solución")
    #    exit()

    #print("Hay solución")
    
main()