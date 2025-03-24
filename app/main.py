from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    list_visitor = []
    cinema_bar = CinemaBar()
    cimena_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    for customer in customers:
        visitor = Customer(customer.get("name"), customer.get("food"))
        list_visitor.append(visitor)
        cinema_bar.sell_product(customer=visitor, product=visitor.food)

    cimena_hall.movie_session(
        movie_name=movie,
        customers=list_visitor,
        cleaning_staff=cleaner
    )
