from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    if not isinstance(customers, list):
        raise TypeError("customers should be a list")

    customer_objects = []

    # Продажа продуктов
    for c in customers:
        customer_instance = Customer(name=c["name"], food=c["food"])
        CinemaBar.sell_product(product=customer_instance.food, customer=customer_instance)
        print(f'Cinema bar sold {customer_instance.food} to {customer_instance.name}.')
        customer_objects.append(customer_instance)

    # Начало фильма
    print(f'"{movie}" started in hall number {hall_number}.')

    # Показываем, кто смотрит фильм
    for customer in customer_objects:
        print(f'{customer.name} is watching "{movie}".')

    # Завершение фильма
    print(f'"{movie}" ended.')

    # Уборка зала
    print(f'Cleaner {cleaner} is cleaning hall number {hall_number}.')

    # Вызываем метод movie_session
    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(cleaner)
    print("Calling movie_session...")  # Debug message
    hall.movie_session(movie_name=movie, customers=customer_objects, cleaning_staff=cleaning_staff)

    # После выполнения, если необходимо, добавьте вывод
    print("Movie session completed.")  # Debug message
