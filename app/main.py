from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
# from __future__ import annotations


def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaning_staff: str,
                 movie_name: str) -> None:

    cinema_bar = CinemaBar()

    customers_list = []

    # Ітеруємось по dict_customers. Створюємо екземпляри Customer.
    # продаємо їжу кожному відвідувачу
    # Створюємо список та записуємо екземпляри Customer в нього
    for customer_dict in customers:
        customer = Customer(name=customer_dict["name"],
                            food=customer_dict["food"])

        cinema_bar.sell_product(customer=customer, product=customer.food)
        customers_list.append(customer)

    cleaner = Cleaner(name=cleaning_staff)

    cinema_hall = CinemaHall(number=hall_number)

    # Проведення сеансу фільму в кінозалі
    cinema_hall.movie_session(movie_name=movie_name,
                              customers=customers_list,
                              cleaning_staff=cleaner)
