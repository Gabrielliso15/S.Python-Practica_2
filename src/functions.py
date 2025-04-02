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

# Ejercicio 7
import random
import datetime
import string

def cumple_nombre (nombre):
    if len(nombre) > 15 or " " in nombre or nombre[0] == " ":
        return False
    return True

def codigo_descuento (nombre):
    fecha = datetime.date.today()
    fecha = str(fecha).replace("-", "")
    cod1 = f"{nombre.upper()}-{fecha}-"   
    cod2= random.choices(string.ascii_uppercase + string.digits, k=30 - len(cod1))
    codfinal = cod1 + "".join(cod2)
    return codfinal

# Ejercicio 8
def son_anagramas (s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    s1 = sorted(s1)
    s2 = sorted(s2)
    if s1 == s2:
        return True
    else:
        return False
