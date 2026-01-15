from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    current_cleaner = Cleaner(cleaner)
    current_hall = CinemaHall(hall_number)
    customers_objs = []

    for el in customers:
        customer = Customer(name=el["name"], food=el["food"])
        customers_objs.append(customer)
        CinemaBar.sell_product(product=customer.food, customer=customer,)

    current_hall.movie_session(movie, customers_objs, current_cleaner)
