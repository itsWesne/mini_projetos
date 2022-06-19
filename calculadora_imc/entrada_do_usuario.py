def calculo_imc(a, p):
    imc = p / (a * a)
    return f'{imc:.2f}'


def set_float(input_a):
    try:
        float_input_a = float(input_a)
        return float_input_a
    except ValueError:
        pass


def show_more_infos(imc):
    if imc < 18.5:
        return '''Você está abaixo do peso ideal!
Isso pode ser apenas uma característica
pessoal,mas também pode ser um sinal
de desnutrição ou de algum problema
de saúde'''
    elif 18.5 <= imc <= 24.9:
        return '''Você está com o peso normal!
Parabéns, você está com o peso normal.
Recomendamos que mantenha hábitos 
saudáveis em seu dia a dia. '''
    elif 25.0 <= imc <= 29.9:
        return '''Você está com sobrepeso!
Atenção! Alguns quilos a mais já são 
suficientes para que algumas pessoas
desenvolvam doenças associadas,
como diabetes e hipertensão. '''
    elif 30 <= imc <= 40:
        return '''Você está com obesidade!
Sinal de alerta! O excesso de peso é 
fator de risco para desenvolvimento de
outros problemas de saúde. '''
    else:
        return '''Você está com obesidade severa!'''




