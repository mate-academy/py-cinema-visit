from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list, hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_list = [
        Customer(
            person["name"],
            person["food"]
        )
        for person in customers
    ]
    cleaner_person = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)

    for person in customers_list:
        CinemaBar.sell_product(person, person.food)

    cinema_hall.movie_session(movie, customers_list, cleaner_person)
