from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    customer_objs = []
    for customer in customers:
        c = Customer(name=customer["name"], food=customer["food"])
        customer_objs.append(c)
        CinemaBar.sell_product(product=c.food, customer=c)

    cl = Cleaner(name=cleaner)
    hall = CinemaHall(hall_number=hall_number)
    hall.movie_session(movie_name=movie, customers=customer_objs, cleaning_staff=cl)

if __name__ == "__main__":
    customers = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"}
    ]
    hall_number = 5
    cleaner_name = "Anna"
    movie = "Madagascar"

    cinema_visit(customers=customers, hall_number=hall_number, cleaner=cleaner_name, movie=movie)

