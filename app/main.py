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
    clean_customers = []

    for customer in customers:
        instance = Customer(customer.get("name"), customer.get("food"))
        clean_customers.append(instance)

    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    for customer in clean_customers:
        CinemaBar.sell_product(product=customer.food, customer=customer)
    hall.movie_session(movie, clean_customers, cleaning_staff)
