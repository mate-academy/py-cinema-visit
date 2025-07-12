from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        movie: str,
        customers: list,
        hall_number: int,
        cleaner: str
) -> None:
    customers_obj = [
        Customer(name=c["name"], food=c["food"]) for c in customers
    ]
    cinema_hall_obj = CinemaHall(number=hall_number)
    cleaner_obj = Cleaner(name=cleaner)

    for customer_obj in customers_obj:
        CinemaBar.sell_product(
            customer=customer_obj,
            product=customer_obj.food
        )
    cinema_hall_obj.movie_session(
        movie_name=movie,
        customers=customers_obj,
        cleaning_staff=cleaner_obj
    )
