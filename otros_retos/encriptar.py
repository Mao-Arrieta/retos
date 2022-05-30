"""
Encriptar y desencriptar un mensaje

Dado un mensaje realizar las siguientes tareas
TAREAS: 
1 - Extraer los caracteres únicos
2 - Crear una clave de encripción, esto consistirá de un diccionario con elementos que tendrán por clave los elementos extraidos en el paso anterior y por valor las letras del alfabeto del inglés en mayúsculas
3- Encriptar el mensaje usando la clave anterior generada, es decir, debe reescribir el mensaje intercambiando los caracteres originales por los correspondientes del alfabeto según el diccionario.
Hasta este punto se debe tener la clave de encripción y el mensaje codificado. Ahora para crear un decodificador debe:
4 - Invertir la clave de encripción, es decir, poner los valores como claves y las claves como valores.
5 - Desencriptar el mensaje usando la clave invertida de forma similar como codificó el mensaje, el resultado debe ser el mensaje original. 

ENTRADA: La función encriptador(mensaje)
función desencriptar(encriptado = str, clave = {})

SALIDAS:
La función 𝑒𝑛𝑐𝑟𝑖𝑝𝑡𝑎𝑑𝑜𝑟 tiene el mensaje encriptado y la clave de encriptación
como salida.
La función 𝑑𝑒𝑠𝑒𝑛𝑐𝑟𝑖𝑝𝑡𝑎𝑑𝑜𝑟 tiene el mensaje desencriptado como salida.

"""

alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def encriptar(mensaje):
    # Extraer los valores únicos del mensaje
    vlr_unicos = []
    [vlr_unicos.append(x) for x in mensaje if x not in vlr_unicos]
    
    clave = {}
    lista_encriptada = []
    i = 0

    #  dar valores al diccionario
    while i < len(vlr_unicos):
        clave[vlr_unicos[i]] = alfabeto[i]
        i += 1

    #  Encriptar el mensaje
    for i in range(len(mensaje)):
        letra_mensaje = mensaje[i]
        letra_encriptada = clave[letra_mensaje]
        lista_encriptada.append(letra_encriptada)

    encriptado = ''.join(lista_encriptada) # convertir la lista a un string
    return encriptado, clave

encriptado,clave = encriptar('Hola a todos los pythonistas')

print(encriptado,clave)

def desencriptar(encriptado,clave):
    lista_desencriptar = []
    nueva_clave = {}
    encriptado = list(encriptado)  # converir mensaje encriptado a una lista

    #  Invertir diccionario
    for k, v in clave.items():
        nueva_clave[v] = k

    # Desencriptar el mensaje
    for i in range(len(encriptado)):
        letra_encriptado = encriptado[i]
        nuevo_valor = nueva_clave[letra_encriptado]
        lista_desencriptar.append(nuevo_valor)

    desencriptado=''.join(lista_desencriptar)

    return desencriptado

print(desencriptar(encriptado,clave))


