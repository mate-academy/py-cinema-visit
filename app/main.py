from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: Cleaner,
        movie: str
) -> None:
    customer_instances = [
        Customer(name=c["name"],
                 food=c["food"]
                 ) for c in customers
    ]
    cleaner_instance = Cleaner(name=cleaner)
    cinema_hall = CinemaHall(number=hall_number)
    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)
    cinema_hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
