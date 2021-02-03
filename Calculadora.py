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
9 - Factoriales
Elige una opcion:"""
opcion = int(input(menu))

def suma(valor1, valor2):
    sumatoria = valor1 + valor2
    return sumatoria
    # esta suma es ineficiente, si quisiera sumar muchos datos no podria, hay que revisar eso

def resta(valor1, valor2):
    resta = valor1 - valor2
    return resta
    #ineficiente, revisar eso que se indico en la suma

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
    poten = valor1**valor2
    poten = round(poten,2)
    return poten

def raiz(valor1, valor2):
    valor2 = 1 / valor2
    raiz = valor1 ** valor2
    raiz = round(raiz,2)
    return raiz
    #Hay que revisar lo que hay que hacer para variables negativas
def factorial(valor1):
    #Aqui el factorial es un int <= a 1, la formula de factorial es n*(n-1)!, esta es la que estaremos integrando a la calculadora
    if valor1 == 1:
        return 1
    return valor1 * factorial(valor1-1)

def run():
    if opcion == 1:
        valor1 = float(input('Ingrese un primer valor a sumar: '))
        valor2 = float(input('Ingrese un segundo valor  sumar: '))
        print(f'La suma es: {suma(valor1, valor2)}')
        #Aqui estamos usando formatos para printear diferente
    elif opcion == 2 :
        valor1 = float(input('Ingrese un primer valor: '))
        valor2= float(input('Ingrese valor a restar: '))
        print(f'La resta es {resta(valor1, valor2)}')
    elif opcion == 3 :
        valor1 = float(input('Ingrese un primer valor: '))
        valor2 = float(input('Ingrese valor por que quieres multiplicar: '))
        print(f'La Multipliacion es {multiplicacion(valor1, valor2)}')
    elif opcion == 4 :
        valor1 = float(input('Ingrese un primer valor: '))
        valor2 = float(input('Ingrese un por que quieres dividir: '))
        print(f'La Division es {division(valor1, valor2)}')
    elif opcion == 5 :
        valor1 = float(input('Ingrese un primer valor: '))
        valor2 = float(input('Ingrese un por que quieres dividir: '))
        print(f'La Division entera es {div_entera(valor1, valor2)}')
    elif opcion == 6 :
        valor1 = float(input('Ingrese valor: '))
        valor2 = float(input('Ingrese la potencia: '))
        print(f'La potencia  es {potencia(valor1, valor2)}')
    elif opcion == 7 :
        valor1 = float((input("Ingrese el valor base:")))
        valor2 = float((input("Ingrese el valor raiz a usar:")))
        print(f'La raiz {str(int(valor2))} de {str(int(valor1))}  es {str(raiz(valor1, valor2))}')
    elif opcion == 8 :
        print(f'Actualmente se esta trabajando en integrar esta funcion')
    elif opcion == 9 :
        valor1 = int(input("Ingrese un numero: "))
        if valor1 < 0 :
            valor1 = abs(valor1)
            print(f' No se puede valorar un negativo, por lo tanto se toma su valor absoluto')
        print(f' El factorial de {valor1} es {factorial(valor1)}')

#Quiero probar otra vez el branch
if __name__ == '__main__':
    run()