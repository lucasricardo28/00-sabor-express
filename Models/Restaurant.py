from Models.Rate import Rate

class Restaurant:
    '''
    A Classe restaurante.
    '''
    restaurante_list = []

    def __init__(self, name, category):
        '''
        Construtor da classe.
        '''
        self._name = name.title()
        self._category = category.upper()
        self._is_active = False
        self._rate_list = [];

        self.restaurante_list.append(self)

    def __str__(self):
        return f'{self._name}'
    
    @classmethod
    def list(cls):
        '''
        Método da classe para listar todos os restaurantes cadastrados!
        '''
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Nota'.ljust(25)} | {'Status'}')
        for restaurant in cls.restaurante_list:
            print(f'{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {str(restaurant.avg_rate).ljust(25)} | {restaurant.active}')

    @property
    def active(self):
        '''
        Propriedade para conventer em texto.

        Parametro:
        - Self (Obj): Proprio objeto

        Retorno:
        - (str): String ativa ou inativa
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

        Parâmetros:
        - Cliente (str): Nome do cliente
        - Nota (float): Nota que o cliente quer colocar (1 - 5)
        '''
        if 0 < rate <= 5:
            rate = Rate(client, rate)
            self._rate_list.append(rate)

    @property
    def avg_rate(self):
        '''
        Método para calcular a média do objeto selecionado.
        '''
        if not self._rate_list:
            return '-'
        
        sum_value = sum(rate._rate for rate in self._rate_list)
        count = len(self._rate_list)
        return round(sum_value / count, 1)
 
