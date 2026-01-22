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

    list_of_customers = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]
    cinema_hall = CinemaHall(number=hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaner)

    for customer_instance in list_of_customers:
        cinema_bar.sell_product(
            product=customer_instance.food,
            customer=customer_instance
        )
    cinema_hall.movie_session(
        movie_name=movie,
        customers=list_of_customers,
        cleaning_staff=cleaner
    )
