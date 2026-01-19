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
    customers_objs = []
    for i in customers:
        customer_obj = Customer(name=i["name"], food=i["food"])
        CinemaBar.sell_product(
            product=customer_obj.food,
            customer=customer_obj)
        customers_objs.append(customer_obj)
    hall = CinemaHall(number=hall_number)
    cleaner_obj = Cleaner(name=cleaner)
    hall.movie_session(
        movie_name=movie,
        customers=customers_objs,
        cleaning_staff=cleaner_obj
    )
