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
    cleaner_obj = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    customer_objs = []

    for customer in customers:
        customer_obj = Customer(customer["name"], customer["food"])
        cinema_bar.sell_product(
            product=customer_obj.food,
            customer=customer_obj
        )
        customer_objs.append(customer_obj)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objs,
        cleaning_staff=cleaner_obj
    )
