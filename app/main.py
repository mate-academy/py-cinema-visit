from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    visitors = []

    for customer in customers:
        visitor = Customer(name=customer["name"], food=customer["food"])
        visitors.append(visitor)
        CinemaBar.sell_product(product=visitor.food, customer=visitor)

    hall = CinemaHall(hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=visitors,
        clearing_staff=Cleaner(name=cleaner)
    )
