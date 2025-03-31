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


# Ejercicio 4

def verificar_nombre(nombre):
    if len(nombre) < 5:
        return False
    if not any(i.isdigit() for i in nombre):
        return False
    if not any(i.isupper() for i in nombre):
        return False
    if not any(i.isalnum() for i in nombre):
        return False
    else:
        return True
    
# Ejercicio 5

def cat_vel(velocidad):
    if velocidad < 200:
        return 1
    elif velocidad >= 200 and velocidad <= 500:
        return 2
    elif velocidad > 500:
        return 3
