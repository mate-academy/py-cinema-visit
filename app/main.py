from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list[dict],
        hall_number: int,
        cleaning_staff: str,
        movie: str
) -> str:
    customer_instances = [
        Customer(customer["name"],
                 customer["food"]
                 ) for customer in customers]
    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    cleaner = Cleaner(cleaning_staff)

    for customer in customer_instances:
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie, customer_instances, cleaner)
