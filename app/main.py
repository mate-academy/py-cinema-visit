from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    customer_instances = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    new_cinema_hall = CinemaHall(hall_number)
    new_cinema_bar = CinemaBar()
    new_cleaner = Cleaner(cleaner)

    for customer in customer_instances:
        new_cinema_bar.sell_product(
            product=customer.food,
            customer=customer
        )

    new_cinema_hall.movie_session(
        movie,
        customer_instances,
        new_cleaner
    )
