from app.cinema.bar import CinemaBar, sell_product
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner

def cinema_visit(customers, hall_number, cleaner, movie):
    # 1) Створюємо об’єкти Customer
    customer_objs = [Customer(c["name"], c["food"]) for c in customers]

    # 2) Продаємо їжу через CinemaBar
    for cust in customer_objs:
        sell_product(customer=cust, product=cust.food)

    # 3) Підготовка залу і Cleaner
    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)

    # 4) Запуск сеансу та прибирання
    hall.movie_session(movie, customer_objs, cleaner_obj)
