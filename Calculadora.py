menu = """
Bienvenido ala calculadora,con el tiempo la funcionalidad de la calculadora
mejoraria con la implementacion de nuevas funciones, mientras tanto.. disfruta y
juega con ella =)
1 - Suma
2 - Resta
3 - Multiplicacion
4 - Division
5 - Division Entera
6 - Potencia
7 - Raiz
Elige una opcion:"""
opcion = int(input(menu))

def suma(a, b):
    suma = a + b
    return suma

def resta(a, b):
    resta = a - b
    return resta

def multiplicacion(a, b):
    multiplicacion = a*b
    return multiplicacion
    
def division(a, b):
    division = a/b
    return division


def div_entera(a, b):
    div_entera = a%b
    return div_entera


def potencia(a, b):
    potencia = a**b
    potencia = round(potencia,0)
    return potencia

def raiz(a, b):
    b = 1 / b
    #b = float(b)
    #print(b)
    raiz = a ** b
    #print(raiz)
    raiz = round(raiz,3)
    return raiz

def run():    
    #a = es el valor 1
    #b = es el valor 2
    if opcion == 1:
        a = float(input('Ingrese un primer valor a sumar: '))
        b = float(input('Ingrese un segundo valor  sumar: '))
        print('La suma es: '+ str(suma(a, b)))
    elif opcion == 2 :
        a = float(input('Ingrese un primer valor: '))
        b = float(input('Ingrese valor a restar: '))
        print('La resta es: '+ str(resta(a, b)))
    elif opcion == 3 :
        a = float(input('Ingrese un primer valor: '))
        b = float(input('Ingrese valor por que quieres multiplicar: '))
        print('La Multipliacion es: '+ str(multiplicacion(a, b)))
    elif opcion == 4 :
        a = float(input('Ingrese un primer valor: '))
        b = float(input('Ingrese un por que quieres dividir: '))
        print('La Division es: '+ str(division(a, b)))
    elif opcion == 5 :
        a = float(input('Ingrese un primer valor: '))
        b = float(input('Ingrese un por que quieres dividir: '))
        print('La Division entera es: '+ str(div_entera(a, b)))
    elif opcion == 6 :
        a = float(input('Ingrese valor: '))
        b = float(input('Ingrese la potencia: '))
        print('La potencia  es: '+ str(potencia(a, b)))
    elif opcion == 7 :
        a = float((input("Ingrese el valor base:")))
        b = float((input("Ingrese el valor raiz a usar:")))
        print('La raiz ' + str(b) +' de ' + str(a) + ' es '+ str(raiz(a, b)))

#Quiero probar otra vez el branch
if __name__ == '__main__':
    run()
    