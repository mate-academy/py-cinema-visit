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
    visitors = []

    for customer in customers:
        visitors.append(
            Customer(
                name=customer["name"],
                food=customer["food"]
            )
        )

    hall = CinemaHall(number=hall_number)
    cinema_bar = CinemaBar()
    cleaner_hall = Cleaner(name=cleaner)

    for visitor in visitors:
        cinema_bar.sell_product(
            product=visitor.food,
            customer=visitor
        )

    hall.movie_session(
        movie_name=movie,
        customers=visitors,
        cleaning_staff=cleaner_hall
    )
