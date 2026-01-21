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
    customers_instances = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]
    cleaning_staff = Cleaner(cleaner)
    for customer in customers_instances:
        CinemaBar.sell_product(customer=customer, product=customer.food)
    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(
        customers=customers_instances,
        cleaning_staff=cleaning_staff,
        movie_name=movie
    )
