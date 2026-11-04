from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    persons = [Customer(name=customer["name"],
                        food=customer["food"]) for customer in customers]

    for person in persons:
        CinemaBar.sell_product(product=person.food, customer=person)

    cleaner_instance = Cleaner(name=cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(movie_name=movie,
                       customers=persons,
                       cleaning_staff=cleaner_instance)
