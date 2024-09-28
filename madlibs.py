#Faça um jogo de madlibs; consiste em pegar palavras de diferentes classes e adicioná-las em uma frase (String)

#recebe o nome de um jogo pelo teclado e armazena na variável jogo
jogo = input("Entre com o nome de um jogo (eletrônico ou tradiional): ")

#recebe um verbo pelo teclado e armazena na variável verbo1
verbo1 = input("Entre com o verbo número um: ")

#recebe outro verbo pelo teclado e armazena na variável verbo2
verbo2 = input("Entre com o verbo número dois: ")

#recebe adjetivo pelo teclado e armazena na variável adjetivo
adjetivo = input("Entre com o adjetivo: ")

#Imprime a frase estática com as variáveis definidas anteriormente pelo usuário
madlib = "Participe das aulas como em " +jogo +", se divirta e " + verbo1 +", além de " +verbo2 +". Isto tudo é muito " +adjetivo + "."

#imprime a frase com as características fornecidas pelo usuário
print(madlib)