from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    inst_customers: list[Customer]
    inst_customers = []
    for customer in customers:
        inst_customers.append(
            Customer(name=customer["name"],
                     food=customer["food"])
        )
    for customer in inst_customers:
        CinemaBar.sell_product(customer=customer, product=customer.food)
    CinemaHall(number=hall_number).movie_session(
        movie_name=movie,
        customers=inst_customers,
        cleaning_staff=Cleaner(cleaner))
