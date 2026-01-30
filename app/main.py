# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    # Создаём экземпляры Customer
    customer_instances = [Customer(name=c["name"], food=c["food"]) for c in customers]

    # Продаём еду через CinemaBar (статический метод)
    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    # Создаём экземпляр Cleaner
    cleaner_instance = Cleaner(name=cleaner)

    # Создаём экземпляр CinemaHall
    hall_instance = CinemaHall(hall_number=hall_number)

    # Запускаем сеанс
    hall_instance.movie_session(movie_name=movie, customers=customer_instances, cleaning_staff=cleaner_instance)
