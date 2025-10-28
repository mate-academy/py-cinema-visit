from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    persons = []

    for customer in customers:
        persons.append(Customer(name=customer["name"], food=customer["food"]))

    for person in persons:
        CinemaBar.sell_product(product=person.food, customer=person)

    cleaning = Cleaner(name=cleaner)

    hall = CinemaHall(number=hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=persons,
        cleaning_staff=cleaning)
