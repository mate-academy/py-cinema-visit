from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    bar = CinemaBar()
    hall = CinemaHall(hall_number)

    for customer in customers:
        customer.buy_ticket(movie)
        bar.sell_popcorn(customer)

    for customer in customers:
        hall.seat_customer(customer)

    hall.start_movie(movie)

    cleaner_obj = Cleaner(cleaner)
    cleaner_obj.clean_hall(hall_number)
