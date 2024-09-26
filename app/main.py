from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_ = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    cleaner_ = Cleaner(cleaner)

    for customer in customers_:
        CinemaBar.sell_product(customer, customer.food)

    cinema_hall.movie_session(movie, customers_, cleaner_)
