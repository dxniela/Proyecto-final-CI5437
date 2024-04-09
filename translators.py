def translator_input(filename):
    n, m, row_clues, column_clues = None, None, None, None

    with open(filename, 'r') as file:
        first_line = next(file).strip()
        m, n = map(int, first_line.split())  

        row_clues, column_clues = [[]]*n, [[]]*m

        for i in range(n):
            clues = next(file).strip()
            row_clues[i] = list(map(int, clues.split()))

        for j in range(m):
            clues = next(file).strip()
            column_clues[j] = list(map(int, clues.split()))

    if (n == None or m == None or row_clues == None or column_clues == None):
        raise ValueError(f"Hubo un error al leer el archivo {filename}")

    return n, m, row_clues, column_clues