from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers = [Customer(name=customer['name'], food=customer['food']) for customer in customers]
    cleaning_staff = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)

    for customer in customers:
        CinemaBar.sell_product(customer=customer, product=customer.food)

    hall.movie_session(movie_name=movie, customers=customers, cleaning_staff=cleaning_staff)
