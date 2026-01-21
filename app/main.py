from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_objects = []

    for customer_info in customers:
        customer = Customer(name=customer_info["name"],
                            food=customer_info["food"])
        customer_objects.append(customer)
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall = CinemaHall(hall_number)
    hall.movie_session(movie_name=movie, customers=customer_objects,
                       cleaning_staff=Cleaner(name=cleaner))
