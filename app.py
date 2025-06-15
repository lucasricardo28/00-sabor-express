import random
from Models.Restaurant import Restaurant


restaurant_brasil = Restaurant('Brazilian food', 'Brasileira')
restaurant_mexican = Restaurant('Mexican food', 'Mexican')
restaurant_mexican.change_state()
restaurant_american = Restaurant('American food', 'American')


restaurant_brasil.add_new_rate('Darius', random.randint(1, 5))
restaurant_brasil.add_new_rate('Riven', random.randint(1, 5))
restaurant_brasil.add_new_rate('Urgot', random.randint(1, 5))

restaurant_mexican.add_new_rate('Darius', random.randint(1, 5))
restaurant_mexican.add_new_rate('Riven', random.randint(1, 5))
restaurant_mexican.add_new_rate('Urgot', random.randint(1, 5))


restaurant_american.add_new_rate('Darius', random.randint(1, 5))
restaurant_american.add_new_rate('Riven', random.randint(1, 5))
restaurant_american.add_new_rate('Urgot', random.randint(1, 5))

def main():
    '''
    Constutor da classe.
    '''
    Restaurant.list()

if __name__== '__main__':
    main()
    