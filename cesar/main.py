# ENCRIPTAR CARACTER
def encriptar_caracter(caracter, b):
    alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    caracter_encriptado = ''

    if caracter in alfabeto:
        indice = alfabeto.index(caracter)
        caracter_encriptado = (indice + b) % len(alfabeto)
        caracter_encriptado = alfabeto[caracter_encriptado]
    else:
        caracter_encriptado = caracter
    
    return caracter_encriptado


# ENCRIPTAR MENSAJE     
def encriptar(mensaje, b):
    mensaje_encriptado = ''

    for letra in mensaje:
        letra = encriptar_caracter(letra, b)
        mensaje_encriptado += letra
      
    return mensaje_encriptado

# print(encriptar('U DE A', 7))


# DESENCRIPTAR CARACTER     
def desencriptar_caracter(caracter_encriptado, b):
    alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    caracter_desencriptado = ''

    if caracter_encriptado in alfabeto:
        indice = alfabeto.index(caracter_encriptado)
        caracter_desencriptado = (indice - b) % len(alfabeto)
        caracter_desencriptado = alfabeto[caracter_desencriptado]
    else:
        caracter_desencriptado = caracter_encriptado
 
    return caracter_desencriptado


# DESENCRIPTAR MENSAJE   
def desencriptar(mensaje_encriptado, b):
    mensaje_desencriptado = ''

    for letra in mensaje_encriptado:
        letra = desencriptar_caracter(letra, b)
        mensaje_desencriptado += letra
     
    return mensaje_desencriptado

mensaje_encriptado = encriptar('U DE A', 7)
print('Mensaje encriptado')
print(mensaje_encriptado)

print('\nMensaje desencriptado')
print(desencriptar(mensaje_encriptado, 7))
