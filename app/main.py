from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):

    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cinema_stuff = Cleaner(cleaner)
    cinema_customers = [
        Customer(each["name"], each["food"]) for each in customers
    ]

    for cust in cinema_customers:
        cinema_bar.sell_product(customer=cust, product=cust.food)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=cinema_customers,
        cleaning_staff=cinema_stuff,
    )
