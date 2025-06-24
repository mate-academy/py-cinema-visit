from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers_in_cinema = [
        Customer(name=cust["name"],
                 food=cust["food"])
        for cust in customers
    ]
    for customer in customers_in_cinema:
        CinemaBar.sell_product(product=customer.food, customer=customer)
    hall = CinemaHall(number=hall_number)
    staff = Cleaner(name=cleaner)
    hall.movie_session(movie_name=movie,
                       customers=customers_in_cinema,
                       cleaning_staff=staff)
