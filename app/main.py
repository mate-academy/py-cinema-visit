from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list[dict], hall_number: int, cleaner: str, movie: str
) -> None:
    customers_list = list()
    for customer in customers:
        customers_list.append(Customer(customer["name"], customer["food"]))
    visit_cleaner = Cleaner(cleaner)
    visit_hall = CinemaHall(hall_number)
    for customer in customers_list:
        CinemaBar.sell_product(customer.food, customer)
    visit_hall.movie_session(movie, customers_list, visit_cleaner)
