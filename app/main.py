from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
        customers:
        list[dict],
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_objects = []
    for cust in customers:
        customer_obj = Customer(name=cust["name"], food=cust["food"])
        customer_objects.append(customer_obj)
        CinemaBar.sell_product(product=customer_obj.food,
                               customer=customer_obj)

    hall = CinemaHall(number=hall_number)
    cleaner_obj = Cleaner(name=cleaner)
    hall.movie_session(movie_name=movie,
                       customers=customer_objects,
                       cleaning_staff=cleaner_obj
                       )
