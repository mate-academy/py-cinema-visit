from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    guests = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    current_hall = CinemaHall(hall_number)
    current_cleaner = Cleaner(cleaner)

    for guest in guests:
        CinemaBar.sell_product(guest.food, guest)

    current_hall.movie_session(movie, guests, current_cleaner)
