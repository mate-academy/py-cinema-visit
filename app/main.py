from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(number=hall_number)
    cleaner_name = Cleaner(name=cleaner)
    for customer_inf in customers:
        customer = Customer(
            name=customer_inf["name"],
            food=customer_inf["food"])
        cinema_bar.sell_product(customer=customer, product=customer.food)
    cinema_hall.movie_session(
        movie_name=movie,
        customers=[Customer(**c) for c in customers],
        cleaning_staff=cleaner_name)
