import pytest
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.main import cinema_visit


def test_cinema_bar_sell_product(capsys: pytest.CaptureFixture[str]) -> None:
    # Testa a venda de um produto
    customer = Customer(name="Bob", food="popcorn")
    CinemaBar.sell_product(product="popcorn", customer=customer)
    captured = capsys.readouterr()
    assert captured.out == "Cinema bar sold popcorn to Bob.\n"


def test_customer_watch_movie(capsys: pytest.CaptureFixture[str]) -> None:
    # Testa o cliente assistindo a um filme
    customer = Customer(name="Bob", food="popcorn")
    customer.watch_movie(movie="Madagascar")
    captured = capsys.readouterr()
    assert captured.out == 'Bob is watching "Madagascar".\n'


def test_cleaner_clean_hall(capsys: pytest.CaptureFixture[str]) -> None:
    # Testa o faxineiro limpando a sala
    cleaner = Cleaner(name="Anna")
    cleaner.clean_hall(hall_number=5)
    captured = capsys.readouterr()
    assert captured.out == "Cleaner Anna is cleaning hall number 5.\n"


def test_cinema_hall_movie_session(capsys: pytest.CaptureFixture[str]) -> None:
    # Testa uma sessão de filme
    hall = CinemaHall(hall_number=5)
    customers = [
        Customer(name="Bob", food="Coca-cola"),
        Customer(name="Alex", food="popcorn"),
    ]
    cleaner = Cleaner(name="Anna")
    hall.movie_session(movie_name="Madagascar", customers=customers, cleaning_staff=cleaner)
    captured = capsys.readouterr()
    expected_output = (
        '"Madagascar" started in hall number 5.\n'
        'Bob is watching "Madagascar".\n'
        'Alex is watching "Madagascar".\n'
        '"Madagascar" ended.\n'
        'Cleaner Anna is cleaning hall number 5.\n'
    )
    assert captured.out == expected_output


def test_cinema_visit(capsys: pytest.CaptureFixture[str]) -> None:
    # Testa a visita completa ao cinema
    customers = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"},
    ]
    hall_number = 5
    cleaner_name = "Anna"
    movie = "Madagascar"
    cinema_visit(customers=customers, hall_number=hall_number, cleaner=cleaner_name, movie=movie)
    captured = capsys.readouterr()
    expected_output = (
        "Cinema bar sold Coca-cola to Bob.\n"
        "Cinema bar sold popcorn to Alex.\n"
        '"Madagascar" started in hall number 5.\n'
        'Bob is watching "Madagascar".\n'
        'Alex is watching "Madagascar".\n'
        '"Madagascar" ended.\n'
        'Cleaner Anna is cleaning hall number 5.\n'
    )
    assert captured.out == expected_output
