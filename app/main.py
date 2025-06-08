from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_list = [
        Customer(
            name=customer["name"],
            food=customer["food"]) for customer in customers]
    cinema_hall = CinemaHall(hall_number)
    cleaner_name = Cleaner(cleaner)
    for customer in customers_list:
        CinemaBar.sell_product(customer.food, customer)
    CinemaHall.movie_session(cinema_hall, movie, customers_list, cleaner_name)
    return
