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
    object_customers = []
    for person in customers:
        cust = Customer(name=person["name"], food=person["food"])
        CinemaBar.sell_product(customer=cust, product=cust.food)
        object_customers.append(cust)
    clean = Cleaner(name=cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(
        movie_name=movie,
        customer=object_customers,
        cleaning_staff=clean
    )
