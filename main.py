from libs.gui import *
from libs.logica_jogo import *
from random import choice

if __name__ == '__main__':
    while True:
        jogo = InterfaceGrafica()
        erros = acertos = 0
        nivel = jogo.menu_principal()
        if nivel == 'fim':
            break
        while True:
            try:
                operacao = choice([jogo_soma(nivel), jogo_subtracao(nivel), jogo_multiplicacao(nivel)])
                resultado = jogo.janela_jogo(operacao[0], operacao[1], operacao[2], acertos, erros)
                if int(resultado) == int(operacao[3]):
                    acertos += 1
                else:
                    erros += 1
                    Popup(f'resposta correta:\n'
                          f'{operacao[0]} {operacao[2]} {operacao[1]} = {operacao[3]}')

            except TypeError:
                Popup(f'Acertos: {acertos}, Erros: {erros}')
                break
