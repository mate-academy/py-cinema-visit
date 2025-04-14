from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar as Bar
from app.cinema.hall import CinemaHall as Hall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers = [Customer(customer["name"], customer["food"])
                 for customer
                 in customers]
    hall = Hall(hall_number)
    cleaner = Cleaner(cleaner)
    for customer in customers:
        Bar.sell_product(customer.food, customer)
    hall.movie_session(movie, customers, cleaner)
