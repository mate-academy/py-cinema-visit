from app.people.cinema_staff import Cleaner
from app.people.customer import Customer

from typing import List, Union


def convert_to_customers(data: List[Union[Customer, dict]]) -> List[Customer]:
    if isinstance(data[0], dict):
        customers_list = []
        for customer_data in data:
            customer = Customer(name=customer_data["name"]
                                , food=customer_data["food"])
            customers_list.append(customer)
        return customers_list
    return data


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: List[Customer],
            cleaning_staff: Cleaner
    ) -> None:

        print(f'"{movie_name}" started in hall number {self.number}.')

        customers_list = convert_to_customers(customers)

        for customer_data in customers_list:
            customer_data.watch_movie(movie=movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(hall_number=self.number)
