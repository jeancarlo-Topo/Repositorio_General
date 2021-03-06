import time
import random
def ordenamiento_burb(lista):
    n = len(lista)
    for i in range(n):#rECORRE DE 0 HASTA LA LINGITUD DE LA LISTA
        for j in range( 0, n - i -1): #AQUI LO QUE DIGO ES QUE X EN UN RANGO DONDE VA DE 0 HASTA DONDE RECORRIO EL I DE ARRIBA( N(LONGITUD)- I =)
            if lista[j]> lista[j+1]:
                lista[j], lista[j+1] =lista[j+1], lista[j]#Aqui digo si el indice siguiente es mayor al que tengo, intercambielo
    return lista

if __name__ == '__main__':
    list_tamaño = int(input('Ingrese el tamaño de la lista: '))
    initial = time.time()

    lista = [random.randint(0,list_tamaño) for i in range(list_tamaño)]

    print(lista)
    
    lista_ordenada = ordenamiento_burb(lista)
    print(lista_ordenada)


    final = time.time()

    print(f' Tiempo de busqueda es {final- initial} segundos' )