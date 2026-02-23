from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        number: int,
        cleaner: str,
        movie: str) -> None:
    customers_object = [
        Customer(name=c["name"], food=c["food"]) for c in customers
    ]
    for customer_obj in customers_object:
        CinemaBar.sell_product(
            product=customer_obj.food,
            customer=customer_obj
        )
    hall = CinemaHall(number=number)
    cleaner_obj = Cleaner(name=cleaner)
    hall.movie_session(
        movie_name=movie,
        customers=customers_object,
        cleaning_staff=cleaner_obj
    )
