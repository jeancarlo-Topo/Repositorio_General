
class Rectangulo:
    def __init__(self, base, altura) :#ESTA ES LA ESTRUCCTURA INICIAL
        self.base = base
        self.altura = altura


    def area(self):
       new_var = self.base * self.altura # se puede hacer asi o pasarlo todo al return
       return new_var

class Cuadrado(Rectangulo): # Esto se lee asi en herencia: LA CLASE CUADRADO EXTIENDE A RECTANGULO
    def __init__(self, lado):
        super().__init__(lado, lado) #Cuando se hereda se pone la sub clase cuadrado que extiende a rectangulo, luego se pone super como indica el codigo y como se ve que REC recibe base y altura, se cambia a lado * lado

def main():
    print(f'A continuacion el sistema pedira informacion sobre el rectanculo')

    base = float(input('Ingrese la base del Rectangulo: '))
    altura = float(input('Ingrese la altura del Rectangulo: '))

    print(f'A continuacion se pide la informacion del Cuadrado')

    lado = float(input('Ingrese el lado del rectangulo:  '))
    area_Rectangulo = Rectangulo(base, altura)
    area_Cuadrado = Cuadrado(lado)

    area_rect = area_Rectangulo.area()
    area_cuad = area_Cuadrado.area()

    print(f'Area rectangular es: {area_rect}')
    print(f'Area del cuadrado es: {area_cuad}')     

if __name__ == "__main__":
    main()
    