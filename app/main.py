from app.bar import CinemaBar
from app.hall import CinemaHall
from people.customer import Customer
from people.cinema_staff import Cleaner


def cinema_visit(movie: str, customers: list[dict], hall_number: int, cleaner: str) -> None:
    cinema_hall = CinemaHall(hall_number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    customer_objects = []

    for customer_data in customers:
        customer = Customer(
            name=customer_data["name"],
            food=customer_data["food"],
        )
        customer_objects.append(customer)
        CinemaBar.sell_product(product=customer.food, customer=customer)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff,
    )
