from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:

    cin_bar = CinemaBar()
    cin_hall = CinemaHall(hall_number)
    clean = Cleaner(cleaner)

    list_cust = []

    for customer in customers:
        cust = Customer(customer["name"], customer["food"])
        cin_bar.sell_product(customer=cust, product=cust.food)
        list_cust.append(cust)

    cin_hall.movie_session(movie, list_cust, clean)
