from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:

    cinema_bar = CinemaBar()

    guests_list = [
        Customer(
            customer.get("name"),
            customer.get("food")
        )
        for customer in customers
    ]

    for guest in guests_list:
        cinema_bar.sell_product(guest.food, guest)

    cinema_stuff = Cleaner(cleaner)

    hall = CinemaHall(hall_number)

    hall.movie_session(movie, guests_list, cinema_stuff)
