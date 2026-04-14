from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str,
) -> None:
    custs = []
    for customer in customers:
        cust = Customer(name=customer["name"], food=customer["food"])
        custs.append(cust)
        CinemaBar.sell_product(product=cust.food, customer=cust)
    hall = CinemaHall(number=hall_number)
    clean = Cleaner(name=cleaner)
    hall.movie_session(movie, custs, clean)
