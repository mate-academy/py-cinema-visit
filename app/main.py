from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_list = []
    for item in customers:
        customers_list.append(Customer(item["name"], item["food"]))
        CinemaBar.sell_product(customers_list[-1], customers_list[-1].food)

    cinema = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    cinema.movie_session(movie_name=movie,
                         customers=customers_list,
                         cleaning_staff=cleaner)
