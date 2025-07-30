#E: nombre del archivo
#S:
def process_log(filename):
    usuarios = []
    actividades = []
    mayor = 0
    usuario_mas_activo = ''

    with open (filename, 'r') as archivo:
        linea = archivo.readline()

        for linea in archivo:
            if 'Usuario' in linea:
                palabra = ''
                palabras = []

                for c in linea:
                    if c == ' ':
                        if palabra != '':
                            palabras.append(palabra)
                            palabra = ''
                    else:
                        palabra += c
                if palabra != '':
                    palabras.append(palabra)

                for i in range(len(palabras)):
                    if palabras[i] == 'Usuario':
                        nombre = palabras[i + 1]
                        break

                for j in range(len(usuarios)):
                    if usuarios[j] == nombre:
                        actividades[j] += 1
                        break
                else:
                    usuarios.append(nombre)
                    actividades.append(1)

        for i in range(len(usuarios)):
            if actividades[i] > mayor:
                mayor = actividades[i]
                usuario_mas_activo = usuarios[i]
        print('Usuario mas activo: ', usuario_mas_activo)

        with open('user_activity.txt', 'w') as archivo:
            for i in range(len(usuarios)):
                archivo.write('Usuario ' + usuarios[i] + ' tiene ' + str(actividades[i]) + ' actividades')
                
        
        
            

                    
    

        


#E: nombre del archivo
#S: 
def read_map(filename):
    matriz = []
    with open(filename, 'r') as archivo:
        for linea in archivo:
            fila = list(linea.strip())
            matriz.append(fila)

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 'X':
                print(i,j)

