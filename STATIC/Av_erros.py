import json

class PioresErros:
    def __init__(self, nome, atrocidade, nota):
        self.nome = nome
        self.atrocidade = atrocidade
        self.nota = nota

    def mostrar(self):
        print(f"{self.nome} - {self.atrocidade} - Nota: {self.nota}")

piores_erros = []
for i in range(3):
    nome = str(input("Nome: "))
    atrocidade = str(input("Qual foi o erro: "))
    nota = int(input("Nota do erro (0-10): "))

    erro = PioresErros(nome, atrocidade, nota)
    piores_erros.append(erro)

piores = sorted(piores_erros, key=lambda erro: erro.nota)[:3]
dados = []
for erro in piores:
    dados.append({
        "nome": erro.nome,
        "atrocidade": erro.atrocidade,
        "nota": erro.nota
    })
with open("piores_erros.json", "w") as arquivo:
    json.dump(dados, arquivo, indent=4)
print("Piores erros salvos no JSON!")