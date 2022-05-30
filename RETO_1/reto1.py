def solucion(b,n):
    intentos = 0

    number_user = int(input(f'Ingrese un número que esté entre 0 y {b} >>> '))

    while True:
        if number_user not in range(0, b + 1):
           print('¡Te saliste del intervalo!') 

        if number_user < n and number_user in range(0, b + 1):
            print('¡Ups! Estás por debajo')
            intentos += 1
        elif number_user > n and number_user in range(0, b + 1):
            print('¡Ups! Te pasaste')
            intentos += 1
        elif number_user == n:
            intentos += 1
            print(f'¡Lo lograste! Usaste {intentos} intentos')
            break

        number_user = int(input(f'Inténtalo de nuevo >>> '))



solucion(25,15)
        