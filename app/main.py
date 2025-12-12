from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_objects = [Customer(customer["name"], customer["food"]) for customer in customers]
    cinema_object = CinemaHall(hall_number)
    cleaner_object = Cleaner(cleaner)
    
    for customer in customers:
        CinemaBar.sell_product(customer=customer.name, product=customer.food)
    
    