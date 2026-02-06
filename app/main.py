# write your imports here
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str) -> None:
    customer_objects = []
    for customer_data in customers:
        name = customer_data["name"]
        food = customer_data["food"]
        customer_objects.append(Customer(name=name, food=food))

    for customer in customer_objects:
        CinemaBar.sell_product(customer.food, customer)

    hall = CinemaHall(hall_number)
    cleaner1 = Cleaner(cleaner)
    hall.movie_session(movie, customer_objects, cleaner1)
