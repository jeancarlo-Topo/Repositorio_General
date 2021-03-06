
class coordenadas:
    def __init__(self, x,y) :#ESTA ES LA ESTRUCCTURA INICIAL
        self.x = x
        self.y = y


    def distancia(self,otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2
        dist = (x_diff + y_diff)**0.5
        dist = round(dist, 2)
        return dist
    

if __name__ == "__main__":
    x1 = float(input('Ingrese la coordenada inicial "x": '))
    y1 = float(input('Ingrese la coordenada inicial "y": '))
    x2 = float(input('Ingrese la segunda coordenada "x": '))
    y2 = float(input('Ingrese la segunda coordenada "y": '))

    coord_1 = coordenadas(x1, y1)
    coord_2 = coordenadas(x2, y2)
    dist = coord_1.distancia(coord_2)#Aqui lo que hago es calculo de la distancia entre la coordenada 1 y la 2

    print(f'La distancia en linea recta entre las coordenadas {x1},{y1} y {x2},{y2} es {dist}')