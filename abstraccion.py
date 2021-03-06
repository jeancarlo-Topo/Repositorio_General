
class Lavadora:
    def __init__(self):
        pass
    
    def lavar(self, temperatura = '25 grados'):
        self._llenado(temperatura)
        self._inicioCiclo()
        self._centrifuga()
    
    def _llenado(self, temperatura):
        print(f'LLenando la lavadora con {temperatura}')

    def _inicioCiclo(self):
        print(f'Dando vuelta por  minutos')

    def _centrifuga(self):
        print(f'Ropa secada, por favor tender ropa')
    
if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()