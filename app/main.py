from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str,) -> None:
    cinema_hall = CinemaHall(hall_number)

    customers_instance_list = [Customer(person.get("name"), person.get("food"))
                               for person in customers]
    cleaner_person = Cleaner(cleaner)

    for person in customers_instance_list:
        CinemaBar.sell_product(person.food, person)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customers_instance_list,
        cleaning_staff=cleaner_person)
