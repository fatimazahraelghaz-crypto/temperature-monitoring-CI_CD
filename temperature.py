def check_temperature(tmp):
    if tmp < 30:
        return "NORMAL"
    else:
        return "ALERT"


if __name__ == "__main__":
    print("Test 25°C :", check_temperature(25))
    print("Test 35°C :", check_temperature(35))