from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: Cleaner, movie: str) -> None:
    customer_info = [Customer(name=cust["name"],
                              food=cust["food"]) for cust in customers]
    for customer in customer_info:
        CinemaBar.sell_product(customer=customer, product=customer.food)
    hall = CinemaHall(hall_number)
    cleaner_name = Cleaner(cleaner)
    hall.movie_session(movie_name=movie,
                       customers=customer_info,
                       cleaning_staff=cleaner_name)
