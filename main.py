import random

import utils


def main():
    continuar_jogando = True
    while continuar_jogando:
        jogo = [0,0,0,0,0,0,0,0,0]
        quem_comeca = random.randint(0,1)
        if quem_comeca == 0:
            print(' O jogador que usaram X ira começar! \n')
            while True:
                escolha = int(input('(Jogador X) Escolha um numero de 1 a 9: '))
                while True:
                    if jogo[escolha-1] == 0:
                        jogo[escolha-1] = 1
                        break
                    else:
                        escolha = int(input('(Jogador X) Escolha um numero de 1 a 9: '))
                utils.exibe(jogo)
                if not(utils.saida_estado(jogo) == True):
                    if (input('Quer parar de jogar? (S)im ou qualquer outra tecla para continuar: ')).lower() == 's':
                        continuar_jogando = False
                    break
                escolha = int(input('(Jogador O) Escolha um numero de 1 a 9: '))
                while True:
                    if jogo[escolha-1] == 0:
                        jogo[escolha-1] = -1
                        break
                    else:
                        escolha = int(input('(Jogador O) Escolha um numero de 1 a 9: '))
                utils.exibe(jogo)
                if not(utils.saida_estado(jogo) == True):
                    if (input('Quer parar de jogar? (S)im ou qualquer outra tecla para continuar: ')).lower() == 's':
                        continuar_jogando = False
                    break
        else:
            print(' O jogador que usaram O ira começar! \n')
            while True:
                escolha = int(input('(Jogador O) Escolha um numero de 1 a 9: '))
                while True:
                    if jogo[escolha-1] == 0:
                        jogo[escolha-1] = -1
                        break
                    else:
                        escolha = int(input('(Jogador O) Escolha um numero de 1 a 9: '))
                utils.exibe(jogo)
                if not(utils.saida_estado(jogo) == True):
                    if (input('Quer parar de jogar? (S)im ou qualquer outra tecla para continuar: ')).lower() == 's':
                        continuar_jogando = False
                    break
                escolha = int(input('(Jogador X) Escolha um numero de 1 a 9: '))
                while True:
                    if jogo[escolha-1] == 0:
                        jogo[escolha-1] = 1
                        break
                    else:
                        escolha = int(input('(Jogador X) Escolha um numero de 1 a 9: '))
                utils.exibe(jogo)
                if not(utils.saida_estado(jogo) == True):
                    if (input('Quer parar de jogar? (S)im ou qualquer outra tecla para continuar: ')).lower() == 's':
                        continuar_jogando = False
                    break

main()
