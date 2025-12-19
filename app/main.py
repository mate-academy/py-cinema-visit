from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    new_customers = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]
    for client in new_customers:
        CinemaBar.sell_product(product=client.food, customer=client)
    cinema_hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    cinema_hall.movie_session(
        movie_name=movie,
        customers=new_customers,
        cleaning_staff=cleaning_staff
    )
