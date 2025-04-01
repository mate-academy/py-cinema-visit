from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)
    customers_objs = []
    for person in customers:
        customer_obj = Customer(
            person["name"],
            person["food"]
        )
        customers_objs.append(customer_obj)
        cinema_bar.sell_product(
            product=person["food"],
            customer=customer_obj)
    hall.movie_session(
        movie_name=movie,
        customers=customers_objs,
        cleaning_staff=cleaner_obj
    )
