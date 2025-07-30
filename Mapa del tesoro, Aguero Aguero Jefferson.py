import tkinter as tk


#crear un mapa de nxm caracteres
#E: ruta_nombre del archivos, filas, columnas, caracter
#S: none (crea el archivo)
def create_raw_map(filename, rows, col, char):
    with open (filename, 'w') as file: 
        line = char * col  
        for _ in range(rows):  
            file.write(line + '\n') 
        

#lee el archivo linea a linea y retorna una matriz con cada linea
#E: nombre del archivo
#S: matriz
def read_map(filename):
    matriz = []
    with open (filename, 'r') as file: #abre el archivo
        for line in file:   #el file es iterable, se recorre por linea
            matriz.append(line[:-1]) #hace push en la matriz y se guarda como lista, el [:-1] quita el \n
    return matriz

#cambiar un caracter en el mapa dado un x,y
#E: ruta_nombre del archivos, filas, columnas, caracter nuevo
#S: none (cambia el mapa)
def change_character(filename, row, col, new_char):
    with open (filename, 'r+') as file:
        file.seek(0)
        line = file.readline()
        row_length = len(line[:-1])
        offset = row * (row_length + 1) + col
        file.seek(offset)
        file.write(new_char)



#dibujar caminos horizontales y verticales dada una lista de puntos (tuplas,(x,y)
#E: archivo, caracter, lista coordenadas [(4,6) (6,30), (30,52), ....]
        #uno de los 2 valores debe ser igual
        #si es x se va a pintar horizontalmente
        #si es y se va a pintar verticalmente
#R: No se puede llegar mas largo al tamno de la fila
        #el calculo se puede hacer con linea -2
   
def draw_path(filename, new_char, coords_list):
    with open(filename, 'r+') as file:
        file.seek(0)
        line = file.readline()
        row_length = len(line[:-1])
        file.seek(0)

        for i in range(len(coords_list) - 1):
            row1, col1 = coords_list[i]
            row2, col2 = coords_list[i + 1]

            if row1 == row2:  
                for c in range(min(col1, col2), max(col1, col2) + 1):
                    offset = row1 * (row_length + 1) + c
                    file.seek(offset)
                    file.write(new_char)

            elif col1 == col2:  
                for r in range(min(row1, row2), max(row1, row2) + 1):
                    offset = r * (row_length + 1) + col1
                    file.seek(offset)
                    file.write(new_char)
            else:
                return

    


def find_treasure(filename, start):
    mapa = read_map(filename)
    rows = len(mapa)
    col = len(mapa[0])
    passed = [[False] * col for _ in range(rows)]
    path = []


    def valid(r, c):
        if r < 0 or r >= rows or c < 0 or c >= col:
            return False
        if passed[r][c]:
            return False
        if mapa[r][c] != '.' and mapa[r][c] != 'T':
            return False
        return True

    def backtracking_solution(r,c):
        if not valid(r,c):
            return False

        passed[r][c] = True
        path.append((r, c))

        if mapa[r][c] == 'T':
            return True

        coords = [(-1,0), (1,0), (0,-1), (0,1)]
        for new_r, new_c in coords:
            if backtracking_solution( r + new_r, c + new_c):
                return True

        path.pop()
        passed[r][c] = False
        return False

    found = backtracking_solution(start[0], start[1])
    if found:
        print('se encontro')
        mark_path(filename, path, '*')
        return path
    else:
        print('no se encontro')
        return False
        

def mark_path(filename, path, char='*'):
    mapa = read_map(filename)
    mapa_lista = []
    for row in mapa:
        row_lista = []
        for caracter in row:
            row_lista.append(caracter)
        mapa_lista.append(row_lista)

    for r, c in path:
        mapa_lista[r][c] = char

    if path:
        new_filename = 'mapa_camino.txt'
        with open(new_filename, 'w') as file:
            for row in mapa_lista:
                line = ""
                for character in row:
                    line += character
                file.write(line + "\n")
        print("Archivo con camino guardado en " + new_filename)

def map_GUI(filename, start, path, treasure_found):
    mapa = read_map(filename)
    rows = len(mapa)
    col = len(mapa[0])
    cell_size = 20

    root = tk.Tk()
    root.title("Mapa del Tesoro")

    canvas = tk.Canvas(root, width=col * cell_size, height=rows * cell_size + 40)
    canvas.pack()

    for r in range(rows):
        for c in range(col):
            x1 = c * cell_size
            y1 = r * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            cell = mapa[r][c]

            # Pinta el camino si está en path
            if (r, c) in path:
                color = 'green'
            elif cell == '#':
                color = 'purple'
            elif cell == 'T':
                color = 'gold'
            else:
                color = 'white'

            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='black')

    if treasure_found:
        mensaje = 'Tesoro encontrado!'
        color_texto = 'green'
    else:
        mensaje = 'No se encontró el tesoro desde ' + str(start[0]) + ',' + str(start[1])
        color_texto = 'red'
        with open("mapa_err.txt", "w") as error_file:
            error_file.write('Error, mapa sin solución iniciando en coordenadas ' + str(start[0]) + ',' + str(start[1]) + '\n')

    canvas.create_text((col * cell_size) // 2, rows * cell_size + 20, text=mensaje, fill=color_texto, font=("Arial", 12, "bold"))

    root.mainloop()







                
    
