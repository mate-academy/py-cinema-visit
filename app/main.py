from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    hall_of_cinema = CinemaHall(hall_number)
    bar_of_cinema = CinemaBar()
    cleaning_staff = Cleaner(cleaner)
    customers_list = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    for customer in customers_list:
        bar_of_cinema.sell_product(customer.food, customer)

    hall_of_cinema.movie_session(movie, customers_list, cleaning_staff)
