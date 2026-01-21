from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[Customer],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_list = []
    for customer in customers:
        person = Customer(customer["name"], customer["food"])
        customers_list.append(person)
        CinemaBar.sell_product(person, person.food)
    new_hall_number = CinemaHall(hall_number)
    new_cleaner = Cleaner(cleaner)
    new_hall_number.movie_session(movie, customers_list, new_cleaner)
