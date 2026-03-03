from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_list = customers
    clean_staff = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)

    guest_list = []
    for guest in customers_list:
        guest_list.append(Customer(name=guest["name"], food=guest["food"]))
    for guest in guest_list:
        CinemaBar.sell_product(customer=guest, product=guest.food)

    hall.movie_session(
        movie_name=movie,
        customers=guest_list,
        cleaning_staff=clean_staff
    )
