import csv, json
from math import fabs


#  Creación del nuevo archivo csv
def create_csv():
    header = ['Fecha analizada', 'Comportamiento de la accion', 'abs Diferencia Close-Open']
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
            difference = fabs(difference)

            with open(file_w, 'a',newline='') as f:
                writer = csv.writer(f,delimiter='\t')
                writer.writerow([row[0],concept,difference])
        


def create_json(file1, file2):
    datos = {}
    volumes = [[], []]
    with open(file1,'r') as f:
        reader = csv.reader(f,delimiter=',')
        next(reader)

        for row in reader:
            volumes[0].append(row[0])
            volumes[1].append(int(row[-1]))

    min_volume = min(volumes[1])
    min_index = volumes[1].index(min_volume)
    max_volume = max(volumes[1])
    max_index = volumes[1].index(max_volume)

    datos['date_lowest_volume'] = volumes[0][min_index]
    datos['lowest_volume'] = min_volume
    datos['date_highest_volume'] = volumes[0][max_index]
    datos['highest_volume'] = max_volume
    datos['mean_volume'] = sum(volumes[1]) / len(volumes[1])

    differences = [[],[]]
    with open(file2,'r') as f:
        reader = csv.reader(f,delimiter='\t')
        next(reader)

        for row in reader:
            differences[0].append(row[0])
            differences[1].append(float(row[-1]))

    max_difference = max(differences[1])
    max_index_difference = differences[1].index(max_difference)

    datos['date_greatest_difference'] = differences[0][max_index_difference]
    datos['greatest_difference'] = max_difference

    with open('detalles.json', 'w') as f:
        json.dump(datos,f, indent=4)

    # print(datos)

def solucion():
    create_csv()
    read_data('JandJ.csv','analisis_archivo.csv')
    create_json('JandJ.csv','analisis_archivo.csv')
