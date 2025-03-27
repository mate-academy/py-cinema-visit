from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_list = []
    hall = CinemaHall(hall_number)
    cleaner_staff = Cleaner(cleaner)
    for person in customers:
        customer = Customer(person["name"], person["food"])
        customers_list.append(customer)
        CinemaBar.sell_product(customer, customer.food)
    hall.movie_session(movie, customers_list, cleaner_staff)
