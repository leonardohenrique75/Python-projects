import random

#funcao que ira definir o resultado, aleatoriedade do computador e pega entrada do teclado para saber qual dos 3 valores o jogador escolheu
def play():
#solicita pelo teclado qual a escolha do jogador
    usuario = input("Qual sua escolha: 'r' para pedra, 'p' para papel, 's' para tesoura")
#aleatoriza a escolha do computador 
    computador = random.choice(['r', 'p', 's'])
#caso o valor dado pelo usuario seja o mesmo do jogador, e um empate    
    if usuario == computador:
#printa que e um empate
        return 'É um empate.'
#condicao que testa se a vitoria foi ou nao consumada   
    if is_win(usuario, computador):
#em caso positivo, retorna mensagem gratificando
        return 'Você ganhou!'
#em caso negativo, retorna mensagem informando
    return 'Você perdeu!'
#funcao que define se ganhou ou perdeu
def is_win(jogador, oponente):
#testa as condicoes de vitoria necessarias para a vitoria
    if jogador == 'r' and oponente == 's' or jogador == 's' and oponente == 'p' or jogador == 'p' and oponente == 'r': 
        return True
#caso for diferente de qualquer uma destas, retorna False pois significa que jogador perdeu
    else:
        return False
#roda o jogo    
print(play())