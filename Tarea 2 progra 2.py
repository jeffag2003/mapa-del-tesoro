#1. Contar ocurrencias de un dígito específico
#E: 2 numeros
#S: Numero con la cantidad de ocurrencias
def contar_ocurrencias(num, dig, contador=0):
    if num == 0:
        if dig == 0 and contador == 0:
            return 1
        return contador
    elif num%10 == dig:
        return contar_ocurrencias(num//10, dig, contador + 1)
    else:
        return contar_ocurrencias(num//10, dig, contador)

#2. Verificar si un numero es primo
#E: Un numero y un numero divisor
#S: Booleano
def es_primo(num, divisor=2):
    if num <= 1:
        return False
    if divisor * divisor > num:
        return True
    if num % divisor == 0:
        return False
    return es_primo(num, divisor+1)


#3. Contar ceros
#E: Un numero
#S: Un numero
def contar_ceros(num, contador=0):
    if num == 0:
        if contador == 0:
            return 1
        else:
            return contador

    if num < 10:
        if num == 0:
            return contador + 1
        else:
            return contador

    if num % 10 == 0:
        return contar_ceros(num//10, contador + 1)
    else:
        return contar_ceros(num//10, contador)

#4. Verificar si todos los digitos son pares
#E: Un numero
#S: Booleano
def todos_pares(num, par=True):
    if not par:
        return False
    if num == 0:
        return True
    if (num%10) % 2 != 0:
        par = False
    return todos_pares(num//10, par)

#5. Suma alternada de digitos
#E: Un numero
#S: Un numero

def suma_alternada(num):
    exp = contar_digitos(num) - 1
    return suma_alternada_aux(num, exp, 1, 0)
    
def suma_alternada_aux(num,exp, signo, res):
    if exp < 0:                  
        return res
    dig = (num // 10**exp) % 10
    return suma_alternada_aux(num, exp - 1, -signo, res + dig * signo)

#6. Eliminar pares
#E: Un numero
#S: Un numero
def eliminar_pares(num, res=0, potencia=1):
    if num == 0:
        return res
    dig = num % 10
    if dig % 2 == 1:  
        return eliminar_pares (num // 10, dig * potencia + res, potencia * 10)
    else:  
        return eliminar_pares(num // 10, res, potencia)

#7. Eliminar elementos repetidos
#E: Una lista
#S: Una lista
def sin_repetidos(lista):
    return sin_repetidos_aux(lista, [])

def sin_repetidos_aux(lista, res):
    if not lista:
        return res
    if lista[0] in res:
        return sin_repetidos_aux(lista[1:], res)
    else:
        return sin_repetidos_aux(lista[1:], res + [lista[0]])



#8. Sumar elementos en posiciones pares
#E: Una lista
#S: Un numero

def suma_pos_pares(lista, res=0):
    if lista == []:
        return res
    if len(lista) == 1:
        return res + lista[0]
    else:
        return suma_pos_pares(lista[2:], res + lista[0])

#9. Sumar elementos entre 2 indices
#E: Lista y 2 numeros
#S: Un numero
def suma_rango(lista, i, j, res=0):
    if i > j or i >= len(lista):
        return res
    return suma_rango(lista,i+1,j, res + lista[i])


#10. Sumar solo elementos que sean mayores que el promedio
#E: Lista y numero
#S: Numero
def suma_mayores_promedio(lista, res=0):
    if lista == []:
        return res
    promedio =  sum(lista) / len(lista)
    if lista[0] > promedio:
        return  suma_mayores_promedio(lista[1:], res + lista[0])
    else:
        return suma_mayores_promedio(lista[1:], res)
