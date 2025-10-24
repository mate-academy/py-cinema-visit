from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from typing import List, Dict


def cinema_visit(customers: List[Dict[str, str]],
                 hall_number: int, cleaner: str, movie: str) -> None:
    """
    Função que simula o fluxo completo de uma visita ao cinema:
    1. Venda de produtos no bar.
    2. Agendamento e execução da sessão de cinema.
    3. Limpeza do corredor após a sessão.
    """

    # Lista para armazenar instâncias de Customer
    customer_instances = []
    # 1. O bar do cinema vende comida aos clientes
    # (usando o metodo estático CinemaBar)
    # Itera sobre os dados dos clientes para criar as instâncias
    # e vender o produto
    for customer_data in customers:
        # Cria a instância de Customer
        customer_instance = Customer(name=customer_data["name"],
                                     food=customer_data["food"])

        # Usa o metodo estático sell_product.
        # O produto é o item 'food' desejado.
        CinemaBar.sell_product(product=customer_data["food"],
                               customer=customer_instance)

        # Armazena a instância para a próxima etapa (sessão de filme)
        customer_instances.append(customer_instance)

    # 2. Cria as instâncias de Cleaner e CinemaHall
    cleaner_instance = Cleaner(name=cleaner)
    hall_instance = CinemaHall(hall_number=hall_number)

    # 3. O corredor do cinema agenda e executa a sessão de filme
    hall_instance.movie_session(
        movie_name=movie,
        customers=customer_instances,
        cleaning_staff=cleaner_instance
    )
