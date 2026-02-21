from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    movie: str, customers: list, hall_number: int, cleaner: str
) -> None:
    if isinstance(movie, list):
        movie, customers, hall_number, cleaner = (
            cleaner,
            movie,
            customers,
            hall_number,
        )
    customer_instances = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]

    for customer in customer_instances:
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer,
        )
    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)
    hall.movie_session(movie, customer_instances, cleaning_staff)
