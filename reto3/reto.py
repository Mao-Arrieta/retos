from random import shuffle


def generar_baraja(tipos_cartas, n_palos):
    baraja = []
    t = 0

    while baraja.count(t) < n_palos:
        for t in tipos_cartas:
            baraja.append(t)

    shuffle(baraja) # Retorna una lista aleatoria con los elementos existentes de una lista
    baraja = tuple(baraja)

    return baraja


cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
palos = 4
print(generar_baraja(cartas, palos))