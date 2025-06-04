from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner_name: str,
        movie: str
) -> None:
    cinema_hall = CinemaHall(hall_number)
    cinema_cleaner = Cleaner(cleaner_name)
    customer_info = [
        Customer(customer["name"],
                 customer["food"])
        for customer in customers]

    for client in customer_info:
        CinemaBar.sell_product(client.food, client)

    cinema_hall.movie_session(movie, customer_info, cinema_cleaner)
