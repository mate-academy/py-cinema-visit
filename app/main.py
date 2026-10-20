from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    new_customers = []
    for customer_data in customers:
        customer = Customer(
            name=customer_data["name"],
            food=customer_data["food"]
        )
        new_customers.append(customer)
        CinemaBar.sell_product(customer.food, customer)
    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(name=cleaner)
    hall.movie_session(movie, new_customers, cleaner_obj)
