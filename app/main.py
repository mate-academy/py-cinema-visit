# write your imports here
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    people = [
        Customer(
            name=person["name"],
            food=person["food"])
        for person in customers
    ]
    hall_in_cinema = CinemaHall(number=hall_number)
    staff = Cleaner(name=cleaner)
    for person in people:
        CinemaBar.sell_product(customer=person, product=person.food)
    hall_in_cinema.movie_session(
        movie_name=movie,
        customers=people,
        cleaning_staff=staff
    )
