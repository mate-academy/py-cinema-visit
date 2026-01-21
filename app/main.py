from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_objs = [Customer(d["name"], d["food"]) for d in customers]
    cinema_hall = CinemaHall(number=number)
    cleaner_instance = Cleaner(cleaner)
    for customer in customer_objs:
        CinemaBar.sell_product(customer.food, customer)
    cinema_hall.movie_session(
        customers=customer_objs,
        cleaning_staff=cleaner_instance,
        movie_name=movie,
    )
