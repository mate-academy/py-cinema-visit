from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:

    current_hall = CinemaHall(hall_number)
    current_cleaner = Cleaner(cleaner)

    all_customers = [
        Customer(row_data["name"], row_data["food"])
        for row_data in customers
    ]
    for each_costumer in all_customers:
        CinemaBar.sell_product(each_costumer.food, each_costumer)

    current_hall.movie_session(movie, all_customers, current_cleaner)
