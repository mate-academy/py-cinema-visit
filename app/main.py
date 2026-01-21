from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers, hall_number, cleaner, movie):

    customers = [Customer(person["name"], person["food"])
                 for person in customers]
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)

    for viewer in customers:
        cinema_bar.sell_product(customer=viewer, product=viewer.food)

    hall = CinemaHall(hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customers,
        cleaning_staff=cleaner)
