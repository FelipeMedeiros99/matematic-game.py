from typing import Literal
from random import randint


def jogo_soma(nivel: Literal['Fácil', 'Médio', 'Difícil', 'Muito Difícil']):
    if nivel == 'Fácil':
        num1 = randint(1, 20)
        num2 = randint(1, 20)
        return [num1, num2, '+', num1+num2]

    elif nivel == 'Médio':
        num1 = randint(10, 100)
        num2 = randint(10, 100)
        return [num1, num2, '+', num1+num2]

    elif nivel == 'Difícil':
        num1 = randint(100, 1000)
        num2 = randint(100, 1000)
        return [num1, num2, '+', num1+num2]

    elif nivel == 'Muito Difícil':
        num1 = randint(1000, 10_000)
        num2 = randint(1000, 10_000)
        return [num1, num2, '+', num1+num2]


def jogo_subtracao(nivel: Literal['Fácil', 'Médio', 'Difícil', 'Muito Difícil']):
    if nivel == 'Fácil':
        num1 = randint(1, 20)
        num2 = randint(1, 20)
        return [max(num1, num2), min(num1, num2), '-', max(num1, num2) - min(num1, num2)]

    elif nivel == 'Médio':
        num1 = randint(1, 20)
        num2 = randint(1, 20)
        return [max(num1, num2), min(num1, num2), '-', max(num1, num2) - min(num1, num2)]

    elif nivel == 'Difícil':
        num1 = randint(1, 20)
        num2 = randint(1, 20)
        return [max(num1, num2), min(num1, num2), '-', max(num1, num2) - min(num1, num2)]

    elif nivel == 'Muito Difícil':
        num1 = randint(1, 20)
        num2 = randint(1, 20)
        return [max(num1, num2), min(num1, num2), '-', max(num1, num2) - min(num1, num2)]


def jogo_multiplicacao(nivel: Literal['Fácil', 'Médio', 'Difícil', 'Muito Difícil']):
    if nivel == 'Fácil':
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        return [num1, num2, 'x', num1 * num2]

    elif nivel == 'Médio':
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        return [num1, num2, 'x', num1 * num2]

    elif nivel == 'Difícil':
        num1 = randint(10, 100)
        num2 = randint(10, 100)
        return [num1, num2, 'x', num1 * num2]

    elif nivel == 'Muito Difícil':
        num1 = randint(100, 1000)
        num2 = randint(100, 1000)
        return [num1, num2, 'x', num1 * num2]
