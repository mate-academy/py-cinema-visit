from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list, hall_number: int, cleaning_staff: str, movie_name: str
) -> None:
    cinema_hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaning_staff)
    cinema_bar = CinemaBar()

    customers_list = []
    for customer in customers:
        customers_list.append(Customer(customer["name"], customer["food"]))

    for customer in customers_list:
        cinema_bar.sell_product(customer, customer.food)

    cinema_hall.movie_session(movie_name, customers_list, cleaning_staff)
