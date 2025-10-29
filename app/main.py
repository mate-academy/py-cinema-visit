from typing import List, Dict

from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(
    customers: List[Dict[str, str]],
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    """
    Função que simula o fluxo completo de uma visita ao cinema:
    1. Venda de produtos no bar.
    2. Agendamento e execução da sessão de cinema.
    3. Limpeza do corredor após a sessão.
    """

    # Lista para armazenar instâncias de Customer
    customer_instances = []

    # 1. O bar do cinema vende comida aos clientes
    # Itera sobre os dados dos clientes
    for customer_data in customers:
        # Cria a instância do cliente
        customer = Customer(
            name=customer_data["name"],
            food=customer_data["food"]
        )
        # Vende o produto (usando o metodo estático)
        CinemaBar.sell_product(
            product=customer.food,
            customer=customer
        )
        # Armazena a instância para uso posterior na sessão de cinema
        customer_instances.append(customer)

    # 2. Agendamento e execução da sessão de cinema
    # Cria as instâncias necessárias
    hall = CinemaHall(hall_number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    # Inicia a sessão de cinema
    hall.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaning_staff
    )
