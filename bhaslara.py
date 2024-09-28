import math

#Recebe o valor da equação
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digie o valor de c: "))

#if a == 0:
 #   print("Não há o que se resolver, pois não é uma equação de segundo grau, mas sim de primeiro.")
#else:
#   x = a*(x**2) + (b*x) + c   #set os valores de entrada na equação

#calcula o delta para saber se terá uma raiz, duas ou nenhuma
delta = (b**2) - (4 * a * c)

if delta > 0:
 #   print("Há duas soluções/raízes para a equação.")
    X = (-b + math.sqrt(delta)) / (2 * a)
    Y = (-b - math.sqrt(delta)) / (2 * a)
    if X < Y:
        print("as raízes da equação são",+X,"e",+Y)
    else:
        print("as raízes da equação são",+Y,"e",+X)
#    print("A solução número um é: ",+x1)
#    print("A solução número dois é:",+x2)
elif delta == 0:
#    print("Há uma solução/raíz possível para a equação.")
    X = (-b + math.sqrt(delta)) / (2 * a)
    print("a raíz desta equação é",+X)
else:
    print("esta equação não possui raízes reais")

   
