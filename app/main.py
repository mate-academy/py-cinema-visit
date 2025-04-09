from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaning_staff: str,
        movie_name: str
) -> None:
    cinema_hall = CinemaHall(number=hall_number)
    cinema_bar = CinemaBar()
    cleaner_name = Cleaner(name=cleaning_staff)

    visitors = []
    for customer in customers:
        person = Customer(customer["name"], customer["food"])
        visitors.append(person)
        cinema_bar.sell_product(customer=person, product=person.food)

    cinema_hall.movie_session(movie_name, visitors, cleaner_name)
