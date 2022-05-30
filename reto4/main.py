texto = "Llegó a la conclusión que aquel hijo el coronel Aureliano Buendía por quien ella Úrsula Iguarán habría dado la vida, era simplemente un hombre incapacitado para el amor. Una noche, cuando lo tenía en el vientre, lo oyó llorar. Fue un lamento tan definido, que José Arcadio Buendía despertó a su lado y se alegró con la idea de que el niño iba a ser ventrílocuo. Otras personas pronosticaron que sería adivino. Ella, en cambio, se estremeció con la certidumbre de que aquel bramido profundo era un primer indicio de la temible cola de cerdo. Pero la lucidez de la decrepitud le permitió ver, y así lo repitió muchas veces, que el llanto de los niños en el vientre de la madre no es anuncio de ventriloquia ni facultad adivinatoria, sino una señal inequívoca de incapacidad para el amor. Remedios, la bella, se quedó vagando por el desierto de la soledad, sin cruces a cuestas, madurándose en sus sueños sin pesadillas, en sus baños interminables, en sus comidas sin horarios, en sus hondos y prolongados silencios sin recuerdos, hasta una tarde de marzo en que Fernanda quiso doblar en el jardín sus sábanas de bramante, y pidió ayuda a las mujeres de la casa. Apenas habían empezado, cuando Amaranta advirtió que Remedios, la bella, estaba transparentada por una palidez intensa. ¿Te sientes mal? preguntó. Remedios, la bella, que tenía agarrada la sábana por el otro extremo, hizo una sonrisa de lástima."

from operator import itemgetter

lista_palabras = texto.split(" ") # Esto son los datos que creé para probar

def quitar_caracteres(lista):
    caracteres = ['-','¿','?','.',',','¡','!',':','"','–']
    lista = ' '.join(lista)
    lista = lista.lower()
    
    for caracter in caracteres:
        lista = lista.replace(caracter, "")
    
    lista = lista.split(" ")
    
    return lista

def contar_palabras(lista):
    frecuencias = {}
    for palabra in lista:
        if palabra != '':
            frecuencias[palabra] = lista.count(palabra)  

    lista_frecuentes = sorted(frecuencias.items(), key=itemgetter(1), reverse=True)

    frec_ord = [list(lista_frecuentes[i]) for i in range(len(lista_frecuentes))]

    lista_texto = [frec_ord[i] for i in range(20)]

    return lista_texto


def main(lista_texto):
    lista = quitar_caracteres(lista_texto)
    lista_conteo = contar_palabras(lista)
    return lista_conteo

a = main(lista_palabras)
print(a)





















# def quitar_caracteres(lista):
#     from operator import itemgetter
#     caracteres = ['-','¿','?','.',',','¡','!',':','"','–']
#     lista = ' '.join(lista)
#     lista = lista.lower()

#     for caracter in caracteres:
#         lista = lista.replace(caracter, "")
    
#     lista = lista.split()
#     frecuencias = {}
    
#     for palabra in lista:
#         if palabra in frecuencias:
#             frecuencias[palabra] += 1
#         else:
#             frecuencias[palabra] = 1

#     lista_frecuentes = sorted(frecuencias.items(), key=itemgetter(1), reverse=True)

#     frec_ordenada = [list(lista_frecuentes[i]) for i in range(len(lista_frecuentes))]

#     lista_texto = [frec_ordenada[i] for i in range(20)]
    
#     return lista_texto


# def main(lista_texto):
#     # ACÁ INICIA LA FUNCIÓN main
#     lista_conteo = quitar_caracteres(lista_texto)

#     return lista_conteo

# print(main(lista_palabras))

