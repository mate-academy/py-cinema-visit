from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    customer_bar = [Customer(cus["name"], cus["food"])
                    for cus in customers]
    for customer in customer_bar:
        CinemaBar.sell_product(product=customer.food, customer=customer)
    number_hall = CinemaHall(hall_number)
    people_cleaner = Cleaner(cleaner)
    number_hall.movie_session(movie_name=movie,
                              customers=customer_bar,
                              cleaning_staff=people_cleaner)
