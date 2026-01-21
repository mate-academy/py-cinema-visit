from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_info = []
    cleaner_staff = Cleaner(cleaner)
    for customer in customers:
        cls_customer = Customer(customer.get("name"), customer.get("food"))
        CinemaBar.sell_product(customer.get("food"), cls_customer)
        customer_info.append(cls_customer)
    CinemaHall(hall_number).movie_session(
        movie,
        customer_info,
        cleaner_staff
    )
