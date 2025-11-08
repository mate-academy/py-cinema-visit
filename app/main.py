from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    create_customer = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    for customer in create_customer:
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall = CinemaHall(hall_number)

    cleaner_name = Cleaner(cleaner)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=create_customer,
        cleaning_staff=cleaner_name
    )
