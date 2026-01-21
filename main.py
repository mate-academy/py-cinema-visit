from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str | Customer,
) -> None:
    customer_objects = []
    for person in customers:
        customer = Customer(name=person["name"], food=person["food"])
        customer_objects.append(customer)
        CinemaBar.sell_product(product=customer.food, customer=customer)
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff
    )
