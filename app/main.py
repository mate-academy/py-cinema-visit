from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list[dict[str, str]], hall_number: int, cleaner: str, movie: str
) -> None:
    customer_objs: list[Customer] = [
        Customer(name=c["name"], food=c["food"]) for c in customers
    ]
    for customer in customer_objs:
        CinemaBar.sell_product(product=customer.food, customer=customer)
    hall: CinemaHall = CinemaHall(number=hall_number)
    cleaning_staff: Cleaner = Cleaner(name=cleaner)
    hall.movie_session(
        movie_name=movie, customers=customer_objs, cleaning_staff=cleaning_staff
    )
