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
    customer_instances = [
        Customer(name=customer_dict["name"], food=customer_dict["food"])
        for customer_dict in customers
    ]
    for customer_instance in customer_instances:
        CinemaBar.sell_product(product=customer_instance.food,
                               customer=customer_instance)
    cleaner_man = Cleaner(cleaner)
    hall_instances = CinemaHall(number=hall_number)
    hall_instances.movie_session(movie_name=movie,
                                 customers=customer_instances,
                                 cleaning_staff=cleaner_man)
