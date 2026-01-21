class Customer:
    cust_name_food = []

    def __init__(self, name, food):
        self.name = name
        self.food = food

    def watch_movie(self, movie):
        print(f'{self.name} is watching "{movie}".')
