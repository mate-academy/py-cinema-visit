from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        movie: str,
        customers: list[dict],
        hall_number: int,
        cleaner: str
) -> None:
    if not isinstance(customers, list):
        (hall_number, cleaner, movie, customers) = (
            customers, hall_number, cleaner, movie
        )
    customer_objs = []
    for cust_dict in customers:
        cust = Customer(name=cust_dict["name"], food=cust_dict["food"])
        CinemaBar.sell_product(product=cust.food, customer=cust)
        customer_objs.append(cust)
    hall = CinemaHall(number=hall_number)
    cleaner_obj = Cleaner(name=cleaner)
    hall.movie_session(
        movie_name=movie,
        customers=customer_objs,
        cleaning_staff=cleaner_obj
    )
