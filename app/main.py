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
    customer_objs = [
        Customer(name=c["name"], food=c["food"])
        for c in customers
    ]
    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)
    for cust in customer_objs:
        CinemaBar.sell_product(product=cust.food, customer=cust)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objs,
        cleaning_staff=cleaner_obj
    )
