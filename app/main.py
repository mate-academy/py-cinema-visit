from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)
    movie_name = movie
    customer_objects = [Customer(name=customer["name"], food=customer["food"])
                        for customer in customers]
    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)
    hall.movie_session(movie_name=movie_name,
                       customers=customer_objects,
                       cleaning_staff=cleaning_staff)
