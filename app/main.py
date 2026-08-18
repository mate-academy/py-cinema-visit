from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_fixed = []
    [
        customers_fixed.append(Customer(customer["name"], customer["food"]))
        for customer in customers
    ]
    for customer in customers_fixed:
        CinemaBar.sell_product(customer.name, customer.food)
    hall_module = CinemaHall(hall_number)
    staff_module = Cleaner(cleaner)
    hall_module.movie_session(movie, customers_fixed, staff_module)
