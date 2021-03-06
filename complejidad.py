import time
import sys



def factorial(valor):
    #Aqui el factorial es un int <= a 1, la formula de factorial es n*(n-1)!, esta es la que estaremos integrando a la calculadora
    #if valor1 == 1:
     #   return 1
    #elif valor1 == 0 :
    #    return 1 OJO QUE AQUI LO PODIA HACER SEPARADO PERO ES LO MISMO QUE DECIR QUE SI EL NUMERO ES MENOR A 2 , OSEA 1 Y 0 ENTONCES DEVUELVAME 1
    if valor < 2 :
        return 1
    return valor * factorial(valor-1)

if __name__ == '__main__':
    valor = int(input('Ingrese un numero: '))
    sys.setrecursionlimit(1000000)

    inicio = time.time()

    factorial(valor)
    #print(factorial(valor))

    final = time.time()
    
    print( final - inicio)

