from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:

    customers_obj = [
        Customer(person.get("name"), person.get("food"))
        for person in customers
    ]
    the_hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)

    # sell food.
    for obj in customers_obj:
        CinemaBar.sell_product(obj.food, obj)

    # movie session.
    the_hall.movie_session(movie, customers_obj, cleaner_obj)
