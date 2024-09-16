from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: Customer, hall_number: int,
                 cleaner: Cleaner, movie: str) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)

    for customer_data in customers:
        customer = Customer(customer_data["name"], customer_data["food"])
        cinema_bar.sell_product(customer, customer.food)

    cinema_hall.movie_session(
        movie,
        [Customer(client["name"], client["food"]) for client in customers],
        cleaner_instance
    )
