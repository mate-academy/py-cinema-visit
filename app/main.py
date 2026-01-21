from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_hall = CinemaHall(hall_number)
    clean = Cleaner(cleaner)
    guests = []

    for visitor in customers:
        visitor_instance = Customer(visitor["name"], visitor["food"])
        CinemaBar.sell_product(
            customer=visitor_instance,
            product=visitor_instance.food
        )
        guests.append(visitor_instance)

    cinema_hall.movie_session(movie, guests, clean)
