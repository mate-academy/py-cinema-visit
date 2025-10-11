from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list | Customer,
        hall_number: int | CinemaHall,
        cleaner: str | Cleaner,
        movie: str | Customer,
) -> None:
    customer_objects = []
    for person in customers:
        customer = Customer(name=person["name"], food=person["food"])
        customer_objects.append(customer)
        CinemaBar.sell_product(customer=customer, product=customer.food)
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff
    )
