from temperature import check_temperature


def test_normal_temperature():
    assert check_temperature(20) == "NORMAL"
    assert check_temperature(25) == "NORMAL"


def test_limit_below():
    assert check_temperature(29) == "NORMAL"


def test_limit_exact():
    assert check_temperature(30) == "ALERT"


def test_high_temperature():
    assert check_temperature(40) == "ALERT"