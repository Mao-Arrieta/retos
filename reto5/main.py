import csv
import json


def clima():
    resultado = {}

    with open('data_nuevo.csv', 'w', newline='') as file_csv:
        fieldnames=['id','location','temperature','pressure','above_avg_temp','above_avg_pres'] #  Nombra los encabezados
        writer=csv.DictWriter(file_csv, fieldnames=fieldnames, delimiter=',') #  Inserta los encabezados
        writer.writeheader()

    with open('data.csv', 'r') as file:
        reader = csv.reader(file,delimiter=',')
        next(reader)

        lista1 = []; lista2 = []; lista3 = []; lista4 = []; lista5 = []; temp = []; press = []
        temp2 = []; press2 = []; temp3 = []; press3 = []; temp4 = []; press4 = []; temp5 = []; press5 = [];

        for row in reader:
            if row[1] == '1':
                temp.append(int(row[2])) 
                press.append(int(row[3]))
            elif row[1] == '2':
                temp2.append(int(row[2])) 
                press2.append(int(row[3]))
            if row[1] == '3':
                temp3.append(int(row[2])) 
                press3.append(int(row[3]))
            if row[1] == '4':
                temp4.append(int(row[2])) 
                press4.append(int(row[3]))
            if row[1] == '5':
                temp5.append(int(row[2])) 
                press5.append(int(row[3]))

        temp_prom = round(sum(temp)/len(temp),1)
        lista1.append(temp_prom)
        press_prom = round(sum(press)/len(press),1)
        lista1.append(press_prom)
        resultado["1"] = lista1

        temp_prom2 = round(sum(temp2)/len(temp2),1)
        lista2.append(temp_prom2)
        press_prom2 = round(sum(press2)/len(press2),1)
        lista2.append(press_prom2)
        resultado["2"] = lista2

        temp_prom3 = round(sum(temp3)/len(temp3),1)
        lista3.append(temp_prom3)
        press_prom3 = round(sum(press3)/len(press3),1)
        lista3.append(press_prom3)
        resultado["3"] = lista3

        temp_prom4 = round(sum(temp4)/len(temp4),1)
        lista4.append(temp_prom4)
        press_prom4 = round(sum(press4)/len(press4),1)
        lista4.append(press_prom4)
        resultado["4"] = lista4

        temp_prom5 = round(sum(temp5)/len(temp5),1)
        lista5.append(temp_prom5)
        press_prom5 = round(sum(press5)/len(press5),1)
        lista5.append(press_prom5)
        resultado["5"] = lista5

        datos = json.dumps(resultado, indent=4)
        with open('datos_json.json', 'w') as file_json:
            json.dump(resultado,file_json)

        above_temp = ''
        above_press = ''
        with open('data.csv', 'r') as file:
            reader = csv.reader(file,delimiter=',')
            next(reader)

            with open('data_nuevo.csv', 'a', newline='') as f:
                writer = csv.writer(f, delimiter=',')
                for row in reader:
                    if row[1] == '1':
                        if int(row[2]) > resultado['1'][0]: above_temp = 'SI'
                        elif int(row[2]) < resultado['1'][0]: above_temp = 'NO'
                        elif int(row[2]) == resultado['1'][0]: above_temp = 'IGUAL'

                        if int(row[3]) > resultado['1'][1]: above_press = 'SI'
                        elif int(row[3]) < resultado['1'][1]: above_press = 'NO'    
                        elif int(row[3]) == resultado['1'][1]: above_press = 'IGUAL'  

                    if row[1] == '2':
                        if int(row[2]) > resultado['2'][0]: above_temp = 'SI'
                        elif int(row[2]) < resultado['2'][0]: above_temp = 'NO'
                        elif int(row[2]) == resultado['2'][0]: above_temp = 'IGUAL'

                        if int(row[3]) > resultado['2'][1]: above_press = 'SI'
                        elif int(row[3]) < resultado['2'][1]: above_press = 'NO'    
                        elif int(row[3]) == resultado['2'][1]: above_press = 'IGUAL'  

                    if row[1] == '3':
                        if int(row[2]) > resultado['3'][0]: above_temp = 'SI'
                        elif int(row[2]) < resultado['3'][0]: above_temp = 'NO'
                        elif int(row[2]) == resultado['3'][0]: above_temp = 'IGUAL'

                        if int(row[3]) > resultado['3'][1]: above_press = 'SI'
                        elif int(row[3]) < resultado['3'][1]: above_press = 'NO'    
                        elif int(row[3]) == resultado['3'][1]: above_press = 'IGUAL'             

                    if row[1] == '4':
                        if int(row[2]) > resultado['4'][0]: above_temp = 'SI'
                        elif int(row[2]) < resultado['4'][0]: above_temp = 'NO'
                        elif int(row[2]) == resultado['4'][0]: above_temp = 'IGUAL'

                        if int(row[3]) > resultado['4'][1]: above_press = 'SI'
                        elif int(row[3]) < resultado['4'][1]: above_press = 'NO'    
                        elif int(row[3]) == resultado['4'][1]: above_press = 'IGUAL'             

                    if row[1] == '5':
                        if int(row[2]) > resultado['5'][0]: above_temp = 'SI'
                        elif int(row[2]) < resultado['5'][0]: above_temp = 'NO'
                        elif int(row[2]) == resultado['5'][0]: above_temp = 'IGUAL'

                        if int(row[3]) > resultado['5'][1]: above_press = 'SI'
                        elif int(row[3]) < resultado['5'][1]: above_press = 'NO'    
                        elif int(row[3]) == resultado['5'][1]: above_press = 'IGUAL'             

                    writer.writerow([row[0], row[1], row[2],row[3], above_temp, above_press])
                
    return datos

clima()