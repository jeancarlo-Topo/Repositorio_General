import time
import random
#Busqueda binaria ocupa que la lista este ordenada, ocupa que tenga un comienzo y un final para buscar, ocupa comparar usando division entera
def search(list,comienzo, final, objective):
    #Primero que todo  ponemos la excepcion, recordar que el min siempre busca un numero, si ese numero es mayor al final de la lista, osea se sale de la lista, entonces no tiene sentido que se haga el codigo porque no abarca la lista que quiero
    print(f' Looking objective {objective} from {list[comienzo]} to {list[final - 1]} ')
    if comienzo > final:
        return False

    #Ponemos la formula que sigue el codigo a continuaicon
    medio = (comienzo + final) // 2 # esto dice: minimo + maximo = el entero de ese valor, compare con el objetivo, dependiendo de si es mayor o menor corte  la lista para calcular mas rapido cual es el numero
    print(f'Valor medio de la lista: {list[medio]}')
    print(f'Valor del indice: {medio}')

    if list[medio] == objective:
        return True

    elif list[medio] < objective:# Aqui digo, si la lista en el indice medio es mayor al objetivo escogido
        return search(list, (medio + 1) , final, objective)
        
    else:
        return search(list , comienzo , medio - 1 , objective)



if __name__ == '__main__':
    list_size =  int(input('Insert the size of the list: '))
    objective = int(input('Insert the value to search for: '))
    initial = time.time()

    list = [random.randint(0,list_size) for i in range(list_size)]#AQUI DIGO, BUSQUEME UN NUMERO DE 0-tamaño de la lista EN EL RECORRIDO QUE TIENE COMO TAMAñO  LA LISTA QUE INSERTE
    list = sorted(list)

   # list = sorted(list)#Aqui acomodo la lista en orden menor a mayor
    print(list)

    found = search(list, 0 , len(list), objective)
    print(f'The element {objective} {"is in the list" if found else "is not in the list" }')#Aqui meti el  if else en una sola linea, asi se haria

    final = time.time()

    print(f' Tiempo de busqueda es {final- initial} segundos' )#Calcule el tiempo que duro dandome el resultado

    