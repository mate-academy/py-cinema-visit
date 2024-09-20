from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str, movie: str) -> None:

    customer_instances = [
        Customer(customer["name"],
                 customer["food"]) for customer in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)
    cinema_bar = CinemaBar()

    for customer in customer_instances:
        cinema_bar.sell_product(product=customer.food, customer=customer)

    cinema_hall.movie_session(
        movie_title=movie,
        customers=customer_instances,
        cleaner=cleaner_instance
    )
