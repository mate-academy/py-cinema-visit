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
    new_list = []
    for customer in customers:
        customer_instance = Customer(name=customer["name"], food=customer["food"])
        new_list.append(customer_instance)
        CinemaBar.sell_product(
            product=customer["food"],
            customer=customer_instance
        )

    cleaner_instance = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)
    hall.movie_session(
        movie,
        new_list,
        cleaner_instance
    )
