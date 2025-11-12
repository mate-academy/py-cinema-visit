from app.people.customer import Customer
from app.people.cinema_staff import  Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    customers_obj = []
    for data in customers:
        customer_instance = Customer(name=data["name"], food=data["food"])
        CinemaBar.sell_product(customer=customer_instance, product=customer_instance.food)
        customers_obj.append(customer_instance)
    hall = CinemaHall(hall_number=hall_number)
    cleaner_instance = Cleaner(name=cleaner)
    hall.movie_session(movie, customers_obj, cleaner_instance)



if __name__ == '__main__':
    customers = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"}
    ]
    hall_number = 5
    cleaner_name = "Anna"
    movie = "Madagascar"
    cinema_visit(customers=customers, hall_number=hall_number, cleaner=cleaner_name, movie=movie)
    # Cinema bar sold Coca-cola to Bob.
    # Cinema bar sold popcorn to Alex.
    # "Madagascar" started in hall number 5.
    # Bob is watching "Madagascar".
    # Alex is watching "Madagascar".
    # "Madagascar" ended.
    # Cleaner Anna is cleaning hall number 5.