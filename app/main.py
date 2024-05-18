from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    list_customers = [Customer(person["name"],
                      person["food"]) for person in customers
                      ]
    hall_number = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    for customer in list_customers:
        CinemaBar.sell_product(customer, customer.food)
    hall_number.movie_session(movie, list_customers, cleaner)
