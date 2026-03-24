from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    new_customers = []
    for customer in customers:
        new_customers.append(Customer(customer["name"], customer["food"]))
    for person in new_customers:
        CinemaBar.sell_product(person.food, person)
    hall_num = CinemaHall(hall_number)
    cln = Cleaner(cleaner)
    hall_num.movie_session(movie, new_customers, cln)
