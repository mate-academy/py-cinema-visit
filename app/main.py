from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_list = []
    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        customers_list.append(new_customer)
        CinemaBar.sell_product(new_customer, new_customer.food)

    cinema = CinemaHall(number=hall_number)
    cinema.movie_session(movie, customers_list, Cleaner(cleaner))
