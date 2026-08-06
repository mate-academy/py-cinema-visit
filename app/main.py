from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    # write you code here
    customers_instances = []
    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        customers_instances.append(customer)
    for customer_instance in customers_instances:
        CinemaBar.sell_product(product=customer_instance.food, customer=customer_instance)
    cinema_hall = CinemaHall(hall_number)
    clean_hall = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customers_instances, clean_hall)
