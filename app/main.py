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
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    hall_cleaner = Cleaner(cleaner)
    customers_list = []
    for customer in customers:
        customer = Customer(name=customer["name"], food=customer["food"])
        customers_list.append(customer)
        cinema_bar.sell_product(customer.food, customer)
    cinema_hall.movie_session(movie, customers_list, hall_cleaner)
