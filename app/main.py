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
    hall = CinemaHall(hall_number)
    movie_name = movie
    cleaning_staff = Cleaner(cleaner)
    customer_list = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    for customer in customer_list:
        CinemaBar.sell_product(customer.food, customer)
    hall.movie_session(movie_name, customer_list, cleaning_staff)
