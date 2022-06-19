def calculo_imc(a, p):
    imc = p / (a * 2)
    return f'{imc:.2f}'


def set_float(input_a):
    try:
        float_input_a = float(input_a)
        return float_input_a
    except ValueError:
        pass




