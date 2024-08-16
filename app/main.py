from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_hall = CinemaHall(number=hall_number)
    cinema_bar = CinemaBar()

    cleaner_instance = Cleaner(name=cleaner)
    customer_instances = []

    for customer in customers:
        new_customer = Customer(name=customer["name"], food=customer["food"])
        customer_instances.append(new_customer)
        cinema_bar.sell_product(new_customer.food, new_customer)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance,
    )
