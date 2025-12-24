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
    cool_bar = CinemaBar()
    my_hall = CinemaHall(hall_number)
    my_cleaner = Cleaner(cleaner)
    my_customers = []
    for customer in customers:
        my_customers.append(Customer(customer["name"], customer["food"]))
    for customer in my_customers:
        cool_bar.sell_product(customer, customer.food)
    my_hall.movie_session(movie, my_customers, my_cleaner)
