from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_list = []
    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        customers_list.append(customer)
        CinemaBar.sell_product(customer.food, customer)
    cinema_hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customers_list, cleaner_obj)
