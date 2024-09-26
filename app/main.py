# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str,
                 movie: str) -> None:
    # write you code here
    customer_instances = []
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner_instance = Cleaner(cleaner)
    for customer in customers:
        customer_instances.append(Customer(customer["name"], customer["food"]))

    for customer in customer_instances:
        cinema_bar.sell_product(customer.food, customer)
    cinema_hall.movie_session(movie, customer_instances, cleaner_instance)
