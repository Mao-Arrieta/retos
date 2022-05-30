def solucion():
    print("¡Bienvenido! En esta aplicación los estudiantes podrán gestionar las notas de su materia.")
    nombre = input("Por favor ingrese su nombre: ")
    materia = input("Ingrese el nombre de la materia: ")
    notas = porcentaje = p = n = 0
    n = float(input("Ingrese la nota obtenida: ")) # con punto
    p = int(input("Ingrese el porcentaje de la nota: "))
    n *= p / 100
    notas += n
    porcentaje += p

    while porcentaje != 100:        
        if porcentaje == 0 or porcentaje < 100:
            dec= input("¿Falta añadir notas? S/N ").upper()
            if dec == 'S':   
                n = float(input("Ingrese la nota obtenida: ")) # con punto
                p = int(input("Ingrese el porcentaje de la nota: "))
                n *= p / 100
                notas += n
                porcentaje += p
            if dec == 'N':
                break

        if porcentaje > 100:
            print("El porcentaje evaluado de una materia no puede ser mayor a 100")
            notas -= n
            porcentaje -= p
            n=float(input("Ingrese la nota obtenida: ")) # con punto
            p=int(input("Ingrese el porcentaje de la nota: "))
            n *= p / 100
            notas += n
            porcentaje += p

    if notas >=3:
        print(f"El estudiante {nombre.capitalize()} cursó la materia {materia.capitalize()} y obtuvo {round(notas, 2)} resultando en aprobado")
    else:
        print(f"El estudiante {nombre.capitalize()} cursó la materia {materia.capitalize()} y obtuvo {round(notas, 2)} resultando en reprobado")

solucion()