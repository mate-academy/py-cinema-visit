from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from people.customer import Customer
from people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    customer_objects = []

    for data in customers:
        customer_objects.append(
            Customer(name=data["name"], food=data["food"])
        )

    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall = CinemaHall(hall_number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff
    )

