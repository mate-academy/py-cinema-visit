from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str)\
        -> None:
    objects_customer = [Customer(name=custom["name"], food=custom["food"])
                        for custom in customers]

    objects_hall = CinemaHall(number=hall_number)

    objects_clean = Cleaner(name=cleaner)

    for customer in objects_customer:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    objects_hall.movie_session(
        movie_name=movie,
        customers=objects_customer,
        cleaning_staff=objects_clean
    )
