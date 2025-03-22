from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[Customer],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_list = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]
    cinema_bar = CinemaBar()
    for customer in customers_list:
        cinema_bar.sell_product(customer.food, customer)
    hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner)

    hall.movie_session(movie, customers_list, cinema_cleaner)
