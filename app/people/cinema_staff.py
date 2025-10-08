class Cleaner(object):
    def __init__(self, name):
        self.name = name

    def clean(self, hall_number):
        return "{} is cleaning hall {}".format(self.name, hall_number)
