from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    customers_list = [
        Customer(person["name"], person["food"])
        for person in customers]

    for customer in customers_list:
        CinemaBar.sell_product(customer, customer.food)

    movie_show = CinemaHall(hall_number)
    movie_show.movie_session(
        movie,
        customers_list,
        Cleaner(cleaner))
