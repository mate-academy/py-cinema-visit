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
    customer_list = []
    for customer in customers:
        customer_one = Customer(name=customer["name"], food=customer["food"])
        CinemaBar.sell_product(
            product=customer_one.food,
            customer=customer_one
        )
        customer_list.append(customer_one)
    hall = CinemaHall(hall_number)
    cleaner_one = Cleaner(cleaner)
    hall.movie_session(
        movie_name=movie,
        customers=customer_list,
        cleaning_staff=cleaner_one
    )
