from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    # создаём объекты
    customer_objs = [Customer(name=c["name"], food=c["food"]) for c in customers]
    bar = CinemaBar()
    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)

    # бар продаёт еду
    for customer in customer_objs:
        bar.sell_product(product=customer.food, customer=customer)

    # киносеанс
    hall.movie_session(movie_name=movie, customers=customer_objs, cleaning_staff=cleaner_obj)


if __name__ == "__main__":
    customers = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"}
    ]
    cinema_visit(customers=customers, hall_number=5, cleaner="Anna", movie="Madagascar")
