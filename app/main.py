from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_list = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    for person in customers_list:
        CinemaBar.sell_product(person.food, person)

    hall = CinemaHall(hall_number)

    cleaner_personal = Cleaner(cleaner)

    hall.movie_session(movie, customers_list, cleaner_personal)
