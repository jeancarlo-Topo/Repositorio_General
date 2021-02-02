def run():
    objetivo = int(input('Ingrese un numero: '))
    tolerancia = float(input('Ingrese la tolerancia con la que quiere trabajar: '))
    #   El if lo que me hace es que si diera un valor mayor a 1 entonces me lo divide para que el sistema lo use como tolerancia
    if tolerancia < 1 :
        tolerancia = tolerancia/100
    else :
        tolerancia = tolerancia

    bajo = 0.0
    alto = max(1, objetivo)
    respuesta = (alto + bajo)/2

    while abs(respuesta**2 - objetivo) >= tolerancia :
        print(f'Bajo = {bajo}, Alto = {alto} , Respuesta = {respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto + bajo)/2
    print(f' La raiz cuadrada del {objetivo} es la {respuesta}')



if __name__ == "__main__":
    run()
