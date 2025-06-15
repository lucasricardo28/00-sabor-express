from Models.Rate import Rate

class Restaurant:
    '''
    A Classe restaurante é o meu primeiro model respresntando um restaurante.
    '''
    restauranteList = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._is_active = False
        self._rateList = [];

        self.restauranteList.append(self)

    def __str__(self):
        return f'{self._name}'
    
    @classmethod
    def list(cls):
        '''
        Método da classe para listar todos os restaurantes cadastrados!
        '''
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} |  {'Nota'.ljust(25)} | {'Status'}')
        for restaurant in cls.restauranteList:
            print(f'{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} {str(restaurant.avg_rate).ljust(25)} | {restaurant.active}')

    @property
    def active(self):
        '''
        Propriedade para conventer em texto.
        '''
        return '✅' if self._is_active else '❌'

    def change_state(self):
        '''
        Método do objeto para mudar o status negando o antigo valor.
        '''
        self._is_active = not self._is_active

    
    def add_new_rate(self, client, rate):
        '''
        Método do objeto para adicionar uma nova avaliação.
        '''
        rate = Rate(client, rate)
        self._rateList.append(rate)

    @property
    def avg_rate(self):
        '''
        Método para calcular a média do objeto selecionado.
        '''
        if not self._rateList:
            return 0
        
        sumValue = sum(rate._rate for rate in self._rateList)
        count = len(self._rateList)
        return round(sumValue / count, 1)
    
