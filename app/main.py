from cinema import bar
from cinema import hall
from people import customer
from people import cinema_staff


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    customers_instances = [customer.Customer(name=c['name'], food=c['food']) for c in customers]
    cinema_hall_instance = hall.CinemaHall(number=hall_number)
    cleaner_instances = cinema_staff.Cleaner(name=cleaner)
    for i in customers_instances:
        bar.CinemaBar.sell_product(product=i.food, customer=i)
    hall.CinemaHall.movie_session(movie_name=movie, customers=customers_instances, cleaning_staff=cleaner)
    cinema_staff.Cleaner.clean_hall(hall_number)