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
        aux = 0
        possibility = ['F'] * n
        for i, block in zip(combination, blocks):
            possibility[i+aux:i+aux+len(block)] = block
            aux = aux + (len(block)-1)                        
        if len(possibility) > n and possibility[-1] == 'F':
            possibility = possibility[:-1]
            
        possibilities.append(possibility)
        #print("arreglo possibilities",possibilities)

    return possibilities

# Función que genera todas las posibles formas de colocar los bloques en los espacios vacíos.
def generate_possibilities(row_groups, column_groups, n, m):
    CNF_variables = {}
    possibilities_variables = {}
    counter = 1

    for i in range(len(row_groups)):
        possibilities = generate_possibilities_aux(row_groups[i], m)
        num_pos = 0
        for possibility in possibilities:
            CNF_variables[(0, i, num_pos)] = counter
            possibilities_variables[(0, i, num_pos)] = possibility
            counter += 1
            num_pos += 1
    
    for i in range(len(column_groups)):
        possibilities = generate_possibilities_aux(column_groups[i], n)
        num_pos = 0
        for possibility in possibilities:
            CNF_variables[(1, i, num_pos)] = counter
            possibilities_variables[(1, i, num_pos)] = possibility
            counter += 1
            num_pos += 1

    return CNF_variables, possibilities_variables, counter - 1

def get_possibilities(CNF_variables, id_row_column, n):
    restrictions = []
    # Restricción de que solo debe ser cierta a lo sumo una posibilidad para cada fila o columna
    for i in range(n):
        possibilities = []
        num_pos = 0
        while True:
            try:
                # Intenta obtener el valor de CNF_variables[(0, i, num_pos)]
                val = CNF_variables[(id_row_column, i, num_pos)]
                # Si el valor existe, entonces añade las restricciones
                possibilities.append(val)
                num_pos += 1
            except KeyError:
                # Si la clave no existe, rompe el bucle
                break
        
        # Restricción de que solo debe ser cierta a lo sumo una posibilidad para cada fila o columna
        for a, b in combinations(possibilities, 2):
            restrictions.append([-a, -b])

        # Restricción de que por lo menos se cumple 1 posibilidad para cada fila o columna
        restrictions.append(possibilities)
        
    return restrictions

def generate_cell_restrictions(CNF_variables, possibilities_variables):
    restrictions = []
    for (id_row_column, i, k_row), val_row in CNF_variables.items():
        for (id_col_column, j, k_col), val_col in CNF_variables.items():
            if id_row_column == 0 and id_col_column == 1:
                try:
                    # Intenta obtener las posibilidades para la fila i y la columna j
                    if j < len(possibilities_variables[(0, i, k_row)]):
                        possibility_row = possibilities_variables[(0, i, k_row)][j]
                    if i < len(possibilities_variables[(1, j, k_col)]):
                        possibility_col = possibilities_variables[(1, j, k_col)][i]
                    # Si las posibilidades son diferentes, entonces añade las restricciones
                    if possibility_row != possibility_col:
                        restrictions.append([-val_row, -val_col])
                except KeyError:
                    # Si la clave no existe, continúa con el siguiente k
                    continue
    return restrictions

# Función para generar las restricciones de las posibilidades.
def generate_restrictions(CNF_variables, possibilities_variables, n_rows, n_cols):
    restrictions = []
    # Restricción de que solo debe ser cierta a lo sumo una posibilidad para cada fila o columna
    restrictions += get_possibilities(CNF_variables, 0, n_rows)
    restrictions += get_possibilities(CNF_variables, 1, n_cols)
    restrictions += generate_cell_restrictions(CNF_variables, possibilities_variables)
 
    return restrictions


