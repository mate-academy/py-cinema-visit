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
    customers_list = [
        Customer(customer["name"],
                 customer["food"])
        for customer in customers
    ]
    hall_number = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    for customer in customers_list:
        CinemaBar.sell_product(customer.food, customer)
    hall_number.movie_session(movie, customers_list, cleaner)
