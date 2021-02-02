valor1 = int(input('Ingrese un valor: '))
enum_exhaustiva = 0
while enum_exhaustiva**2 < valor1:
    enum_exhaustiva += 1
if enum_exhaustiva**2 == valor1:
    print(f'La raiz cuadrada de {valor1} es {enum_exhaustiva}')
else:
    print(f'El numero {valor1} no tiene raiz cuadrada')