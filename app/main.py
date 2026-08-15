from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    class_customers = [Customer(name=customer.get("name"),
                                food=customer.get("food")
                                )
                       for customer in customers]

    clean_guy = Cleaner(name=cleaner)

    hall = CinemaHall(number=hall_number)

    for human in class_customers:
        CinemaBar.sell_product(product=human.food, customer=human)

    hall.movie_session(movie_name=movie,
                       customers=class_customers,
                       cleaning_staff=clean_guy)
