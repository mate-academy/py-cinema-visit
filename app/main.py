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
    customer_instances = []
    for customer in customers:
        new_cus = Customer(
            name=customer["name"],
            food=customer["food"]
        )
        CinemaBar.sell_product(new_cus.food, new_cus)
        customer_instances.append(new_cus)

    cleaner_instance = Cleaner(cleaner)
    hall_instance = CinemaHall(hall_number)
    hall_instance.movie_session(
        movie, customer_instances, cleaner_instance
    )
