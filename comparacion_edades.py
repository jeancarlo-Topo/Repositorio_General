def run():
    nombre1 = input("Ingresa un nombre: ")
    edad1   = int(input("Ingresa su edad: "))
    nombre2 = input("Ingresa otro nombre: ")
    edad2   = int(input("Ingresa su edad: "))

    if edad1 < edad2 :
        print(f'{nombre1} con {edad1} años es menor a {nombre2} con {edad2} años.')
    elif edad1 > edad2 :
        print(f'{nombre1} con {edad1} años es mayor a {nombre2} con {edad2} años.')
    else :
        print(f'{nombre1} y {nombre2} tienen la misma edad')

if __name__ == "__main__":
    run()