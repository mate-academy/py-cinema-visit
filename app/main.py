from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    list_of_customers = []

    for customer in customers:
        list_of_customers.append(Customer(customer["name"], customer["food"]))

    bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    for person in list_of_customers:
        bar.sell_product(person.food, person)

    hall.movie_session(movie, list_of_customers, cleaner)
