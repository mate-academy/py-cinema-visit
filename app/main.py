from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[Customer],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_bar = CinemaBar()
    clean = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    customer_list = []
    for one_customer in customers:
        customer = Customer(one_customer["name"], one_customer["food"])
        customer_list.append(customer)
        cinema_bar.sell_product(customer=customer, product=customer.food)
    hall.movie_session(movie, customer_list, clean)
