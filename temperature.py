def check_temperature(tmp):


    if not isinstance(tmp, (int, float)) or isinstance(tmp, bool):
        return "INVALID"

    if tmp < 0:
        return "INVALID"

    if tmp < 30:
        return "NORMAL"

    elif tmp < 60:
        return "WARNING"

    else:
        return "ALERT"

