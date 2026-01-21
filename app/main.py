from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    cinema_customers = []
    cinema_hall = CinemaHall(number=hall_number)
    cinema_cleaner = Cleaner(name=cleaner)

    for customer in customers:
        cinema_customers.append(
            Customer(name=customer["name"],
                     food=customer["food"]))

    for cinema_customer in cinema_customers:
        CinemaBar.sell_product(product=cinema_customer.food,
                               customer=cinema_customer)

    cinema_hall.movie_session(movie_name=movie,
                              customers=cinema_customers,
                              cleaning_staff=cinema_cleaner)
