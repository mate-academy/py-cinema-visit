# app/cinema/bar.py

class CinemaBar(object):
    @staticmethod
    def sell_product(product, customer):
        print("Cinema bar sold {} to {}.".format(product, customer.name))
