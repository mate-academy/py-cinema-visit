from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner_name: str, movie: str) -> None:
    customer_instances = []
    for customer in customers:
        new_customer = Customer(name=customer["name"], food=customer["food"])
        customer_instances.append(new_customer)

    for customer in customer_instances:
        CinemaBar.sell_product(customer.food, customer)

    cleaner_instance = Cleaner(cleaner_name)
    hall_instance = CinemaHall(hall_number)

    hall_instance.movie_session(movie, customer_instances, cleaner_instance)
