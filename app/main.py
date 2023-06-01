from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner: str,
                 movie: str) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(number=hall_number)
    customer_instance = [Customer(name=customer_data["name"],
                                  food=customer_data["food"])
                         for customer_data in customers]
    cleaner_instance = Cleaner(name=cleaner)

    for customer in customer_instance:
        cinema_bar.sell_product(product=customer.food, customer=customer)

    cinema_hall.movie_session(movie_name=movie,
                              customers=customer_instance,
                              cleaning_staff=cleaner_instance)
