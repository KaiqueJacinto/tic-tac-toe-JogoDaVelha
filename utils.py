def verifica_estado(jogo):
    if jogo[:3] == [1,1,1] or jogo[3:6] == [1,1,1] or jogo[6:] == [1,1,1] or (jogo[0]==1 and jogo[3]==1 and jogo[6]==1) or (jogo[1]==1 and jogo[4]==1 and jogo[7]==1) or (jogo[2]==1 and jogo[5]==1 and jogo[8]==1) or (jogo[0]==1 and jogo[4]==1 and jogo[8]==1) or (jogo[2]==1 and jogo[4]==1 and jogo[6]==1):
        return 0
    elif jogo[:3] == [-1,-1,-1] or jogo[3:6] == [-1,-1,-1] or jogo[6:] == [-1,-1,-1] or (jogo[0]==-1 and jogo[3]==-1 and jogo[6]==-1) or (jogo[1]==-1 and jogo[4]==-1 and jogo[7]==-1) or (jogo[2]==-1 and jogo[5]==-1 and jogo[8]==-1) or (jogo[0]==-1 and jogo[4]==-1 and jogo[8]==-1) or (jogo[2]==-1 and jogo[4]==-1 and jogo[6]==-1):
        return 1
    else:
        if not(0 in jogo):
            return 2

def exibe(jogo):
    jogo = converte(jogo)
    imagem = f'''\n {jogo[0]} | {jogo[1]} | {jogo[2]} \n ---------- \n {jogo[3]} | {jogo[4]} | {jogo[5]} \n ---------- \n {jogo[6]} | {jogo[7]} | {jogo[8]} \n'''
    print(imagem)

def converte(jogo):
    jogo_modificado = jogo.copy()
    aux = {-1:'O',1:'X',0:' '}
    for num in range(-1,2):
        for num_item in range(len(jogo)):
            if num == jogo[num_item]:
                jogo_modificado[num_item] = aux[num]
    return jogo_modificado


def saida_estado(jogo):
    estado = verifica_estado(jogo)
    if estado == 0:
        print('Jogador X ganhou!')
        return False
    elif estado == 1:
        print('Jogador O ganhou!')
        return False
    elif estado == 2:
        print('Deu velha!')
        return False
    else:
        return True

#print(saida_estado([1, -1, -1, 0, 1, 0, 0, 0, 1]))
