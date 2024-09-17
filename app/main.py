from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    list_of_customers = []
    for people in customers:
        client = Customer(people.get("name"), people.get("food"))
        CinemaBar.sell_product(client.food, client)
        list_of_customers.append(client)
    cinema_hall = CinemaHall(hall_number)
    clean_person = Cleaner(cleaner)
    cinema_hall.movie_session(movie, list_of_customers, clean_person)
