import json


class Arquivo:            #CRIA UMA classe chamada Arquivo
    def __init__(self, nome, utilizado):       
        self.nome = nome
        self.utilizado = utilizado    #recebe duas informaçoes, nome e utilizado

    def verificar(self):     #cria uma função chamada verificar
        if self.utilizado.lower() == "não":
            print(f"O arquivo {self.nome} pode ser removido.")
        else:
            print(f"O arquivo {self.nome} deve ser mantido.")   #se a resposta for "não", o arquivo pode ser removido, caso contrário, deve ser mantido


arquivo = input("Digite o nome do arquivo: ")      #guarda o N. do arquivo digitado pelo usuário na variável "arquivo"
resposta = input("Você usa esse arquivo? (sim/não): ")

meu_arquivo = Arquivo(arquivo, resposta)   #
meu_arquivo.verificar()

dados = {       #cria um dicionario
    "nome": meu_arquivo.nome,
    "utilizado": meu_arquivo.utilizado
}

with open("arquivo.json", "w", encoding="utf-8") as arquivo_json:
    json.dump(dados, arquivo_json, indent=4, ensure_ascii=False)