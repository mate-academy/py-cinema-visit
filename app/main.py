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
    people = []
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    for person in customers:
        customer = Customer(person["name"], person["food"])
        people.append(customer)
        CinemaBar.sell_product(customer, customer.food)
    hall.movie_session(movie, people, cleaning_staff)
