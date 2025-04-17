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
    customer_objects = []
    for c in customers:
        customer_obj = Customer(name=c['name'], food=c["food"])
        CinemaBar.sell_product(
            customer=customer_obj,
            product=customer_obj.food
        )
        customer_objects.append(customer_obj)

    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff
    )
