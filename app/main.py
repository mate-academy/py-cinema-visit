from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:

    costomers_list = []
    for customer in customers:
        costomers_list.append(Customer(customer["name"], customer["food"]))

    hall = CinemaHall(hall_number)
    bar_cinema = CinemaBar()
    clean = Cleaner(cleaner)

    for client in costomers_list:
        bar_cinema.sell_product(product=client.food, customer=client)

    hall.movie_session(movie_name=movie,
                       customers=costomers_list,
                       cleaning_staff=clean)
