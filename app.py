from Models.Restaurant import Restaurant


restaurant_brasil = Restaurant('Brazilian food', 'Brasileira')
restaurant_mexican = Restaurant('Mexican food', 'Mexican')
restaurant_mexican.change_state()
restaurant_american = Restaurant('American food', 'American')

def main():
    Restaurant.list()
    

if __name__== '__main__':
    main()