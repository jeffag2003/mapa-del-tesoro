def permutar(lista, camino=[]):
    if not lista:
        print(camino)
        return

    for i in range(len(lista)):
        # Elegimos el elemento i
        nuevo_elemento = lista[i]
        # Generamos una nueva lista sin ese elemento
        resto = lista[:i] + lista[i+1:]
        print(i,':',nuevo_elemento, 'lista:', resto, camino + [nuevo_elemento])
        # Exploramos con esa nueva elección
        permutar(resto, camino + [nuevo_elemento])

# Ejemplo:
permutar(['A', 'B', 'C'])
