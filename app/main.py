from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    movie_customers = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]
    movie_hall = CinemaHall(hall_number)
    movie_cleaner = Cleaner(cleaner)
    for movie_customer in movie_customers:
        CinemaBar.sell_product(movie_customer.food, movie_customer)
    movie_hall.movie_session(movie, movie_customers, movie_cleaner)
