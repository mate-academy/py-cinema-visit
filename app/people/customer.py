# app/people/customer.py

class Customer(object):
    def __init__(self, name, food):
        self.name = name
        self.food = food

    def watch_movie(self, movie):
        print('{} is watching "{}".'.format(self.name, movie))
