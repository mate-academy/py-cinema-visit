from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    customers_objs = []
    clean = Cleaner(cleaner)

    for person in customers:
        customer = Customer(person["name"], person["food"])
        CinemaBar.sell_product(customer.food, customer)
        customers_objs.append(customer)

    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, customers_objs, clean)
