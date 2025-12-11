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
    customers = [
        Customer(name=cust["name"], food=cust["food"])
        for cust in customers
    ]

    hall = CinemaHall(hall_number)
    cleaner1 = Cleaner(cleaner)
    movie_name = movie
    for customer in customers:
        CinemaBar.sell_product(customer.food, customer)
    hall.movie_session(movie_name, customers, cleaner1)
