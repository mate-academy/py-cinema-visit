from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list, hall_number: int, cleaner_name: str, movie_name: str
) -> None:
    cb = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner_name)

    for customer_data in customers:
        customer = Customer(
            name=customer_data["name"], food=customer_data["food"]
        )
        cb.sell_product(customer, customer.food)

    hall.movie_session(movie_name, [
        Customer(
            name=customer["name"],
            food=customer["food"]
        ) for customer in customers
    ], cleaner)
