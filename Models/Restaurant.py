class Restaurant:
    
    restauranteList = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._is_active = False

        self.restauranteList.append(self)

    def __str__(self):
        return f'{self._name}'
    
    @classmethod
    def list(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurant in cls.restauranteList:
            print(f'{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {restaurant.active}')

    @property
    def active(self):
        return '✅' if self._is_active else '❌'

    def change_state(self):
        self._is_active = not self._is_active


testRestaurant = Restaurant('praça', 'Categoria')
testRestaurant.change_state()
testRestaurant2 = Restaurant('praça2', 'Categoria2')

Restaurant.list()