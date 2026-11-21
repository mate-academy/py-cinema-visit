from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_objects = []
    for person in customers:
        new_customer = Customer(name=person["name"], food=person["food"])
        customer_objects.append(new_customer)
    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)
    hall = CinemaHall(number=hall_number)
    cleaning = Cleaner(name=cleaner)
    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning
    )
