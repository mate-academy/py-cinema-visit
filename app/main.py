from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list[dict[str, str]],
                 hall_number: int,
                 cleaner: str,
                 movie: str,
                 ) -> None:
    # створюємо список об’єктів Customer
    customer_objects = [
        Customer(name=c["name"], food=c["food"])
        for c in customers
    ]

    # створюємо об’єкт Cleaner
    cleaning_staff = Cleaner(name=cleaner)

    # бар продає їжу всім клієнтам
    for customer in customer_objects:
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer
        )

    # створюємо об’єкт CinemaHall
    hall = CinemaHall(number=hall_number)

    # запускаємо кіносеанс
    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff
    )
