from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    # write you code here
    customers_list = []
    cinemabar = CinemaBar()
    for customer in customers:
        customer = Customer(name=customer["name"], food=customer["food"])
        customers_list.append(customer)
        cinemabar.sell_product(customer=customer, product=customer.food)

    cinemahall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    cinemahall.movie_session(
        customers=customers_list,
        cleaning_staff=cleaner,
        movie_name=movie
    )
