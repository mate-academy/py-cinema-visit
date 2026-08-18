from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    people = []

    for person in customers:
        people.append(Customer(person["name"], person["food"]))

    cb = CinemaBar()
    for person in people:
        cb.sell_product(customer=person, product=person.food)

    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    cinema_hall.movie_session(
        movie_name=movie, customers=people, cleaning_staff=cleaning_staff
    )
