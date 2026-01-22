from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_object = [Customer(name=c["name"],
                                food=c["food"])
                       for c in customers]
    cinema_bar = CinemaBar()
    for customer in customer_object:
        cinema_bar.sell_product(product=customer.food, customer=customer)

    cinema_hall = CinemaHall(number=hall_number)

    cleaner_obj = Cleaner(name=cleaner)

    cinema_hall.movie_session(
        movie_name=movie, customers=customer_object, cleaning_staff=cleaner_obj
    )
