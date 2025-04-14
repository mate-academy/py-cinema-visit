from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    list_customers = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]
    for customer in list_customers:
        CinemaBar.sell_product(customer=customer,
                               product=customer.food)
    cinema_hall = CinemaHall(number=hall_number)
    cinema_hall.movie_session(movie_name=movie,
                              customers=list_customers,
                              cleaning_staff=Cleaner(name=cleaner))
