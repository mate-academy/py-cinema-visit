from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, number: int, cleaner: str,
                 movie: str) -> None:
    customers_class = [Customer(name=customer["name"], food=customer["food"])
                       for customer in customers]

    for customer in customers_class:
        CinemaBar.sell_product(customer=customer,
                               product=customer.food)

    CinemaHall(number=number).movie_session(
        movie_name=movie,
        customers=customers_class,
        cleaning_staff=Cleaner(cleaner)
    )
