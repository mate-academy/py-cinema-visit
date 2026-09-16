from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    custs = []
    for customer in customers:
        custs.append(Customer(name=customer["name"], food=customer["food"]))

    for cust in custs:
        CinemaBar.sell_product(product=cust.food, customer=cust)

    hall = CinemaHall(hall_number)
    clean = Cleaner(cleaner)

    hall.movie_session(movie_name=movie, customers=custs, cleaning_staff=clean)
