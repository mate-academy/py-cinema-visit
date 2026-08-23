from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str
                 ) -> None:

    # Customer instance
    new_customer_list = []
    for customer in customers:
        customer_obj = Customer(name=customer["name"], food=customer["food"])
        new_customer_list.append(customer_obj)

    # CinemaHall instance
    hall_obj = CinemaHall(hall_number)

    # Cleaner instance
    cleaner_obj = Cleaner(cleaner)

    for customer in new_customer_list:
        CinemaBar.sell_product(customer.food, customer)

    hall_obj.movie_session(movie, new_customer_list, cleaner_obj)
