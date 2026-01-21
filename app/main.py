from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    visitors = list([Customer(customer["name"],
                              customer["food"]) for customer in customers])
    for visitor in visitors:
        CinemaBar.sell_product(visitor.food, visitor)
    cinema_hall.movie_session(movie, visitors, cleaner)


if __name__ == "__main__":
    customers = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"}
    ]
    hall_number = 5
    cleaner_name = "Anna"
    movie = "Madagascar"
    cinema_visit(customers=customers, hall_number=hall_number,
                 cleaner=cleaner_name, movie=movie)
