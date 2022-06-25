import csv, json, math

#  Creación del nuevo archivo csv
def create_csv():
    header = ['Fecha', 'Comportamiento_de_la_accion', 'Diferencia_absoluta_open-high']
    with open('analisis_archivo.csv','w', newline='') as f:
        writer = csv.DictWriter(f,fieldnames=header,delimiter=' ')
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
            
            diff_high = float(row[4]) - float(row[2])
            diff_high = math.fabs(diff_high)
            potencia = diff_high  ** 2
            abs_diffe = math.sqrt(potencia)

            with open(file_w, 'a',newline='') as f:
                writer = csv.writer(f,delimiter=' ')
                writer.writerow([row[0],concept,abs_diffe])
        


def create_json(file1, file2):
    datos = {} # alamaceno mis datos
    resultado = [[], [], [], []]
    with open(file1,'r') as f:
        reader = csv.reader(f,delimiter=',')
        next(reader)

        for row in reader:
            resultado[0].append(row[0]) # fechas
            resultado[1].append(int(row[-1])) # volumenes

    min_volume = min(resultado[1])
    min_index = resultado[1].index(min_volume)
    promedio = sum(resultado[1]) / len(resultado[1])


    datos['date_lowest_volume'] = resultado[0][min_index]
    datos['lowest_volume'] = min_volume
    datos['mean_volume'] = promedio

    with open(file2,'r') as f:
        reader = csv.reader(f,delimiter=' ')
        next(reader)

        for row in reader:
            resultado[-1].append(row[0])
            resultado[2].append(float(row[2]))
    
    min_diff = min(resultado[2])
    index_min_diff = resultado[2].index(min_diff)
    max_diff = max(resultado[2])
    index_max_diff = resultado[2].index(max_diff)

    datos['date_greatest_difference'] = resultado[-1][index_max_diff]
    datos['greatest_difference'] = max_diff
    datos['date_smallest_difference'] = resultado[-1][index_min_diff]
    datos['smallest_difference'] = min_diff


    with open('detalles.json', 'w') as f:
        json.dump(datos,f, indent=4)


def solucion():
    create_csv()
    read_data('AMAZON.csv','analisis_archivo.csv')
    create_json('AMAZON.csv','analisis_archivo.csv')

solucion()