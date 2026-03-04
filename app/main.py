from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    visitors = []
    for customer in customers:
        cust = Customer(customer["name"], customer["food"])
        visitors.append(cust)

    for visitor in visitors:
        CinemaBar.sell_product(product=visitor.food, customer=visitor)

    hall = CinemaHall(number=hall_number)

    cleaner_obj = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=visitors,
        cleaning_staff=cleaner_obj
    )
