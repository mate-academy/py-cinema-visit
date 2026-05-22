from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customers_list = []
    for customer in customers:
        name = customer["name"]
        food = customer["food"]
        customers_list.append(Customer(name, food))

    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    for customer in customers_list:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    cinema_hall.movie_session(movie, customers_list, cleaner)
