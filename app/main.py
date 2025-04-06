from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

def cinema_visit(customers, hall_number, cleaner, movie):
    customer_instances = [Customer(name=c['name'], food=c['food']) for c in customers]
    cleaner_instance = Cleaner(name=cleaner)
    hall_instance = CinemaHall(hall_number)

    for customer in customer_instances:
        CinemaBar.sell_product(customer=customer, product=customer.food)

    hall_instance.movie_session(movie_name=movie, customers=customer_instances, cleaning_staff=cleaner_instance)

if __name__ == "__main__":
    customers = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"}
    ]
    hall_number = 5
    cleaner_name = "Anna"
    movie = "Madagascar"
    cinema_visit(customers=customers, hall_number=hall_number, cleaner=cleaner_name, movie=movie)