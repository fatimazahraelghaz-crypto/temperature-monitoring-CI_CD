from temperature import check_temperature

def test_25():
    assert check_temperature(25) == "NORMAL"

def test_29_9():
    assert check_temperature(29.9) == "NORMAL"

def test_30():
    assert check_temperature(30) == "WARNING"

def test_45():
    assert check_temperature(45) == "WARNING"

def test_59_9():
    assert check_temperature(59.9) == "WARNING"
    
def test_60():
    assert check_temperature(60) == "ALERT"

def test_conversion():
    assert convert_to_fahrenheit(0) == 32