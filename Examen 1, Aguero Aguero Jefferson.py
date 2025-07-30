#E: Lista
#S: Lista

def detectar_valles(lista):
    if len(lista) < 3:
        return []
    return detectar_valles_aux (lista,1,[])

def detectar_valles_aux(lista, i, res):
        if i >= len(lista) - 1:
            return res

        if lista[i] < lista[i-1] and lista[i] < lista[i + 1]:
            return detectar_valles_aux(lista, i + 1, res + [[lista[i-1], lista[i], lista[i+1]]])
        return detectar_valles_aux(lista, i + 1, res)






#E: Lista
#S: Lista

def cut(lista):
    return cut_aux(0,[],[], lista)

def cut_aux(i, actual, res, lista):
    if i >= len(lista):
        if actual:
            res += [actual]
        return res

    if lista[i] == 0:
        if actual:
            res += [actual]
        return cut_aux(i + 1, [], res, lista)
    return cut_aux(i + 1, actual + [lista[i]], res, lista)


#E: 2 numeros
#S: numero
def contar_digitos(n, contador =0):
    if n == 0:
        return contador
    return contar_digitos(n // 10, contador + 1)


def elimine(num, dig):
    if num == 0 and dig == 0:
        return 0
    exp = contar_digitos(num) - 1
    return elimine_aux(num, exp, False, 0, dig)


def elimine_aux(num, exp, encontrado, nuevo, dig):
    if exp < 0:
        return nuevo
    temp = (num // (10 ** exp)) % 10
    
    if temp == dig:
        if not encontrado:
            return elimine_aux(num, exp - 1, True, nuevo * 10 + temp, dig)
        return elimine_aux(num, exp - 1, True, nuevo, dig)
    return elimine_aux(num, exp - 1, encontrado, nuevo * 10 + temp, dig)
        


#E: numero
#S: lista
def es_montana(num):
    digito = conseguir_digito(num)
    return es_montana_aux(digito, [], [], [], 'subiendo')

def conseguir_digito(num, res=[]):
    if num < 10:
        return [num] + res
    else:
        return conseguir_digito(num // 10, [num % 10] + res)

def es_montana_aux(digito, subida, pico, bajada, fase):
    if len(digito) == 1:
        if fase == 'bajando' and subida and pico and bajada:
            return (subida, pico, bajada + [digito[0]])
        else:
            return ([], [], [])

    actual = digito[0]
    siguiente = digito[1]

    if actual == siguiente:
        return ([], [], [])

    if fase == 'subiendo':
        if actual < siguiente:
            return es_montana_aux(digito[1:], subida + [actual], pico, bajada, 'subiendo')
        elif actual > siguiente:
            if not subida:
                return ([], [], [])
            return es_montana_aux(digito[1:], subida, [actual], bajada, 'bajando')

    elif fase == 'bajando':
        if actual > siguiente:
            return es_montana_aux(digito[1:],subida, pico, bajada + [actual],  'bajando')
        else:
            return ([], [], [])




