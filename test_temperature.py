from temperature import check_temperature


def test_negative_temperature():
    assert check_temperature(-10) == "INVALID"


def test_text_input():
    assert check_temperature("abc") == "INVALID"


def test_empty_input():
    assert check_temperature(None) == "INVALID"
    

def test_boolean_input():
    assert check_temperature(True) == "INVALID"