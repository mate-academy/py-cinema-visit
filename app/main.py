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
    Customer.customers = []
    for customer in customers:
        Customer.name = customer["name"]
        Customer.food = customer["food"]
        Customer.customers.append(
            Customer(name=customer["name"], food=customer["food"])
        )

    for person in Customer.customers:
        CinemaBar.sell_product(person, person.food)

    CinemaHall.movie_session(
        CinemaHall(hall_number), movie, Customer.customers, Cleaner(cleaner)
    )
