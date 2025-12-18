from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(movie: str, customers: list[dict], hall_number: int, cleaner: str) -> None:
    customer_instances = []
    
    # 1. Сначала бар продает еду
    for cust_data in customers:
        customer = Customer(cust_data["name"], cust_data["food"])
        customer_instances.append(customer)
        CinemaBar.sell_product(customer.food, customer)

    # 2. Создаем зал и уборщика
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    # 3. Запускаем сеанс
    hall.movie_session(movie, customer_instances, cleaning_staff)
