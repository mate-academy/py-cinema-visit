from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_list = []
    for customer in customers:
        current_customer = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(current_customer.food, current_customer)
        customers_list.append(current_customer)
    cleaning_staff = Cleaner(cleaner)
    current_hall = CinemaHall(hall_number)
    current_hall.movie_session(movie, customers_list, cleaning_staff)
