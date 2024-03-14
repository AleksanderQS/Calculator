from decimal import Decimal


def calculate(signal, act_value):
    try:
        value = eval(act_value)

        if signal == '%':
            value /= 100
        elif signal == '±':
            value = -value
    except:
        return 'Error'

    digits = min(abs(Decimal(value).as_tuple().exponent), 5)
    return format(value, f'.{digits}f')
