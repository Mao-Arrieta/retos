from random import shuffle,sample

balotas = ['B1','B2','B3','B4','B5','B6','B7','B8','B9','B10','B11','B12','B13','B14','B15','I16','I17','I18','I19','I20','I21','I22','I23','I24','I25','I26','I27','I28','I29','I30','N31','N32','N33','N34','N35','N36','N37','N38','N39','N40','N41','N42','N43','N44','N45','G46','G47','G48','G49','G50','G51','G52','G53','G54','G55','G56','G57','G58','G59','G60','O61','O62','O63','O64','O65','O66','O67','O68','O69','O70','O71','O72','O73','O74','O75']


def balotera(balotas):
    b = []; i = []; n = []; g = []; o = []

    for balota in balotas:
        if balota[0] == 'B': b.append(balota)
        elif balota[0] == 'I': i.append(balota)
        elif balota[0] == 'N': n.append(balota)
        elif balota[0] == 'G': g.append(balota)
        elif balota[0] == 'O': o.append(balota)
    b = sample(b, 5); i = sample(i, 5); n = sample(n, 4); g = sample(g, 5); o = sample(o, 5)

    lista = b + i + n + g + o
    shuffle(lista)
    lista = tuple(lista)

    return lista

print(balotera(balotas))
