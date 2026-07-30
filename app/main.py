from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    customer_list = []

    for customer in customers:
        person = Customer(customer["name"], customer["food"])
        customer_list.append(person)
        CinemaBar.sell_product(person.food, person)

    hall.movie_session(movie, customer_list, cleaning_staff)
