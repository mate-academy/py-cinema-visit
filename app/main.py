# write your imports here
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    customer_objects = [Customer
                        (name=client["name"], food=client["food"])
                        for client in customers]

    hall_instance = CinemaHall(number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)

    for person in customer_objects:
        CinemaBar.sell_product(customer=person, product=person.food)

    hall_instance.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_instance)
