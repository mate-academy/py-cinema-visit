from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str,
) -> tuple:
    customers = [
        Customer(customer["name"],
                 customer["food"]
                 ) for customer in customers]

    hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaning_staff = Cleaner(cleaner)
    for customer in customers:
        cinema_bar.sell_product(customer.food, customer)
    hall.movie_session(movie, customers, cleaning_staff)
    return hall, cinema_bar, cleaning_staff


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
        movie="Madagascar",
    )
