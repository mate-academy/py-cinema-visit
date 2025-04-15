from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaning_staff: str,
        movie_name: str
) -> None:
    persons = []
    for customer in customers:
        name = customer["name"]
        food = customer["food"]
        person = Customer(name, food)
        persons.append(person)

        CinemaBar.sell_product(food, person)
    staff = Cleaner(cleaning_staff)

    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie_name, persons, staff)
