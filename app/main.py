from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str,
                 movie: str) -> None:
    cinema_bar = CinemaBar()
    hall = CinemaHall(number=hall_number)
    cleaner = Cleaner(name=cleaner)
    customers_list = []
    for igors in customers:
        customer = Customer(igors["name"], igors["food"])
        customers_list.append(customer)
        cinema_bar.sell_product(customer.food, customer)
    hall.movie_session(movie, customers_list, cleaner)
