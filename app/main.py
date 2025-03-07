from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    result_list = []
    for element in customers:
        result_list.append(Customer(element["name"], element["food"]))
    cinema_bar = CinemaBar()
    for customer in result_list:
        cinema_bar.sell_product(customer.food, customer)
    hall = CinemaHall(hall_number)
    cl = Cleaner(cleaner)
    hall.movie_session(movie, result_list, cl)
