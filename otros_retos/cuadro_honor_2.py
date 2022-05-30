def calcular_promedio_y_cuadro_honor(grupo):
    lista = []
    notas = 0
    
    for estudiante in grupo:
        nota = estudiante['nota_fundamentos']
        notas += nota
        if nota not in lista: lista.append(nota)

    lista.sort()
    promedio = notas / len(grupo)
    resultado = {}

    puesto1 = [estudiante['cedula'] for estudiante in grupo if estudiante['nota_fundamentos'] == lista[-1]]
    resultado[1] = puesto1

    puesto2 = [estudiante['cedula'] for estudiante in grupo if estudiante['nota_fundamentos'] == lista[-2]]
    resultado[2] = puesto2

    puesto3 = [estudiante['cedula'] for estudiante in grupo if estudiante['nota_fundamentos'] == lista[-3]]
    resultado[3] = puesto3

    return promedio, resultado


grupo = [
    {'cedula': '00014301503', 'nombre': 'Pepito','nota_fundamentos': 4.3},
    {'cedula': '1037678471', 'nombre':'Fulanito','nota_fundamentos': 3.2},
    {'cedula': '71023567', 'nombre':' Pancho', 'nota_fundamentos': 5},
    {'cedula': '32276123', 'nombre':'Rita','nota_fundamentos': 4.7},
    {'cedula':'1036765245', 'nombre':'Anita','nota_fundamentos': 4.7},
    {'cedula':'89122456', 'nombre':'Pedrito','nota_fundamentos': 4.7},
    {'cedula':'289765345', 'nombre':'Mat','nota_fundamentos': 4.8},
    {'cedula':'4576890', 'nombre':'Dan','nota_fundamentos': 4.8},
]

print(calcular_promedio_y_cuadro_honor(grupo))