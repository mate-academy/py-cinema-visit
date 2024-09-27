from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema_bar = CinemaBar()
    cleaner = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)
    visitors = [
        Customer(name=customer["name"],
                 food=customer["food"])
        for customer in customers
    ]
    for customer in visitors:
        cinema_bar.sell_product(customer=customer, product=customer.food)

    hall.movie_session(
        movie_name=movie, customers=visitors, cleaning_stuff=cleaner
    )
