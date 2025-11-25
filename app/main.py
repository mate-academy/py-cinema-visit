from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    customers = [
        Customer(customer.get("name"), customer.get("food"))
        for customer in customers
    ]
    cleaner = Cleaner(name=cleaner)
    cinema_hall = CinemaHall(number=hall_number)
    sell_products = CinemaBar.sell_product

    for customer in customers:
        sell_products(customer=customer, product=customer.food)

    cinema_hall.movie_session(
        movie_name=movie, customers=customers, cleaning_staff=cleaner
    )
