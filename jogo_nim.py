def main():
#pergunta se o usuário quer jogar uma partida ou campeonato
    print("Bem-vindo ao jogo do NIM! Escolha: ")
#printa a opçção 01 a ser escolhida posteriormente
#    print("1 = para jogar uma partida isolada ")
#printa a opção 02 a ser escolhida posteriormente
    resp = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n"))
 #   print("2 - para jogar um campeonato ")
#recebe do teclado o valor desejado
#    teclado = int(input("Digite 1 ou 2. "))
#testa o valor e...
    if resp == 1:
#se for 1, Ã© uma partida isolada
#printa a mensagem na tela
        print("Você escolheu uma partida isolada!")
        partida()
#mas se for 2, Ã© um campeonato
    elif resp ==  2:
#printa a mensagem na tela
        print("Você escolheu um campeonato!")
        campeonato()
#se for qualquer outra coisa...
    else:
#mostra mensagem de erro e pede para rodar novamente
        print("Dígito inválido! Comece novamente!")
#mensagem puramente estática indicando a rodada atual
    print("**** Rodada única ****")
#inicializa a função partida
def partida():
#    computador = 0
#    jogada_usuario = 0 
#pergunta quantas peças o jogador quererÃ¡ ter no jogo
    n = int(input("Quantas peças? "))   
#define quantas peças serÃ£o retiradas por rodada 
    m = int(input("Limite de peças por jogada? "))
    print(" ")
#verifica se não é múltiplo de (m + 1) ARRUMAR DEPOIS
    if n % (m + 1) == 0:
#computador deixa o usuário começar
        print("Você começa!")
#define variável booleana para usar em outrsa função
        vez_do_computador = False
    else:
#caso a condição seja invÃ¡lida, o computador começa
        print("Computador começa!")
#agora é a vez do pc, então é true
        vez_do_computador = True
#laço dentro de partida
#o qual é o indicador da partida, dura enquanto > 0
    while n > 0:
#caso for a vez do computador
        if vez_do_computador is True:
#chama a função do pc
            jogada_computador = computador_escolhe_jogada(n, m)
            print("O computador tirou", jogada_computador, "peça(s)\n")
#seta a variável para falsa, pois acabou a vez do pc
            n = n - jogada_computador
            vez_do_computador = False
#quando acaba o pc, começa o usuário
        else:
#agora é a vez do usuário, chama função
            jogada_usuario = usuario_escolhe_jogada(n, m)
            n -= jogada_usuario
#acabou o turno do user, é a vez do computador
#logo, vezpc = true
            if n > 0:
                print("Agora restam", n, "peças no tabuleiro.\n")
        vez_do_computador = True
        if n == 1:
            print("Agora resta 1 peça no tabuleiro.\n")
#executa para ver quem ganhou
    if vez_do_computador:
#mensagem de fim de jogo com vitória da máquina
        print("Fim do jogo! O computador ganhou!\n")
#retorna o computador
        return "computador"
#se não
    else:
#mensagem caso usuário ganhar
        print("Fim do jogo! Você ganhou!\n")
#retorna jogador ganhador
        return "jogador"
#função da opção campeonato
def campeonato():
#inicializa as vars de placar de ambos
    placar_jogador = 0
    placar_computador = 0
#    rodada = 1
#    computador = 0
#enquanto for menor que quatro games
#    while rodada < 4:
    for rodada in range(1,4):
#printa o nome da rodada
        print("**** Rodada", rodada,"****\n")
#estabelece o resultado da partida
        resultado = partida()
#se computador ganhar
        if "computador" in resultado:
#incrementa-se um ponto
            placar_computador += 1
#rodada é aumentada em ambos
 #           rodada = rodada + 1
#caso contrário
        else:
#user ganha mais um ponto
            placar_jogador += 1
#rodada é incrementada, de todo modo
      #      rodada = rodada + 1
#ao fim, estabelece o final do campeonato
    print("\n**** Final do Campeonato! ****\n")
#printa placar
    print("Placar: Você", placar_jogador, "X", placar_computador, "Computador\n")
    
#função da jogada do computador
def computador_escolhe_jogada(n, m):
#define a variável jogada, começando em 1, obviamente
    jogada = 1
#enquanto a jogada for diferente do nÃºmero de peças
    while jogada != m:
#tentando retirar o maior numero de peças e multiplos
        if (n - jogada) % (m + 1) == 0:
#retorna a variável jogada
            return jogada
#incrementa o contador do while em 1
        jogada = jogada + 1
#retorna jogada
    return jogada

#função dajogada do usuário[
def usuario_escolhe_jogada(n, m):
#laço para saber quantas peças irá se retirar
    while True:
        jogada = int(input("Quantas peças você vai tirar? "))
#trata alguns erros abaixo
        if jogada > m or jogada > n or jogada <= 0:
            print("Oops! Jogada inválida! Tente de novo")
        else:
#caso retira uma peça
            if jogada == 1:
#mensagem para uma peça retirada
                print("Você tirou 1 peça!")
            else:
#mensagem que mostra quantas peças foram retiradas
                print("Você tirou",jogada, "peças!")
#retorna jogada no final do laço
            return jogada

main()
