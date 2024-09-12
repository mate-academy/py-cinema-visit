from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar


def cinema_visit(customers: list,
                 hall_number: int,
                 cleaning_staff: str,
                 movie_name: str) -> None:

    customer_list = [
        Customer(name=customer["name"],
                 food=customer["food"])
        for customer in customers]

    cinema_hall = CinemaHall(number=hall_number)
    cinema_bar = CinemaBar()

    for customer in customer_list:
        cinema_bar.sell_product(product=customer.food, customer=customer)

    cinema_hall.movie_session(movie_name=movie_name,
                              customers=customer_list,
                              cleaning_staff=Cleaner(name=cleaning_staff))
