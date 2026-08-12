from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    cus = []
    for customer in customers:
        customer = Customer(name=customer["name"], food=customer["food"])
        CinemaBar.sell_product(product=customer.food, customer=customer)
        cus.append(customer)

    hall = CinemaHall(number=hall_number)
    cleaner = Cleaner(name=cleaner)
    hall.movie_session(movie_name=movie, cleaning_staff=cleaner, customers=cus)
