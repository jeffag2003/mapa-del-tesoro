def generar_binarios(n, cadena=""):
    if len(cadena) == n:
        print(cadena)
        return
    generar_binarios(n, cadena + "0")
    generar_binarios(n, cadena + "1")
    

# Ejemplo:
generar_binarios(4)
