from PySimpleGUI import Text, Popup, Radio, Input, Window, WINDOW_CLOSED, theme, Button
from typing import Literal


class InterfaceGrafica:

    def __init__(self):
        theme('MeuTema')

        # modelo da janela 1
        self.layout1 = [
            [Text(f'\n{" "*12}JOGO DE MATEMÁTICA', size=(30, 3), background_color='#C3C3C3')],
            [Text('Selecione o nível de dificuldade:')],
            [Radio('Fácil', 'nivel', True, key='Fácil')],
            [Radio('Médio', 'nivel', key='Médio')],
            [Radio('Difícil', 'nivel', key='Difícil')],
            [Radio('Muito Difícil', 'nivel', key='Muito Difícil')],
            [Button('Iniciar'), Button('Sair')],
        ]

        # itens da janela 1
        self.janela1 = Window('jogo de matemática', self.layout1, ttk_theme='BlueMono')
        self.botoes1 = self.dados1 = self.nivel = None

    def menu_principal(self):
        while True:
            self.botoes1, self.dados1 = self.janela1.read()
            if self.botoes1 == WINDOW_CLOSED or self.botoes1 == 'Sair':
                self.janela1.close()
                return 'fim'


            if self.botoes1 == 'Iniciar':
                for chave, valor in self.dados1.items():
                    if valor is True:
                        self.nivel = chave
                        return self.nivel

    def janela_jogo(self, numero1: int, numero2: int, operacao: Literal['+', '-', 'x'], acertos: int, erros: int):
        # modelo da janela 2
        layout2 = [
            [Text('QUAL O RESULTADO?')],
            [Text(numero1, key='num1'), Text(operacao, key='operacao'), Text(numero2, key='num2'),
             Input('', size=(6, 1), key='resposta')],
            [Text('acertos:'), Text(acertos, key='acertos'), Text('erros:'), Text(erros, key='erros')],
            [Button('Confirmar'), Button('Sair')]
        ]

        # itens da janela 2:
        janela2 = Window('', layout2)

        while True:
            botoes2, dados2 = janela2.Read()

            if botoes2 == WINDOW_CLOSED or botoes2 == 'Sair':
                janela2.close()
                raise TypeError

            if botoes2 == 'Confirmar':
                try:
                    janela2.close()
                    return int(dados2['resposta'])

                except ValueError:
                    Popup('Insira apenas valores válidos')


if '__main__' == __name__:
    janela = InterfaceGrafica()
    #janela.menu_principal()
    janela.janela_jogo(12, 14, '-', acertos=1, erros=1)
