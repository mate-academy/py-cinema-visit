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
    customer_objects = []
    for customer in customers:
        name = customer["name"]
        food = customer["food"]
        new_customer = Customer(name, food)
        customer_objects.append(new_customer)

    cleaner_object = Cleaner(cleaner)
    hall_object = CinemaHall(hall_number)

    for customer_object in customer_objects:
        CinemaBar.sell_product(customer_object.food, customer_object)

    hall_object.movie_session(movie, customer_objects, cleaner_object)
