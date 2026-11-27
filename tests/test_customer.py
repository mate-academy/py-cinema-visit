import io

from contextlib import redirect_stdout

from app.people.customer import Customer


def test_customer_constructor():
    customer = Customer(name="Bob", food="popcorn")
    assert hasattr(customer, "name"), (
        "Customer instance should have 'name' attribute"
    )
    assert hasattr(customer, "food"), (
        "Customer instance should have 'food' attribute"
    )
    assert customer.name == "Bob", (
        f"Value of attribute 'name' should equal to 'Bob' when "
        f"instance is created by 'Customer(name='Bob', food='popcorn')'"
    )
    assert customer.food == "popcorn", (
        f"Value of attribute 'food' should equal to 'popcorn' when "
        f"instance is created by 'Customer(name='Bob', food='popcorn')'"
    )


def test_customer_watch_movie():
    name = "Bob"
    movie = "Matrix"
    customer = Customer(name=name, food="popcorn")
    f = io.StringIO()

    with redirect_stdout(f):
        customer.watch_movie(movie)

    out = f.getvalue()
    output = 'Bob is watching "Matrix".\n'
    assert out == output, (
        f"'watch_movie' output should equal to {output}, "
        f"when customer's name is '{name} and movie is {movie}"
    )