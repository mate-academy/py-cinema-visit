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

    hall_num = CinemaHall(hall_number)
    bar_sneks = CinemaBar()
    cleaner_lady = Cleaner(cleaner)
    visitor = []
    for customer in customers:
        order = Customer(name=customer["name"], food=customer["food"])
        visitor.append(order)
        bar_sneks.sell_product(
            product=order.food,
            customer=order
        )

    hall_num.movie_session(
        movie_name=movie,
        customers=visitor,
        cleaning_staff=cleaner_lady
    )
