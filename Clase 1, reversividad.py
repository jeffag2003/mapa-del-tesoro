#Potencia con numero enteros positivos o cero
#E: base, exponente
#S: numero

def potencia(base, exp):
    if exp == 0:
        return 1
    else:
        return base * potencia(base, exp-1)



#E: numero natural
#S: numero natural

def sumatoria(n):
    if n == 0:
        return 0
    else:
        return n + sumatoria(n-1)




#contar_digitos
# E: numero entero
# S: cantidad de digitos

def contar_digitos(n):
    if n <= 0:
        return 0
    else:
        return 1 + contar_digitos(num//10)



#retornar la cantidad de divisores que tiene un numero positivo o 0
# divisores(10) retorna un 4 #1,2,5,10
# E: num
# S: num

def divisores(num):
    return divisores_aux(num, 1)

def divisores_aux(num, divisor):
    if divisor > num:
        return 0   #Este return hace que en la ultima repeticion la funcion se 
    elif num%div == 0:
        return 1 + divisores_aux(num,divisor+1)
    else:
        return divisores_aux(num,divisor+1) #Se vuelve 0 cuando completa las iteraciones respectivas y se empieza a sumar


#E: lista
#S: numero
def suma_pares(lista):
    if lista == []:
        return 0
    elif lista == 0:
        return 1 + suma_pares(lista[1:])
    else:
        return suma_pares(lista[1:])


#E: numero
#S: numero
def contar_multiplos_3(num):
    if num == 0:
        return 0
    elif num%3 == 0:
        return 1 + contar_multiplos_3(num//10)
    else:
        return contar_multiplos_3(num//10)

#E: numero
#S: numero
def producto_digitos(num):
    if num <10 :
        return num
    else:
        return  (num%10) * producto_digitos(num//10)








