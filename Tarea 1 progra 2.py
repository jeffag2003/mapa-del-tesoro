#1. Contar ocurrencias de un dígito específico
#E: 2 numeros
#S: Numero con la cantidad de ocurrencias
def contar_ocurrencias(num, rep):
    if num == 0:
        return 0
    elif num%10 == rep:
        return 1 + contar_ocurrencias(num//10, rep)
    else:
        return contar_ocurrencias(num//10, rep)
        
#2. Verificar si un numero es primo
#E: Un numero y un numero divisor
#S: Booleano
def es_primo(num, divisor=2):
    if num <= 1:
        return False
    elif num % divisor == 0:
        return False
    elif divisor * divisor > num:
        return True
    return es_primo(num, divisor+1)

#3. Contar ceros
#E: Un numero
#S: Un numero
def contar_ceros(num):
    if num == 0:
        return 1
    elif num < 10:
        return 0
    elif num % 10 == 0:
        return 1 + contar_ceros(num//10)
    else:
        return contar_ceros(num//10)


#4. Verificar si todos los digitos son pares
#E: Un numero
#S: Booleano
def todos_pares(num):
    if num == 0:
        return True
    elif (num%10) % 2 == 1:
        return False
    return todos_pares(num//10)


#5. Suma alternada de digitos
#E: Un numero
#S: Un numero
def suma_alternada(num):
    if num == 0:
        return 0
    elif num > 0:
        return num + suma_alternada((num//10))
                                    








#6. Eliminar pares
#E: Un numero
#S: Un numero
def eliminar_pares(num):
    if num == 0:
        return 0
    elif (num%10) % 2 == 1:
        return eliminar_pares(num//10) * 10 + (num%10)
    else:
        return eliminar_pares(num//10)
    

#7. Eliminar elementos repetidos
#E: Una lista
#S: Una lista
def sin_repetidos(lista):
    if lista == []:
        return []
    elif lista[0] in lista[1:]:
        return sin_repetidos(lista[1:])
    else:
        return [lista[0]] + sin_repetidos(lista[1:])

    
















    

