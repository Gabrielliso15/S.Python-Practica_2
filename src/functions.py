# Ejercicio 1

def Cumple(linea):
    palabras = linea.split()
    if len(palabras) > 1 and palabras[1][0].lower() in "aeiou":
        return True
    return False

# Ejercicio 3

def Cumple3 (linea,clave):
    if clave in linea:
        return True
    return False