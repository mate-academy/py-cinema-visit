from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str,
                 movie: str) -> None:

    customer_instances = []
    for customer_data in customers:
        customer = Customer(name=customer_data["name"],
                            food=customer_data["food"])
        customer_instances.append(customer)

    cleaner_instance = Cleaner(cleaner)

    hall = CinemaHall(hall_number)

    for customer in customer_instances:
        CinemaBar.sell_product(customer.food, customer)
    hall.movie_session(movie, customer_instances, cleaner_instance)
