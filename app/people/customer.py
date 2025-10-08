class Customer(object):
    def __init__(self, name):
        self.name = name

    def watch_movie(self, movie):
        return "{} is watching {}.".format(self.name, movie)
