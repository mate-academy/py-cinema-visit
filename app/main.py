# write your imports here
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> None:
    # write you code here
    
    # 1. Створення екземпляра Cleaner
    cleaner_instance = Cleaner(name=cleaner)
    
    # 2. Створення екземплярів Customer та продаж їжі через CinemaBar
    customer_instances = []
    for customer_data in customers:
        # Створення екземпляра Customer
        customer = Customer(name=customer_data["name"], 
                            food=customer_data["food"]) # Line split to fix E501 and quotes changed for Q000
        customer_instances.append(customer)
        
        # Продаж їжі (використовуємо статичний метод CinemaBar)
        CinemaBar.sell_product(product=customer.food, customer=customer)
        
    # 3. Створення екземпляра CinemaHall
    hall_instance = CinemaHall(hall_number=hall_number)
    
    # 4. Запуск кіносеансу
    hall_instance.movie_session(
        movie_name=movie, 
        customers=customer_instances, 
        cleaning_staff=cleaner_instance
    )
