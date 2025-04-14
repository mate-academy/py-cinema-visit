# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    # write you code here
    customers_person = []
    for customer in customers:
        customer_person = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(customer["food"], customer_person)
        customers_person.append(customer_person)
    hall = CinemaHall(hall_number)
    cleaner_person = Cleaner(cleaner)
    hall.movie_session(movie, customers_person, cleaner_person)
