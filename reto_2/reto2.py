pensum = [
        {
            '0123': {'nombre': 'intro a la ing', 'créditos': 2},
            '4567': {'nombre': 'inglés', 'créditos': 1}
        },
        {},
        {}
]

semestre = 1
materia = '0123'
nombre = 'Lectoescritura'
creditos = 3

def modificar_materia(pensum, semestre, materia, nombre, creditos):
    contenido_semestre = {}

    while True:
        if semestre > 0 and semestre <= len(pensum):
            contenido_semestre = pensum[semestre - 1]
        else:
            mensaje = 'Ingrese una semestre válido'
            break

        if len(contenido_semestre) == 0: 
            mensaje = 'El semestre no tiene materias'
            break

        if materia not in contenido_semestre:
            mensaje = 'La materia no existe'
            break

        contenido_semestre[materia]['nombre'] = nombre
        contenido_semestre[materia]['créditos'] = creditos

        mensaje = 'Modificada con éxito'
        break

    return mensaje

print(modificar_materia(pensum, semestre, materia, nombre, creditos))


print(pensum)