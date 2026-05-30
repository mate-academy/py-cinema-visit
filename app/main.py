from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    real_customers = []
    for customer in customers:
        a_real_customer = Customer(customer["name"], customer["food"])
        real_customers.append(a_real_customer)
    cinema_hall = CinemaHall(hall_number)
    the_cleaner = Cleaner(cleaner)
    for i in real_customers:
        CinemaBar.sell_product(customer=i, product=i.food)
    cinema_hall.movie_session(movie, real_customers, the_cleaner)
