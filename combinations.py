from itertools import combinations

def generate_possibilities_aux(groups, n):
    if groups == [0]:
        return [['F'] * n]
    
    # Se calcula el número de grupos y el número de espacios vacíos.
    n_groups = len(groups)
    n_empty = n - sum(groups) - (n_groups - 1)

    # Genera todas las formas posibles de tomar n_groups elementos de un conjunto de n_blocks.
    n_blocks = n_groups + n_empty
    combinations_list = list(combinations(range(n_blocks), n_groups))

    # Genera los bloques que se colocarán en los espacios vacíos.
    blocks = [['T'] * n + ['F'] for n in groups]

    # Para cada combinación, inserta los bloques en las posiciones correspondientes.
    possibilities = []
    for combination in combinations_list:
        possibility = ['F'] * n_blocks
        for i, block in zip(combination, blocks):
            possibility[i:i] = block
        possibilities.append(possibility[:-1])

    return possibilities

# Función que genera todas las posibles formas de colocar los bloques en los espacios vacíos.
def generate_possibilities(row_groups, column_groups, n, m):
    CNF_variables = {}
    possibilities_variables = {}
    counter = 1

    for i in range(len(row_groups)):
        possibilities = generate_possibilities_aux(row_groups[i], n)
        num_pos = 0
        for possibility in possibilities:
            CNF_variables[(0, i, num_pos)] = counter
            possibilities_variables[(0, i, num_pos)] = possibility
            counter += 1
            num_pos += 1
    
    for i in range(len(column_groups)):
        possibilities = generate_possibilities_aux(column_groups[i], m)
        num_pos = 0
        for possibility in possibilities:
            CNF_variables[(1, i, num_pos)] = counter
            possibilities_variables[(0, i, num_pos)] = possibility
            counter += 1
            num_pos += 1

    return CNF_variables, possibilities_variables