from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers = [
        Customer(customer['name'], customer['food']) for customer in customers
    ]
    cleaning_staff = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)

    for customer in customers:
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, customers, cleaning_staff)
