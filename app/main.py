from __future__ import annotations
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str, movie: str
) -> None:

    list_of_customers = []
    for person_data in customers:
        name = person_data["name"]
        food = person_data["food"]
        person = Customer(name=name, food=food)
        list_of_customers.append(person)
        CinemaBar.sell_product(product=person.food, customer=person)

    cinema_hall = CinemaHall(number=hall_number)
    current_cleaner = Cleaner(name=cleaner)
    cinema_hall.movie_session(
        movie_name=movie,
        customers=list_of_customers,
        cleaning_staff=current_cleaner
    )
