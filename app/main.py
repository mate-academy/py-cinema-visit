from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:

    customer_instances = [Customer(customer["name"],
                          customer["food"]) for customer in customers]

    cinema_bar = CinemaBar()
    for customer in customer_instances:
        cinema_bar.sell_product(customer, customer.food)

    cinema_hall = CinemaHall(hall_number)
    clean_person = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customer_instances, clean_person)
