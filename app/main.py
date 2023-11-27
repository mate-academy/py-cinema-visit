from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customers_list = []
    current_cleaner = Cleaner(cleaner)
    current_hall = CinemaHall(hall_number)

    for customer in customers:
        customers_list.append(Customer(name=customer["name"],
                                       food=customer["food"]))

    for customer in customers_list:
        CinemaBar.sell_product(product=customer.food, customer=customer)
    current_hall.movie_session(movie, customers_list, current_cleaner)
