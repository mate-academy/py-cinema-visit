from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_objs = [Customer(**c) for c in customers]
    for cust in customer_objs:
        CinemaBar.sell_product(product=cust.food, customer=cust)
    cleaner_obj = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)
    hall.movie_session(movie_name=movie,
                       customers=customer_objs,
                       cleaning_staff=cleaner_obj)
