from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int, cleaner: str, movie: str) -> None:
    customer_objects = []
    for customer in customers:
        obj = Customer(customer["name"], customer["food"])
        customer_objects.append(obj)
        CinemaBar.sell_product(obj.food, obj)

    start_movie = CinemaHall(hall_number)
    cleaner_objects = Cleaner(cleaner)
    start_movie.movie_session(movie, customer_objects, cleaner_objects)


if __name__ == "__main__":
    customers = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"}
    ]
    cinema_visit(customers=customers,
                 hall_number=5, cleaner="Anna", movie="Madagascar")
