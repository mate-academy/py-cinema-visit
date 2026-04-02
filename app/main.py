from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    customer_objects = [Customer(customer["name"],
                                 customer["food"])
                        for customer in customers]
    for customer in customer_objects:
        CinemaBar.sell_product(customer.food, customer)

    hall.movie_session(movie, customer_objects, cleaner)


if __name__ == "__main__":
    customers = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"}
    ]
    cinema_visit(movie="Madagascar",
                 customers=customers,
                 hall_number=5,
                 cleaner="Anna")
