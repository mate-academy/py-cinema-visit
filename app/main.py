from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customer_obj = []
    for customer in customers:
        customer_object = Customer(name=customer["name"],
                                   food=customer["food"])
        customer_obj.append(customer_object)
        CinemaBar.sell_product(product=customer_object.food,
                               customer=customer_object)

    cleaner_obj = Cleaner(name=cleaner)
    hall = CinemaHall(number=hall_number)
    hall.movie_session(movie_name=movie,
                       customers=customer_obj, cleaning_staff=cleaner_obj)
