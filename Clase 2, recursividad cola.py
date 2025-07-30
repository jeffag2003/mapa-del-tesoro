#E: Lista
#S: Numero
def maximo_tail(lista):
    return maximo_tail_aux(lista[1:], lista[0])

def maximo_tail_aux(lista, max_actual):
    if lista == []:
        return max_actual
    elif lista[0] > max_actual:
        max_actual = lista[0]
    return maximo_tail_aux(lista[1:], max_actual)


#E: Numero
#S: Numero
def contar_multiplos_3(num, contador=0):
    if num == 0:
        return contador
    elif (num%10) % 3 == 0:
        contador += 1
    return contar_multiplos_3(num//10, contador)

#E: Numero
#S: Numero
def producto_digitos(num, res=1):
    if num == 0:
        return 0
    if num < 10:
        return res * num
    return producto_digitos(num//10, res *(num%10))

#E: Lista
#S: Numero
def contar(lista, num, contador=0):
    if lista == []:
        return contador
    elif lista[0] == num:
        return contar(lista[1:], num, contador+1)
    return contar(lista[1:], num, contador)
    
    
    
