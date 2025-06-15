class Rate:
    '''
    Classe que simboliza as avaliações de cada cliente
    '''
    def __init__(self, client, rate):
        '''
        Construtor da classe
        '''
        self._client = client
        self._rate = rate