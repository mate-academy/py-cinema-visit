from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict[str, str]],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema_hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)
    customer_list = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    for customer in customer_list:
        CinemaBar.sell_product(customer=customer, product=customer.food)
    cinema_hall.movie_session(movie_name=movie,
                              customers=customer_list,
                              cleaner=cinema_cleaner)
