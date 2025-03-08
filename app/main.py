from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_cinema_hall = []
    cd = CinemaBar()
    for customer in customers:
        customer = Customer(customer["name"], customer["food"])
        cd.sell_product(customer, customer.food)
        customers_cinema_hall.append(customer)
    cleaning = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, customers_cinema_hall, cleaning)
