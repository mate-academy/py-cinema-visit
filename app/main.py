from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_objects = []

    for person in customers:
        customer_obj = Customer(name=person["name"], food=person["food"])
        customer_objects.append(customer_obj)
        CinemaBar.sell_product(product=person["food"], customer=customer_obj)

    cleaning_staff = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff
    )
