import ast
from app import main

def test_cinema_bar_import():
    with open(main.__file__, "r") as source:
        parsed_module = ast.parse(source.read())
        random_import = None

        for child in parsed_module.body:
            if isinstance(child, ast.ImportFrom) and child.module == 'app.cinema_bar':
                random_import = child
        assert (
            random_import is not None
        ), "Class 'CinemaBar' should be imported using 'from'"

def test_cinema_hall_import():
    with open(main.__file__, "r") as source:
        parsed_module = ast.parse(source.read())
        random_import = None

        for child in parsed_module.body:
            if isinstance(child, ast.ImportFrom) and child.module == 'app.cinema_hall':
                random_import = child
        assert (
            random_import is not None
        ), "Class 'CinemaHall' should be imported using 'from'"

def test_cleaner_import():
    with open(main.__file__, "r") as source:
        parsed_module = ast.parse(source.read())
        random_import = None

        for child in parsed_module.body:
            if isinstance(child, ast.ImportFrom) and child.module == 'app.cleaner':
                random_import = child
        assert (
            random_import is not None
        ), "Class 'Cleaner' should be imported using 'from'"

def test_customer_import():
    with open(main.__file__, "r") as source:
        parsed_module = ast.parse(source.read())
        random_import = None

        for child in parsed_module.body:
            if isinstance(child, ast.ImportFrom) and child.module == 'app.people.customer':
                random_import = child
        assert (
            random_import is not None
        ), "Class 'Customer' should be imported using 'from'"
