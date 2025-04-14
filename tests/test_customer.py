from app.people.customer import Customer

def test_customer_constructor():
    customer = Customer(name="Bob", food="popcorn")
    assert customer.name == "Bob"
    assert customer.food == "popcorn"

def test_customer_watch_movie():
    name = "Bob"
    movie = "Matrix"
    customer = Customer(name=name, food="popcorn")
    assert customer.name == name
    assert customer.food == "popcorn"
