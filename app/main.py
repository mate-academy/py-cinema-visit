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
    hall = CinemaHall(hall_number)
    cleaner_name = Cleaner(cleaner)
    cinema_bar = CinemaBar()
    customers = [Customer(customer["name"], customer["food"])
                 for customer in customers]

    [cinema_bar.sell_product(customer.food, customer)
     for customer in customers]
    hall.movie_session(movie, customers, cleaner_name)
