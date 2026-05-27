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
    # Створюємо екземпляри Customer
    customer_objects = []
    for cust in customers:
        customer_obj = Customer(
            name=cust["name"],
            food=cust["food"]
        )
        customer_objects.append(customer_obj)

    # Продаємо їжу
    for customer in customer_objects:
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer
        )

    # Запускаємо сеанс
    hall = CinemaHall(number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff
    )
