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
    result = []
    for visiter in customers:
        customer = Customer(visiter["name"], visiter["food"])
        result.append(customer)
        CinemaBar.sell_product(customer=customer, product=customer.food)
    CinemaHall(hall_number).movie_session(movie, result, Cleaner(cleaner))
