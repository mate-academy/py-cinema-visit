import ast
from _ast import ImportFrom

from app import main


def test_cinema_bar_import():
    with open(main.__file__, "r") as source:
        parsed_module = ast.parse(source.read())
        random_import = None

        for child in parsed_module.body:
            if isinstance(child, ImportFrom) and child.module == 'app.cinema.bar':
                random_import = child
    assert (
            random_import is not None
    ), "Class 'CinemaBar' should be imported using 'from'"
    assert (
            random_import.names[0].name == "CinemaBar"
    ), "Class 'CinemaBar' should be imported from 'cinema_bar' module"


def test_cinema_hall_import():
    with open(main.__file__, "r") as source:
        parsed_module = ast.parse(source.read())
        random_import = None

        for child in parsed_module.body:
            if isinstance(child, ImportFrom) and child.module == 'app.cinema.hall':
                random_import = child
    assert (
            random_import is not None
    ), "Class 'CinemaHall' should be imported using 'from'"
    assert (
            random_import.names[0].name == "CinemaHall"
    ), "Class 'CinemaHall' should be imported from 'cinema_hall' module"


def test_cleaner_import():
    with open(main.__file__, "r") as source:
        parsed_module = ast.parse(source.read())
        random_import = None

        for child in parsed_module.body:
            if isinstance(child, ImportFrom) and child.module == 'app.people.cinema_staff':
                random_import = child
    assert (
            random_import is not None
    ), "Class 'Cleaner' should be imported using 'from'"
    assert (
            random_import.names[0].name == "Cleaner"
    ), "Class 'Cleaner' should be imported from 'cinema_staff' module"


def test_customer_import():
    with open(main.__file__, "r") as source:
        parsed_module = ast.parse(source.read())
        random_import = None

        for child in parsed_module.body:
            if isinstance(child, ImportFrom) and child.module == 'app.people.customer':
                random_import = child
    assert (
            random_import is not None
    ), "Class 'Customer' should be imported using 'from'"
    assert (
            random_import.names[0].name == "Customer"
    ), "Class 'Customer' should be imported from 'customer' module"
