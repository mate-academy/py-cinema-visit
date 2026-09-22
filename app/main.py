
class Customer:
    def __init__(self, name, food):
        self.name = name
        self.food = food
    
    def watch_movie(self, movie):
        print(f'{self.name} is watching "{movie}".')
class Cleaner:
    def __init__(self, name):
        self.name = name
        
    def clean_hall(self, hall_number):
        print(f'Cleaner {self.name} is cleaning hall number {hall_number}.')
class CinemaBar:
    @staticmethod
    def sell_product(product, customer):
        print(f'Cinema bar sold {product} to {customer.name}.')
class CinemaHall:
    def __init__(self, number):
        self.number = number
    
    def movie_session(self, movie_name, customers, cleaning_staff):
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.number)


def cinema_visit(movie, customers, hall_number, cleaner):
    customer_instances = [Customer(name=c["name"], food=c["food"]) for c in customers]
    
    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)
    
    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)
    hall.movie_session(movie_name=movie, customers=customer_instances, cleaning_staff=cleaning_staff)
