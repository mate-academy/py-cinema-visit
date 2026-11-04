from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int,
                 cleaner: str, movie: str) -> None:
    customers_objects = []
    for customer in customers:
        customer_obj = Customer(name=customer["name"],
                                food=customer["food"])
        CinemaBar.sell_product(product=customer_obj.food,
                               customer=customer_obj)
        customers_objects.append(customer_obj)
    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)
    hall.movie_session(movie_name=movie,
                       customers=customers_objects,
                       cleaning_staff=cleaning_staff)
