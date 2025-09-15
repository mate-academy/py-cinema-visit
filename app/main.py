from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list[dict], hall_number: int,
                 cleaner: str, movie: str) -> None:
    customer_objects = []
    # init in Customer
    for element in customers:
        name = element["name"]
        food = element["food"]
        customer_obj = Customer(name, food)
        customer_objects.append(customer_obj)
        CinemaBar.sell_product(product=food, customer=customer_obj)

    cleaner_obj = Cleaner(cleaner)

    hall_obj = CinemaHall(number=hall_number)
    hall_obj.movie_session(movie_name=movie, customers=customer_objects,
                           cleaning_staff=cleaner_obj)
