from itertools import combinations

# Función que genera todas las posibles formas de colocar los bloques en los espacios vacíos.
def generate_possibilities(groups, is_row, n_cols, n_rows):
    # Si la línea tiene un 0, entonces la fila o columna está completamente vacía y se coloca una F en todas las celdas.
    if groups == [0]:
        return [['F'] * (n_cols if is_row else n_rows)]
    
    # Se calcula el número de grupos y el número de espacios vacíos.
    n_groups = len(groups)
    n_empty = (n_cols if is_row else n_rows) - sum(groups) - (n_groups - 1)

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

# Función que escribe las cláusulas en el archivo.
def write_clauses(file, cells, groups, is_row, n_cols, n_rows):
    # Genera todas las posibles combinaciones de bloques y espacios vacíos.
    possibilities = generate_possibilities(groups, is_row, n_cols, n_rows)

    # Para cada posibilidad, escribe las cláusulas en el archivo.
    for possibility in possibilities:
        # Escribe las cláusulas: (l_1 ^ ... ^ l_n)
        for i, value in enumerate(possibility):
            l_i = cells[i] if value == 'T' else f"NOT{cells[i]}"
            file.write(f"{l_i} ")
        file.write("0\\n")