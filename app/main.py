from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_instances = []
    for customer in customers:
        customer_instance = Customer(customer["name"], customer["food"])
        customers_instances.append(customer_instance)
        CinemaBar.sell_product(product=customer["food"], customer=customer_instance)
    cinema_hall_instance = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)
    cinema_hall_instance.movie_session(movie_name=movie, customers=customers_instances, cleaning_staff=cleaner_instance)
