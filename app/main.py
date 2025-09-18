from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers, hall_number, cleaner, movie) -> None:
    """
    Orquestra a visita ao cinema:
    - Vende os itens do bar para cada cliente
    - Inicia a sessão no hall especificado
    - Cada cliente assiste ao filme
    - O cleaner limpa o hall ao final
    (Tudo via prints, conforme os testes esperam.)
    """
    bar = CinemaBar()
    hall = CinemaHall(number=hall_number)
    cleaner_obj = Cleaner(name=cleaner)

    # cria os objetos Customer a partir dos dicionários de entrada
    customer_objs = [Customer(name=c["name"], food=c["food"]) for c in customers]

    # vende os produtos antes do filme
    for cust in customer_objs:
        bar.sell_product(customer=cust, product=cust.food)

    # roda a sessão do filme (imprime início, cada cliente assistindo e fim + limpeza)
    hall.movie_session(movie, customer_objs, cleaner_obj)
