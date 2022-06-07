import csv, json

#  Creación del nuevo archivo csv
def create_csv():
    header = ['Fecha', 'Comportamiento de la accion', 'Punto medio HIGH-LOW']
    with open('analisis_archivo.csv','w', newline='') as f:
        writer = csv.DictWriter(f,fieldnames=header,delimiter='\t')
        writer.writeheader()


def read_data(file, file_w):
    concept = ''
    with open(file,'r') as f:
        reader = csv.reader(f,delimiter=',')
        next(reader)
    
        for row in reader:
            difference = float(row[4]) - float(row[1])
            if difference > 0: concept = 'SUBE'
            elif difference < 0: concept = 'BAJA'
            elif difference == 0: concept = 'ESTABLE'
            high_low = (float(row[2]) - float(row[3])) / 2

            with open(file_w, 'a',newline='') as f:
                writer = csv.writer(f,delimiter='\t')
                writer.writerow([row[0],concept,high_low])
        


def create_json(file1, file2):
    datos = {} # alamaceno mis datos
    prices = [[], [], []]
    with open(file1,'r') as f:
        reader = csv.reader(f,delimiter=',')
        next(reader)

        for row in reader:
            prices[0].append(row[0]) # fechas
            prices[1].append(float(row[2])) # Highs
            prices[2].append(float(row[3])) # Lows

    min_price = min(prices[2])
    min_index = prices[2].index(min_price)
    max_price = max(prices[1])
    max_index = prices[1].index(max_price)

    datos['date_lowest_price'] = prices[0][min_index]
    datos['lowest_price'] = min_price
    datos['date_highest_price'] = prices[0][max_index]
    datos['highest_price'] = max_price

    behaivors = []
    with open(file2,'r') as f:
        reader = csv.reader(f,delimiter='\t')
        next(reader)

        for row in reader:
            behaivors.append(row[1])

    datos['cantidad_veces_sube'] = behaivors.count('SUBE')
    datos['cantidad_veces_baja'] = behaivors.count('BAJA')
    datos['cantidad_veces_estable'] = behaivors.count('ESTABLE')

    with open('detalles.json', 'w') as f:
        json.dump(datos,f, indent=4)


def solucion():
    create_csv()
    read_data('GLOBANT.csv','analisis_archivo.csv')
    create_json('GLOBANT.csv','analisis_archivo.csv')

# solucion()
