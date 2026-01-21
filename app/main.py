from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_link: list = []
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    for i, customer in enumerate(customers):
        customers_link.append(Customer(customer["name"], customer["food"]))
        cinema_bar.sell_product(
            product=customer["food"],
            customer=customers_link[i]
        )

    cinema_hall.movie_session(movie, customers_link, cleaning_staff)
