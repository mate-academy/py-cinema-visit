from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    customers_list = [
        Customer(
            name=customer["name"],
            food=customer["food"]
        ) for customer in customers
    ]

    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    cinema_bar = CinemaBar()

    for customer in customers_list:
        cinema_bar.sell_product(product=customer.food, customer=customer)

    hall.movie_session(movie_name=movie,
                       customers=customers_list,
                       cleaning_staff=cleaner)
