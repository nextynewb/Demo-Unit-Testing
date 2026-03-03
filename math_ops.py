def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def test_add():
    """Test the add function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-1, -1) == -3 # this should pass

def test_subtract():
    """Test the subtract function."""
    assert subtract(10, 5) == 5
    assert subtract(0, 5) == -5
    assert subtract(-1, -1) == 0


