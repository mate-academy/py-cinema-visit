
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall



def cinema_visit(customers: list[dict],
                 hall_number: int,
                 cleaner_name: str,
                 movie: str):
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner_name)
    customers_obj = [Customer(name=customer["name"], food=customer["food"]) for customer in customers]
    for customer_obj in customers_obj:
        CinemaBar.sell_product(product=customer_obj.food, customer=customer_obj)

    hall.movie_session(movie, customers_obj, cleaner)



