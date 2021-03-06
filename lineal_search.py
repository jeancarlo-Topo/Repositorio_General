
import time
import random

def search(list, objective):
    match = False
    for i in list:
        if i == objective:
            match = True
            break
    return match
if __name__ == '__main__':
    list_size =  int(input('Insert the size of the list: '))
    objective = int(input('Insert the value to search for: '))
    initial = time.time()

    list = [random.randint(0,100) for i in range(list_size)]#AQUI DIGO, BUSQUEME UN NUMERO DE 0-100 EN EL RECORRIDO QUE TIENE COMO TAMAñO  LA LISTA QUE INSERTE

    list = sorted(list)#Aqui acomodo la lista en orden menor a mayor
    print(list)

    found = search(list, objective)
    print(f'The element {objective} {"is in the list" if found else "is not in the list" }')#Aqui meti el  if else en una sola linea, asi se haria

    final = time.time()

    print(f' Tiempo de busqueda es {final- initial} segundos' )#Calcule el tiempo que duro dandome el resultado

    