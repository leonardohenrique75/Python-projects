import random
#importa random acima para tentar aleatorizar um número abaixo

#função
def adivinhe(x):
#gera número aleatório maior que um apenas uma vez e o armazena em nova variável
    numero_aleatorio = random.randint(1, x)
#adivinhe é zero, uma vez que será menor que um e nunca adivinhado antes de rodar o código por inteiro
    adivinhe = 0
#    str(x)
#    str(adivinhe)
#    str(numero_aleatorio)
#laço que indica que enquanto o adivinhe for diferente, o usuário deve tentar adivinhar o número até acertar
    while adivinhe != numero_aleatorio:
#recebe do teclado a adivinhação do usuário
        adivinhe = int(input("Adivinhe o número entre 1 e " +str(x) +": "))
#condição que testa se o número adivinhado é menor que o número específico
        if adivinhe <= numero_aleatorio:
#retorna um feedback, caso for realmente menor, para ajudar a adivinhar
            print("Desculpe, adivinhe novamente, tente um número maior!")
#condição que testa se o número adivinhado é maior que o número específico
        elif adivinhe >= numero_aleatorio:
#retorna um feedback, caso for realmente maior, para ajudar a adivinhar
            print("Desculpe, adivinhe novamente, tente um número menor!")
        else:
#sai do laço caso adivinhe, cuidado com bugs
            break
#printa caso você tenha adivinhado o número e o número em questão
    print("Parabéns, você adivinhou o número aleatório" + str(numero_aleatorio) + "!")
#imprime o número adivinhado
        
adivinhe(9)