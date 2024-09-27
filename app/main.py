from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_list = []
    cinema_bar = CinemaBar()
    for customer in customers:
        customers_list.append(
            Customer(customer["name"],
                     customer["food"]
                     ))
        cinema_bar.sell_product(
            customer=customers_list[-1],
            product=customers_list[-1].food
        )
    cinema_cleaner = Cleaner(cleaner)
    visitors = CinemaHall(hall_number)
    visitors.movie_session(movie, customers_list, cinema_cleaner)


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
