from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict[str, str]],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_instances = [Customer(name=c["name"], food=c["food"])
                          for c in customers]
    cleaner_instance = Cleaner(name=cleaner)
    hall_instance = CinemaHall(number=hall_number)

    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food,
                               customer=customer)

    hall_instance.movie_session(movie_name=movie, customers=customer_instances,
                                cleaning_staff=cleaner_instance)
