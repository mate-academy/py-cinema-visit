from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        movie: str,
        customers: list,
        hall_number: int,
        cleaner: str,
) -> None:
    customer_obj = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    for customer in customer_obj:
        CinemaBar.sell_product(customer.food, customer)

    cleaner_obj = Cleaner(cleaner)

    hall = CinemaHall(hall_number)

    hall.movie_session(movie, customer_obj, cleaner_obj)
