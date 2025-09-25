from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        movie: str,
        customers: list,
        hall_number: int,
        cleaner: str
) -> None:
    customers_on_movie = []
    for customer in customers:
        customers_on_movie.append(Customer(customer["name"], customer["food"]))
        that_customer = Customer(customer["name"], customer["food"])
        food = customer.get("food")
        CinemaBar.sell_product(customer=that_customer, product=food)
    cinema_cleaner = Cleaner(cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customers_on_movie,
        cleaning_staff=cinema_cleaner
    )
