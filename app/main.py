from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict[str, any]],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_of_cinema = [
        Customer(
            instance_of_class["name"],
            instance_of_class["food"]
        )
        for instance_of_class in customers
    ]
    for index, customer in enumerate(customers_of_cinema):
        cinema_bar = CinemaBar()
        cinema_bar.sell_product(
            customers[index]["food"], customer
        )
    cinema = CinemaHall(hall_number)
    staff = Cleaner(cleaner)
    cinema.movie_session(movie, customers_of_cinema, staff)
