# app/people/cinema_staff.py

class Cleaner(object):
    def __init__(self, name):
        self.name = name

    def clean_hall(self, hall_number):
        print("Cleaner {} is cleaning hall number {}.".format(
            self.name, hall_number))

