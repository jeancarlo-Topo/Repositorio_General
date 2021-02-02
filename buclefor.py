diccionario = {
    'nombre' : 'Jean Carlos',
    'edad' : 28,
    'cursos': ['Python','Django','JavaScript'], 
    'universidad' : 'UCR',
    'novia' : 'diana',
    'crush' : 'cynthia',
    }
def run():
    for run in diccionario.keys():
        if run == 'edad':
            pass
        print(run)

if __name__ == "__main__":
    run()

