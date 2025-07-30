def sumar_con_1_y_2(n, combinacion=[]):
    if sum(combinacion) == n:
        print(combinacion)
        return
    if sum(combinacion) > n:
        return  # nos pasamos, hay que retroceder

    # Opción 1: agregar un 1
    sumar_con_1_y_2(n, combinacion + [1])

    # Opción 2: agregar un 2
    sumar_con_1_y_2(n, combinacion + [2])

# Ejemplo:
sumar_con_1_y_2(4)
