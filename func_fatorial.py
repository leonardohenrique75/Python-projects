#função que calcula fatorial com base no número dado (x)
def fatorial(x):
#define o valor de i, sendo desnecessário 1
    i = 2
    type(i)
#declara a variável fatorial
    fatorial = 1
    type(fatorial)
#calcula o fatorial, conforme fatorial.py
    while i <= x:
#começa a multiplica~çao de i até x
        fatorial = fatorial * i
#incrementa i em um de modo que satisfaça o laço
        i = i + 1
    return fatorial
#aqui, dentro da função, retorna o valor de função com base no número dado, e, claro, o devido fatorial
    print("O fatorial do número",x,"é de",fatorial)
#número quatro meramente para testes
fatorial(4)
#testes de acordo com a aula
def testa_fatorial():
    if fatorial(1) == 1:
        print("Funciona para 1")
    else:
        print("Não funciona para 1")
    if fatorial(2) == 2:
        print("Funciona para 2")
    else:
        print("Não funciona para 2")
    if fatorial(0) == 1:
        print("Funciona para 0")
    else:
        print("Não funciona para 0")
    if fatorial(5) == 120:
        print("Funciona para 5")
    else:
        print("Não funciona para 5)")
    
#ao executar o comando abaixo, fica claro que os casos funcionam no console
testa_fatorial()

#trasforma a subtração do n - k fatorial em uma função, afim de facilitar o entendimento
def subtração(n, k):
    return n - k
#deifne quociente, uma vez que estava tendo nonetype error por meio da multiplicação no original
def quociente_binomial(n, k):
    return (fatorial(k))*(fatorial(subtração(n, k)))
quociente_binomial(2, 4)
#função solicitada como exercício de treino, função final
def número_binomial(n, k):
    fatorial(n)
    fatorial(k)
#caso queira apenas valores inteiros, usar a //, e não / como divisão
    print("O valor do número binomial é de :",(fatorial(n)) / quociente_binomial(n, k))
#número_binomial(2, 4)
número_binomial(5, 3)
#abaixo, irá a função de teste referente ao número_binomial
def testa_binomial(n, k):
#testa com números negativos
    if número_binomial(-1, 2) == None:
#igual a null pois não há valor possível
        print("Funciona com n == -1")
    else:
        print("Não funciona com -1")
#testa com espaços negativos
    if número_binomial(10, -1) == None:
#igual a null pois não há valor possível
        print("Funciona com k == -1")
    else:
        print("Não funciona com k == -1")
#testa com zero no n
    if número_binomial(0, 10) == 1:
        print("Funciona com k == 0")
    else:
        print("Não funciona com k == 0")
#testa com zero espaços
    if número_binomial(10, 0) == 1:
        print("Funciona com n == 10")
    else:
        print("Não funciona com n == 0")
#por fim, testa com números muito grandes
    if número_binomial(50, 30) == 47129212243960:
        print("Funciona com números grandes.")
    else:
        print("Não funciona com números grandes")
        

testa_binomial(-1, 2)
testa_binomial(10, -1)
testa_binomial(0, 10)
testa_binomial(10, 0)
testa_binomial(50, 30)
