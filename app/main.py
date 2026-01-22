from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaning_staff: str,
        movie_name: str
) -> None:
    cb = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaning_staff)
    customers_list = []

    for cust in customers:
        customer = Customer(cust["name"], cust["food"])
        customers_list.append(customer)
        cb.sell_product(customer.food, customer)

    hall.movie_session(movie_name, customers_list, cleaner_instance)
