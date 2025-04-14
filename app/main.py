from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:

    real_customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)

    for customer in real_customers:
        cinema_bar.sell_product(customer, customer.food)

    cinema_hall.movie_session(
        movie,
        real_customers,
        cleaner
    )


if __name__ == "__main__":
    customers = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"}
    ]
    hall_number = 5
    cleaner_name = "Anna"
    movie = "Madagascar"
    cinema_visit(
        customers=customers,
        hall_number=5,
        cleaner="Anna",
        movie="Madagascar"
    )
