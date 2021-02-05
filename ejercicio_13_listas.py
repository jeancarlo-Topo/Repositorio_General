import statistics
 
def run():
    datos = []
    numeros = (input('Ingrese Valores por favor:'))
    while numeros :
        #if numeros == None: Esto que puse aqui sirve para yo poder hacer un break si no meto datos pero el while entiende que si no meto datos hace un break
           # break
        datos.append(numeros)
        numeros = (input('Ingrese Valores por favor:'))
        
    datos  = [float(i) for i in datos]#Esto me agarra y convierte los datos string en int que es lo que necesito
    print(f' Estos son los datos ingresados: {datos} \n La media de la los valores ingresados es: {statistics.mean(datos)}\n La desviacion tipica de los valores de la tabla son: {statistics.stdev(datos)} ')#aqui esta sacando la desv standar de la muestra

    #rint(f' La media de la los valores ingresados es: {statistics.mean(datos)}')
    #print(f' La desviacion tipica de los valores de la tabla son: {statistics.stdev(datos)}')


if __name__ == '__main__':
    run()