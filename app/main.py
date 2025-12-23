from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    peoples_obj = [
        Customer(customer.get("name"), customer.get("food"))
        for customer in customers
    ]
    hall_obj = CinemaHall(hall_number)
    bar_obj = CinemaBar()
    cleaner_obj = Cleaner(cleaner)

    for people in peoples_obj:
        bar_obj.sell_product(people.food, people)

    hall_obj.movie_session(movie, peoples_obj, cleaner_obj)
