
anoNac = int(input("Que ano vc nasceu palhaço? "))
AnoAtual = int(input("Que ano é"))
def descobre_idade(anoA, anoN):
    idade = anoA - anoN
    return idade
print(f"então vc tem {descobre_idade(anoA = AnoAtual, anoN = anoNac)} anos")


a = int(input("Que ano q vc nasceu? "))
b = int(input("Que ano é? "))
def descobre_ano(idade, anoAtual):
    anoN = anoAtual - idade
    return anoN
print(f"então vc tem{descobre_ano(anoAtual = b, idade = a)}anos")


## 1 linha Pede o ano em que a pessoa nasceu
## 2 linha  Pede o ano atual
 ##  dai ele cria uma função para descobrir a idade
    ## idade = anoA - anoN   Calcula a idade subtraindo o ano de nascimento do ano atual
    return idade  # Retorna o resultado da idade

print(f"então vc tem {descobre_idade(anoA = AnoAtual, anoN = anoNac)} anos")  ## Mostra a idade calculada na tela


a = int(input("Que ano q vc nasceu? "))  ## Pede o ano em que vc nasceu
b = int(input("Que ano é? "))  ## Pede o ano atual

def descobre_ano(idade, anoAtual):  ## Cria uma função para fazer um cálculo usando dois valores
    anoN = anoAtual - idade  ## Faz a subtração entre o ano atual e o valor informado
    return anoN  ## Retorna o resultado da subtração

 ## dai mostra o resultado da função na tela

idade = 16  # Cria uma variável para guardar a idade
nome = "Muryllo"  # Cria uma variável para guardar o nome
print("Oi, eu sou", nome, "e tenho", idade, "anos.")  # Faz uma apresentação usando as variáveis