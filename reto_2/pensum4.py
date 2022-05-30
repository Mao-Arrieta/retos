pensum = [
        {
            '0123': {'nombre': 'intro a la ing', 'créditos': 2},
            '4567': {'nombre': 'inglés', 'créditos': 1}
        },
        {},
        {}
]

# Validar que el semestre sea válido
def es_semestre_valido(pensum, semestre):
    if semestre > 0 and semestre <= len(pensum):
        return True


#  Validar que el semestre contenga información
def es_semestre_vacio(pensum,semestre):
    if es_semestre_valido(pensum, semestre) and len(pensum[semestre - 1]) == 0:
        return True


# Validar que la materia sea válida
def es_materia_valida(pensum,semestre, materia):
    if es_semestre_valido(pensum, semestre) and es_semestre_vacio(pensum, semestre) != True:
        contenido = pensum[semestre-1]
        if materia in contenido:
            return True


# Modificar una materia del semestre
def modificar_materia(pensum, semestre, materia, nombre, creditos):
    contenido_semestre = {}
    if es_semestre_valido(pensum, semestre) and es_semestre_vacio(pensum, semestre) != True and es_materia_valida(pensum,semestre, materia):
        contenido_semestre = pensum[semestre-1]
        contenido_semestre[materia]['nombre'] = nombre
        contenido_semestre[materia]['créditos'] = creditos


# Eliminar una materia del semestre
def eliminar_materia(pensum, semestre, materia):
    contenido_semestre = {}
    if es_semestre_valido(pensum, semestre) and es_semestre_vacio(pensum, semestre) != True and es_materia_valida(pensum,semestre, materia):
        contenido_semestre = pensum[semestre-1]
        del(contenido_semestre[materia])


eliminar_materia(pensum, semestre =1, materia='0123')

print(pensum)