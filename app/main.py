from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str, movie: str
) -> None:
    list_of_customers = [
        Customer(cust.get("name"), cust.get("food"))
        for cust in customers
    ]
    for per in list_of_customers:
        CinemaBar.sell_product(customer=per, product=per.food)

    CinemaHall(hall_number).movie_session(
        movie_name=movie,
        customers=list_of_customers,
        cleaning_staff=Cleaner(cleaner)
    )
