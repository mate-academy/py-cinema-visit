from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner_man = Cleaner(cleaner)

    customers_list = []
    for customer in customers:
        client = Customer(customer["name"], customer["food"])
        cinema_bar.sell_product(client.food, client)
        customers_list.append(client)

    cinema_hall.movie_session(movie, customers_list, cleaner_man)
