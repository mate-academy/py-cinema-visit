from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_list = []
    cb = CinemaBar()
    for customer in customers:
        name, food = customer["name"], customer["food"]
        person = Customer(name, food)
        customers_list.append(person)
        cb.sell_product(product=food, customer=person)

    cinema = CinemaHall(hall_number)
    cinema.movie_session(movie_name=movie,
                         customers=customers_list,
                         cleaning_staff=Cleaner(cleaner))
