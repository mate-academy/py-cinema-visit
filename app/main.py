from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.cinema.bar import CinemaBar


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaner: str,
        movie_name: str
) -> None:
    customers_i = [Customer(name=customer["name"],
                            food=customer["food"])
                   for customer in customers]
    for customer in customers_i:
        CinemaBar.sell_product(customer.food, customer)
    cinema_hall = CinemaHall(hall_number)
    new_staff = Cleaner(cleaner)
    cinema_hall.movie_session(
        movie_name=movie_name,
        customers=customers_i,
        cleaning_staff=new_staff
    )
