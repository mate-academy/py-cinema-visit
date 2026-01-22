from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict], hall_number: int, cleaner: str,
                 movie: str) -> None:

    cleaner_instance = Cleaner(cleaner)

    hall = CinemaHall(hall_number)

    for customer_date in customers:
        customer = Customer(name=customer_date["name"], food=customer_date
                            ["food"])
        CinemaBar.sell_product(product=customer.food, customer=customer)

    movie_customers = [Customer(name=customer["name"], food=customer["food"])
                       for customer in customers]
    hall.movie_session(movie_name=movie,
                       customers=movie_customers,
                       cleaning_staff=cleaner_instance)
