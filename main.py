from translators import translator_input
from combinations import generate_possibilities, generate_restrictions
from pysat.solvers import Solver
import sys

def main():
    filename = sys.argv[1]
    (n, m, row_clues, column_clues) = translator_input(filename)

    s = Solver(name='g421')
    (CNF_variables, possibilities_variables, n_variables) = generate_possibilities(row_clues, column_clues, n, m)
    s.append_formula(generate_restrictions(CNF_variables, possibilities_variables, n, m))
    print(possibilities_variables)
    print("Resolviendo")
    if not s.solve():
        print("No hay solución")
        exit()

    CNF_variables_keys = CNF_variables.keys()

    print("Hay solución")
    print(s.get_model())
    
main()