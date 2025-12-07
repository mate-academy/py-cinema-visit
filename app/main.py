from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

def cinema_visit(
    customers: list[dict],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:

    # Створюємо екземпляри Customer
    customer_objects = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]

    # Продаємо продукти через CinemaBar (статичний метод)
    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    # Створюємо екземпляр CinemaHall
    hall = CinemaHall(hall_number)

    # Створюємо екземпляр Cleaner
    cleaning_staff = Cleaner(cleaner)

    # Запускаємо сесію перегляду фільму
    hall.movie_session(movie_name=movie, customers=customer_objects, cleaning_staff=cleaning_staff)
