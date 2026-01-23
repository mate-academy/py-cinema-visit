from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_list = list()
    for cust in customers:
        customer = Customer(cust["name"], cust["food"])
        customer_list.append(customer)
        CinemaBar.sell_product(customer.food, customer)
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    hall.movie_session(movie, customer_list, cleaner)
