from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:

    customers_list = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]

    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)

    for customer in customers:
        customer = Customer(food=customer["food"], name=customer["name"])
        CinemaBar.sell_product(product=customer.food, customer=customer)

    hall.movie_session(movie, customers_list, cleaner)
