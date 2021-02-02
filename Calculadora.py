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
8 - Determinacion de raiz cuadrada de un numero
Elige una opcion:"""
opcion = int(input(menu))

def suma(valor1, valor2):
    suma = valor1 + valor2
    return suma

def resta(valor1, valor2):
    resta = valor1 - valor2
    return resta

def multiplicacion(valor1, valor2):
    multiplicacion = valor1*valor2
    return multiplicacion

def division(valor1, valor2):
    division = valor1/valor2
    return division
    #tengo que agregar las opciones donde se vuelve infinito o negativo


def div_entera(valor1, valor2):
    div_entera = valor1%valor2
    return div_entera


def potencia(valor1, valor2):
    potencia = valor1**valor2
    potencia = round(potencia,2)
    return potencia

def raiz(valor1, valor2):
    valor2 = 1 / valor2
    #b = float(b)
    #print(b)
    raiz = valor1 ** valor2
    #print(raiz)
    raiz = round(raiz,2)
    return raiz

def run():
    #a = es el valor 1
    #b = es el valor 2
    if opcion == 1:
        valor1 = float(input('Ingrese un primer valor a sumar: '))
        valor2 = float(input('Ingrese un segundo valor  sumar: '))
        print(f'La suma es: {str(suma(valor1, valor2))}')
        #Aqui estamos usando formatos para printear diferente
    elif opcion == 2 :
        valor1 = float(input('Ingrese un primer valor: '))
        valor2= float(input('Ingrese valor a restar: '))
        print('La resta es: '+ str(resta(valor1, valor2)))
    elif opcion == 3 :
        valor1 = float(input('Ingrese un primer valor: '))
        valor2 = float(input('Ingrese valor por que quieres multiplicar: '))
        print('La Multipliacion es: '+ str(multiplicacion(valor1, valor2)))
    elif opcion == 4 :
        valor1 = float(input('Ingrese un primer valor: '))
        valor2 = float(input('Ingrese un por que quieres dividir: '))
        print('La Division es: '+ str(division(valor1, valor2)))
    elif opcion == 5 :
        valor1 = float(input('Ingrese un primer valor: '))
        valor2 = float(input('Ingrese un por que quieres dividir: '))
        print('La Division entera es: '+ str(div_entera(valor1, valor2)))
    elif opcion == 6 :
        valor1 = float(input('Ingrese valor: '))
        valor2 = float(input('Ingrese la potencia: '))
        print('La potencia  es: '+ str(potencia(valor1, valor2)))
    elif opcion == 7 :
        valor1 = float((input("Ingrese el valor base:")))
        valor2 = float((input("Ingrese el valor raiz a usar:")))
        print(f'La raiz {str(int(valor2))} de {str(int(valor1))}  es {str(raiz(valor1, valor2))}')

#Quiero probar otra vez el branch
if __name__ == '__main__':
    run()