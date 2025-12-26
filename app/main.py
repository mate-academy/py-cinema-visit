from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    list_of_customers = []
    new_bar = CinemaBar()
    for customer in customers:
        list_of_customers.append(Customer(
            name=customer["name"],
            food=customer["food"]
        ))
    for instances in list_of_customers:
        new_bar.sell_product(product=instances.food,
                             customer=instances)
    hall = CinemaHall(number=hall_number)
    clean = Cleaner(name=cleaner)
    hall.movie_session(
        movie_name=movie,
        customers=list_of_customers,
        cleaning_staff=clean)
