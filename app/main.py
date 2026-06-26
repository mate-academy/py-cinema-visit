from app.cinema.bar import CinemaBar
from app.people.customer import Customer

from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customers_list = []

    for person in customers:
        product = person.get("food")
        customer = Customer(person.get("name"), product)
        CinemaBar.sell_product(customer, product)
        customers_list.append(customer)

    hall = CinemaHall(number=hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=Cleaner(name=cleaner)
    )
