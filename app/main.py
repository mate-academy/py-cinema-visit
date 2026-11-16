from app.cinema.bar import CinemaBar as CinemaBar
from app.cinema.hall import CinemaHall as CinemaHall
from app.people.cinema_staff import Cleaner as Cleaner
from app.people.customer import Customer as Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customers_list = []
    for customer in customers:
        customers_list.append(
            Customer(name=customer.get("name"), food=customer.get("food"))
        )

    hall = CinemaHall(number=hall_number)
    cleaner = Cleaner(name=cleaner)
    for customer in customers_list:
        CinemaBar.sell_product(customer=customer, product=customer.food)

    hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaner
    )
