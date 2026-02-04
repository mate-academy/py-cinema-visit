from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer  # Убедитесь, что пути импорта верны
from app.people.cinema_staff import Cleaner

def cinema_visit(
    movie: str,
    customers: list,
    hall_number: int,
    cleaner: str
) -> None:
    customer_objects = []
    for customer in customers:
        # Создаем экземпляр и добавляем в список
        c_obj = Customer(customer["name"], customer["food"])
        customer_objects.append(c_obj)
        # Вызываем статический метод бара
        CinemaBar.sell_product(customer["food"], c_obj)

    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_obj
    )