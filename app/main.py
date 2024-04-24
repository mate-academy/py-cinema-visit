from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str, movie: str
) -> None:
    cinema_customers = [Customer(name=customer["name"], food=customer["food"])
                        for customer in customers]
    cinema_hall = CinemaHall(number=hall_number)
    cinema_bar = CinemaBar()
    cinema_cleaner = Cleaner(name=cleaner)

    for customer in cinema_customers:
        cinema_bar.sell_product(product=customer.food, customer=customer)

    cinema_hall.movie_session(
        movie_name=movie,
        customers=cinema_customers,
        cleaning_staff=cinema_cleaner
    )
