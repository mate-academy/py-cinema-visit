from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list[dict], hall_number: int, cleaner: str, movie: str
) -> None:
    """Simulate a cinema visit: sell products, show movie, clean hall."""
    # Создаем объекты клиентов
    customer_objs = [
        Customer(name=c["name"], food=c["food"]) for c in customers
    ]

    # Продажа еды в баре
    for customer in customer_objs:
        CinemaBar.sell_product(
            product=customer.food, customer=customer
        )

    # Создаем кино-зал
    hall = CinemaHall(hall_number=hall_number)

    # Создаем уборщика
    cleaning_staff = Cleaner(name=cleaner)

    # Начинаем сеанс
    hall.movie_session(
        movie_name=movie,
        customers=customer_objs,
        cleaning_staff=cleaning_staff
    )
