import numpy as np
import math
import random

def encriptado(texto):
    clave = []
    list_unicode = []
    desordenada = []
    n = math.sqrt(len(texto)) #  L e saco la raíz cuadrada a la longitubd del texto
    if (n // 1) != n : n = int((n // 1)) + 1 # realizo división entera y Si arroja un numero float le sumo una unidad y lo casteo a int 

    for i in range(len(texto), n*n): texto += '_' # Agrego guiones a los espacios en blanco. el for inicia donde termina el texto y finaliza en la longitud de la matriz

    for i in texto: list_unicode.append(ord(i)) # Cambio las letras del texto a código entero unicode

    for i in range(len(list_unicode)): clave.append(i) # Guardo los indices de la lista unicode en la lista clave
    random.shuffle(clave) # Mezclo la la clave 

    for i in clave: desordenada.append(list_unicode[i]) # recorro los indices de mi clave y agrego en la lista desordenada lo que traiga list_unicode en cada índice

    matriz_encriptada = np.array(desordenada).reshape(n,n) # creo la matriz a partir de la clave mezclada. la función reshape; crea una matriz a partir de una lista. Recibe como argumento las dimensiones de la matriz

    return matriz_encriptada, clave # retorno la clave y la matriz 


#  Invocamos la función encriptar una matriz. IMPORTANTE: Esteo no debe ir en la plataforma

texto = 'Today is Caturday!'
matriz_encriptada, clave = encriptado(texto)
print(matriz_encriptada, clave)


# Función desencriptar

def desencriptado(matriz_encriptada, clave):
    lista_matriz = matriz_encriptada.flatten().tolist() # Convierto la matríz en una lista. flatten() unifica las listas dentro de la matriz y tolist la transforma a lista
    list_unicode_ordenada = []
    lista_ordenada = []
    for i in range(len(lista_matriz)): # Recorro el largo de la nueva lista creada a partir de la matríz
        posicion = clave.index(i) # almaceno la posición actual que coincida con la posición de la clave encontrada
        list_unicode_ordenada.append(lista_matriz[posicion]) # Agrego en una nueva lista lo que me traiga el paso anterior
 
    for code in list_unicode_ordenada: # recorro mi nueva lista con los valores ordenados
        lista_ordenada.append(chr(code)) # transformo el codigo unicode entero a caracter y lo guaro en una nueva lista
    texto = ''.join(lista_ordenada) # convierto la lista a text

    texto = texto.replace('_','') # Borro los guiones bajos
    return texto

print(desencriptado(matriz_encriptada, clave))

