import json

class Atrocidade:     #cria a classe Atrocidade

    def __init__(self, nome, atrocidade, nota):   #cria uma nova atrocidade

        self.nome = nome

        self.atrocidade = atrocidade

        self.nota = nota    #guarda a nota da atrocidade

    def para_dict(self):    #cria uma função para transformar o objeto em dicionário

        return {                    #retorna os dados em formato de dicionário
            "nome": self.nome,
            "atrocidade": self.atrocidade,
            "nota": self.nota
        }

atrocidades = []    #cria uma lista para guardar atrocidades

while True:   #aqui cria um loop infinito para adicionar erros

    nome = input("Nome do aluno: ")   #pede o nome do aluno

    atrocidade = input("Qual foi a atrocidade: ")  #pede a descrição da atrocidade

    nota = int(input("Nota da atrocidade (0-10): "))

    erro = Atrocidade(nome, atrocidade, nota) # cria um objeto para classe Atrocidade

    atrocidades.append(erro)   #ADD erro a lista

    continuar = input("Deseja adicionar outro erro? (sim/não): ") #quer adicionar outro?   

    if continuar.lower() != "sim":  #se sim acabo
        break

dados = []   #aqei cria ima lista pra G. os dados

for erro in atrocidades:

    dados.append(erro.para_dict())   #3converyte para o dicionario

with open("atrocidades.json", "w", encoding="utf-8") as arquivo:  #aqui abre ou pode criar o arquivo para escrita

    json.dump(dados, arquivo, indent=4, ensure_ascii=False)  

print("Atrocidades salvas com sucesso!")   #dis q foi salvo

with open("atrocidades.json", "r", encoding="utf-8") as arquivo:   #abre o arquivo json para a leitura

    dados_carregados = json.load(arquivo)   #pega e carrega os dados do arquivo JSON

print("\nAtrocidades carregadas:") #mostra os dados carregados

for erro in dados_carregados:   #aqui ele vai percorrer todos os erros carregados

    print(f"Nome: {erro['nome']}")  #mostra o nome

    print(f"Atrocidade: {erro['atrocidade']}")  #mostra a atrocidade

    print(f"Nota: {erro['nota']}") #nota

    print("--------------------")  #aqui ele bota uma linha para separar os erros e ficar bonitinho
    