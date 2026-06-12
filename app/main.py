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
    cleaning_staff = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)
    customers_list = []
    for customer in customers:
        cust = Customer(name=customer["name"], food=customer["food"])
        customers_list.append(cust)
        CinemaBar.sell_product(customer["food"], cust)
    hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaning_staff
    )
