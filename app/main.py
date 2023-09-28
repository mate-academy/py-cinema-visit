from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customers_list = []

    for customer in customers:
        customers_list.append(Customer(name=customer["name"],
                                       food=customer["food"]))

    for customer in customers_list:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    clean = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)

    cinema_hall.movie_session(movie, customers_list, clean)
