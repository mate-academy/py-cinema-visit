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
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    customers_list = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    sell_product = CinemaBar.sell_product
    for customer in customers_list:
        sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, customers_list, cleaning_staff)
