from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

def cinema_visit(customers, hall_number, cleaner, movie):
    # Створюємо екземпляри клієнтів
    customer_instances = [Customer(name=c["name"], food=c["food"]) for c in customers]

    # Продаємо їжу
    for customer in customer_instances:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    # Створюємо зал та прибиральника
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)

    # Запускаємо кіносесію
    hall.movie_session(movie_name=movie, customers=customer_instances, cleaning_staff=cleaning_staff)
