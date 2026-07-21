from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str,
) -> None:
    # 1. Creating customer objects
    customer_objects = [Customer(c["name"], c["food"]) for c in customers]

    # 2. Creating staff objects
    cleaner_obj = Cleaner(cleaner)
    hall_obj = CinemaHall(hall_number)

    # 3. Selling food to each customer
    for customer in customer_objects:
        CinemaBar.sell_product(customer.food, customer)

    # 4. Conducting the movie session
    hall_obj.movie_session(movie, customer_objects, cleaner_obj)
