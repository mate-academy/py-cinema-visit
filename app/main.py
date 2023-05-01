from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str, movie: str
) -> None:
    customer_objs = [Customer(**customer) for customer in customers]
    cinema_bar = CinemaBar()
    for customer in customer_objs:
        cinema_bar.sell_product(product=customer.food, customer=customer)

    cinema_hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)
    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_objs,
        cleaning_staff=cleaner_obj
    )
