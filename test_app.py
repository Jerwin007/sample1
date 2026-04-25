from app import add, greet

def test_add():
    assert add(3, 5)

def test_greet():
    assert greet("Nick")
