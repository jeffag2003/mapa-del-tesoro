
##############################
#arboles
# estructura jerarquica sobre un conjunto de objetos llamados nodos
# Los conectores de esa jerarquia se llaman ramas
# Existe un nodo especial, llamado RAIZ
# Un nodo puede ser cualquier tipo de objeto

# Un arbol se puede definir recursivamente:
# el arbol nulo es un arbol
# existe un nodo especial llamado raiz
# los nodos restantes se parte en subconjuntos T1, T2 ... Tn, cada
# uno con una raiz es un subarbol y tiene una raiz

# ARBOL BINARIO
# Nodo Padre, hijo izquierdo, hijo derecho
# mostrar c'omo se representa un arbol con listas

a1 = [10, [5, [2, 1, [3,[],4]], []], [30,25,[60,[50, [40,31,[]],55],[]]]]


# construir un arbol
# centro, hi, hd: arboles binarios
def arbol (centro, hijoizquierdo, hijoderecho):
    if hijoizquierdo == [] and hijoderecho == []:
        return centro
    else:
        return [centro] + [hijoizquierdo] + [hijoderecho]

# funciones que retonan raiz, hi, hd

#atomo
#E: un arbol
#S: booleano
# funcion que indica si es un valor o un subarbol
def atomo(x):
   # return not isinstance (x, list)
    return not type(x) == list

# funcion que retorna la raiz, retorna un valor
#E: arbol
#R: la raiz como un numero
def raiz (arbol):
    if atomo(arbol):
        return arbol
    else:
        return arbol[0]

# funcion que retorna el hijo izquierdo, retorna un arbol
# E: arbol
# S: retorna el hijo izuqierdo
def hijoizq (arbol):
    if atomo(arbol):
        return []
    else:
        return arbol[1]

# funcion que retorna el hijo izquierdo, retorna un arbol
def hijoder (arbol):
    if atomo(arbol):
        return []
    else:
        return arbol[2]

# hoja, es cuando no tiene hijos un nodo
# E: recibe un arbol
# S: retorna True si no tiene hijos
def hoja(nodo):
    if nodo == []:
        return False
    elif atomo(nodo):
        return True #[10,[],[]]
    elif hijoizq(nodo) == [] and hijoder(nodo) == []:
        return True
    else:
        return False




#retorna la cantidad de elemento o nodos que tiene un AB
#E: arbol
#S: numero (+ - * // ...)
def contar_nodos(arbol):
    if arbol == []:
        return 0

    #haga algo con la raiz
    #recursivamente haga lo mismo con los hijos
    else:
        return 1 + contar_nodos(hijoizq(arbol)) + contar_nodos(hijoder(arbol))


#retorne la sumatoria de todas llaves de los nodos del arbol
#E: arbol
#S: numero
def sumatoria(arbol):
    if arbol == []:
        return 0
    else:
        return raiz(arbol) + sumatoria(hijoizq(arbol)) + sumatoria(hijoder(arbol))


#retorne la sumatoria de las claves pares de un arbol binario
#E: arbol
#S: numero
def suma_pares(arbol):
    if arbol == []:
        return 0
    elif raiz(arbol) % 2 == 0:
        return raiz(arbol) + suma_pares(hijoizq(arbol)) + suma_pares(hijoder(arbol))
    else:
        return suma_pares(hijoizq(arbol)) + suma_pares(hijoder(arbol))


#retorne True si todas las claves del AB son pares o 0
#E: arbol
#S: boolean
#def todos_pares(arbol):
    #if arbol == []:
        #return False
    





