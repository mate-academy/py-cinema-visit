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
    cinema_bar = CinemaBar()
    hall_customers = [
        Customer(
            customer_data["name"],
            customer_data["food"]
        ) for customer_data in customers
    ]
    for customer in hall_customers:
        cinema_bar.sell_product(customer.food, customer)

    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    hall.movie_session(movie, hall_customers, cleaning_staff)
