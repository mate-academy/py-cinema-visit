# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    # створюємо об'єкти Customer
    customer_objects = [
        Customer(name=c["name"], food=c["food"])
        for c in customers
    ]

    # продаємо продукти через CinemaBar (без створення екземпляра)
    for customer in customer_objects:
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer
        )

    # створюємо Cleaner
    cleaning_staff = Cleaner(name=cleaner)

    # створюємо CinemaHall і запускаємо сеанс
    hall = CinemaHall(hall_number=hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff
