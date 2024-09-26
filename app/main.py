from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    list_of_customers = [Customer(customer["name"],
                                  customer["food"]) for customer in customers]
    person_cleaner = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)

    for one_of_customers in list_of_customers:
        CinemaBar.sell_product(one_of_customers, one_of_customers.food)

    cinema_hall.movie_session(movie, list_of_customers, person_cleaner)
