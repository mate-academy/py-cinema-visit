from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    total_list = [Customer(cut["name"], cut["food"]) for cut in customers]
    for client in customers:
        bar_cin = CinemaBar()
        bar_cin.sell_product(user=client["name"],
                             product=client["food"]
                             )
    human = CinemaHall(hall_number)
    clean_person = Cleaner(cleaner)
    human.movie_session(movie_name=movie, customers=total_list,
                        cleaning_staff=clean_person)
