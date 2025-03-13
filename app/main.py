from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers = [Customer(person["name"], person["food"])
                 for person in customers]
    hall = CinemaHall(hall_number)
    bar = CinemaBar()
    cleaner = Cleaner(cleaner)

    for customer in customers:
        bar.sell_product(customer=customer, product=customer.food)

    hall.movie_session(movie_name=movie,
                       customers=customers,
                       cleaning_staff=cleaner)
