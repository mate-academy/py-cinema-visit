from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:

    customer_objects = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]

    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall = CinemaHall(number=hall_number)
    hall.movie_session(movie_name=movie, customers=customer_objects,
                       cleaning_staff=Cleaner(name=cleaner))
