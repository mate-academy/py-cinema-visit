from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:

    customer_list = [
        Customer(name=client["name"], food=client["food"])
        for client in customers
    ]

    for client in customer_list:
        CinemaBar.sell_product(product=client.food, customer=client)

    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)

    hall.movie_session(movie, customer_list, cleaner_obj)
