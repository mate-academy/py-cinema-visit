from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, number: int,
                 cleaner: str, movie: str) -> None:
    customer_objects = []
    for customer in customers:
        name = customer["name"]
        food = customer["food"]
        customer_obj = Customer(name, food)
        CinemaBar.sell_product(product=customer_obj.food,
                               customer=customer_obj)
        customer_objects.append(customer_obj)
    hall = CinemaHall(number)
    cleaner_obj = Cleaner(cleaner)
    hall.movie_session(movie_name=movie,
                       customers=customer_objects, cleaning_staff=cleaner_obj)
