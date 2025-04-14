from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list, hall_number: int, cleaner: Cleaner, movie: str
) -> None:
    customer_list = []
    for i in customers:
        customer = Customer(i["name"], i["food"])
        customer_list.append(customer)
    cleaner = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    for customer in customer_list:
        CinemaBar.sell_product(customer, customer.food)
    hall.movie_session(movie, customer_list, cleaner)
