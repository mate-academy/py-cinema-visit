from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    list_of_customers = [Customer(name=customer["name"], food=customer["food"])
                         for customer in customers]

    cinema_bar = CinemaBar()

    for customer in list_of_customers:
        cinema_bar.sell_product(product=customer.food, customer=customer)

    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    CinemaHall.movie_session(hall,
                             movie_name=movie,
                             customers=list_of_customers,
                             cleaning_staff=cleaner)
