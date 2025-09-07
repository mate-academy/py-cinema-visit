from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_objs = []
    for customer in customers:
        customer_objs.append(Customer(name=customer["name"],
                                      food=customer["food"]))

    for customer in customer_objs:
        CinemaBar.sell_product(customer.food, customer)

    cinema_hall_obj = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)
    cinema_hall_obj.movie_session(movie, customer_objs, cleaner_obj)
