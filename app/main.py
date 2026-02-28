from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customer_instances = [
        Customer(cust["name"], cust["food"])
        for cust in customers
    ]

    hall = CinemaHall(hall_number)
    cleaning_person = Cleaner(cleaner)

    for customer in customer_instances:
        CinemaBar.sell_product(customer.food, customer)

    hall.movie_session(movie, customer_instances, cleaning_person)
