

#E: lista
#S: lista
def elementos_unicos(lista):
    if lista == []:
        return []
    elif lista[0] in lista[1:]:
        return elementos_unicos(lista[1:])
    else:
        return [lista[0]] + elementos_unicos(lista[1:])



#E: lista
#S: lista o matriz
def max_secuencias(lista):
    return max_secuencia_aux(lista, [], [[]])


def max_secuencia_aux(lista, actual, res):
    if not lista:
        if len(actual) > len(res[0]):
            return [actual]
        elif len(actual) == len(res[0]):
            return res + [actual]
        else:
            return res
    else:
        if len(actual) > 0:
            ultimo = actual[-1]
            if lista[0] == ultimo + 1:
                return max_secuencia_aux(lista[1:], actual + [lista[0]], res)
            else:
                if len(actual) > len(res[0]):
                    return max_secuencia_aux(lista[1:], [lista[0]], [actual])
                elif len(actual) == len(res[0]):
                    return max_secuencia_aux(lista[1:], [lista[0]], res + [actual])
                else:
                    return max_secuencia_aux(lista[1:], [lista[0]], res)
        else:
            return max_secuencia_aux(lista[1:], [lista[0]], res)            
    
