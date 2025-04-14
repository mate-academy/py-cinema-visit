from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list[dict], hall_number: int, cleaner: str, movie: str
) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(number=hall_number)
    cleaner = Cleaner(name=cleaner)

    for customer_data in customers:
        customer = Customer(
            name=customer_data["name"], food=customer_data["food"]
        )
        cinema_bar.sell_product(customer=customer, product=customer.food)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=[Customer(**customer) for customer in customers],
        cleaning_staff=cleaner
    )
