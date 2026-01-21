from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    customers_array = [
        Customer(customer["name"],
                 customer["food"])
        for customer in customers
    ]
    hall_instance = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)
    [
        CinemaBar.sell_product(customer, customer.food)
        for customer in customers_array
    ]
    hall_instance.movie_session(movie, customers_array, cleaner_instance)
