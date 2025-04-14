from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:

    cinema_hall = CinemaHall(hall_number)
    cleaner_person = Cleaner(cleaner)
    people = [
        Customer(name=person["name"], food=person["food"])
        for person in customers
    ]

    for person in people:
        CinemaBar.sell_product(customer=person, product=person.food)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=people,
        cleaning_staff=cleaner_person
    )
