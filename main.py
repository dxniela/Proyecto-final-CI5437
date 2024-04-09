from translators import translator_input
from combinations import generate_possibilities, generate_restrictions
from pysat.solvers import Solver
import tkinter as tk
from tkinter import filedialog

def solve_nonogram(filename):
    (n, m, row_clues, column_clues) = translator_input(filename)

    s = Solver(name='g421')
    (CNF_variables, possibilities_variables, n_variables) = generate_possibilities(row_clues, column_clues, n, m)
    s.append_formula(generate_restrictions(CNF_variables, possibilities_variables, n, m))
    
    print("Resolviendo")

    if not s.solve():
        print("No hay solución")
        exit()

    print("Hay solución")
    sol = [i for i in s.get_model() if i > 0]
    CNF_variables_keys = list(CNF_variables.keys())
    nonogram = []

    for v in sol:
        (c, i, pos) = CNF_variables_keys[v - 1]
        if c:
            break

        nonogram.append(possibilities_variables[(c, i, pos)])
    
    return nonogram

class NonogramSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Nonogram Solver")

        # Background
        self.background_image = tk.PhotoImage(file="Home.png") 

        self.canvas = tk.Canvas(self.root, width=1366, height=768)
        self.canvas.pack()

        self.canvas.create_image(0, 0, image=self.background_image, anchor=tk.NW)
    
        frame = tk.Frame(root, bg='white')
        frame.place(x=1100, y=500) 

        # Cargar archivo
        self.load_button = tk.Button(frame, text="Cargar nonograma", command=self.load_file, font=("Helvetica World", 15), fg="white", bg="#D68B7C", activebackground="#D68B7C", highlightbackground = "white", highlightcolor= "white")
        self.load_button.pack()

        frame2 = tk.Frame(root, bg='white')
        frame2.place(x=1083, y=580) 
        
        self.solve_button = tk.Button(frame2, text="Resolver nonograma", command=self.solve_and_draw, font=("Helvetica World", 15), fg="white", bg="#D68B7C", activebackground="#D68B7C", highlightbackground = "white", highlightcolor= "white")
        self.solve_button.pack()

        self.filename = ""


    def load_file(self):
        # Abrir el diálogo de selección de archivos
        self.filename = filedialog.askopenfilename()

    def draw_nonogram(self, matrix):
        # Crear una nueva ventana
        new_window = tk.Toplevel(self.root)
        new_window.title("Nonogram")

        # Calcular el tamaño de cada celda
        cell_size = 50  # Tamaño de cada celda en píxeles

        # Calcular el tamaño de la nueva ventana basado en el tamaño del nonograma
        window_width = cell_size * len(matrix[0])
        window_height = cell_size * len(matrix)

        # Configurar el tamaño de la nueva ventana
        new_window.geometry(f"{window_width}x{window_height}")

        # Crear un nuevo canvas en la nueva ventana
        new_canvas = tk.Canvas(new_window, width=window_width, height=window_height)
        new_canvas.pack()

        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                x1 = j * cell_size
                y1 = i * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                color = 'black' if cell == 'T' else 'white'
                new_canvas.create_rectangle(x1, y1, x2, y2, fill=color)



    def solve_and_draw(self):
        # Resolver el nonograma
        matrix = solve_nonogram(self.filename)  # Asume que solve_nonogram es tu función para resolver el nonograma
        # Dibujar el nonograma resuelto
        self.draw_nonogram(matrix)

root = tk.Tk()

# Crear la interfaz gráfica
gui = NonogramSolverGUI(root)

# Mostrar la ventana principal
root.mainloop()

    