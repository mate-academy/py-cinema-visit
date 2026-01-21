from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_bar = CinemaBar()

    customer_objects = [
        Customer(name=client["name"],
                 food=client["food"])
        for client in customers
    ]

    for customer in customer_objects:
        cinema_bar.sell_product(customer=customer, product=customer.food)

    cinema_hall = CinemaHall(hall_number)

    cleaner_instance = Cleaner(cleaner)

    cinema_hall.movie_session(movie, customer_objects, cleaner_instance)
