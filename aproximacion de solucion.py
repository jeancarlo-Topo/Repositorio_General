objetivo = int(input('Ingrese un numero: '))
epsilon = float(input('Cual es la incertidumbre con la que quieres trabajar: '))# Esto es la incertidumbre con la que trabajo que puede ser 10% o 1% o menor, depende de cuanto quiero que trabaje
paso = epsilon**2#Esto es lo que se iria sumando a la respuesta cada vez que pase por el ciclo 
respuesta = 0.0 #Apartir de aqui comienza el contador
while abs(respuesta**2 - objetivo)>= epsilon and respuesta <= objetivo :# en este l respuesta al cuadrado  - el objetivo sea mayor al epsilon usado y que esa respuesta sea menor al objetivo entonces se sigue aplicando el while, en elmomento que la res**2- objetivo sea menor al epsilon y ademas que esa respuesta sea mayor al objetivo entonces se cierra el loop
    respuesta = respuesta + paso
if abs(respuesta**2 - objetivo)>= epsilon:
    print(f'{objetivo} no tiene una raiz cuadrada')
else :
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')


