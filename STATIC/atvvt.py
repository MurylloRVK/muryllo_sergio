import json
 
json_string = "{}"
 
dic = {"chave" : 'valor', "numero" : 10}
 
print(dic["numero"])
 
with open(file = "o.json", mode = 'w') as file:
    file.write(json_string)
 
#CRIEM A TURMA COM BASE NESSA BARRAIA
 
class Aluno:
    def __init__(self, nome, turma):
        self.nome = nome
        self.turma = turma
    def apresentar(self):
        print(f"Oi eu sou {self.nome} e sou da turma {self.turma}")
alunos = []
alunos.append(Aluno("Murilo Verdadeiro", "ProgWEB"))
alunos.append(Aluno("Muryllo Falso", "ProgWEB"))
alunos.append(Aluno("Marcus", "ProgWEB"))
alunos.append(Aluno("Miguel", "ProgWEB"))
alunos.append(Aluno("Luis", "ProgWEB"))
alunos.append(Aluno("Gustavo", "ProgWEB"))
alunos.append(Aluno("Roberto", "ProgWEB"))
alunos.append(Aluno("Maria", "ProgWEB"))
alunos.append(Aluno("Kauã", "ProgWEB"))
jsonS = [
    {
        "nome" : aluno.nome,
        "turma" : aluno.turma      
    } for aluno in alunos
]
with open(file = "o.json", mode = 'w') as file:
    file.write(json.dumps(jsonS, indent=4))
def imprimir_alunos():
    with open("o.json", "r") as file:
        alunos = json.load(file)
    for aluno in alunos:
        print(f"Nome: {aluno['nome']} Turma: {aluno['turma']}")
imprimir_alunos() 
def writeJson(jsonString):
    with open(file = "o.json", mode = 'w') as file:
        file.write(json.dumps(jsonString, indent = 4))
def loadJson():
    with open(file = "o.json", mode = 'r') as file:
        return json.load(file)
lista_alunos = loadJson()
for aluno in lista_alunos:
    print(aluno)
    alunos.append(Aluno(aluno["nome"], aluno["turma"])) 
for aluno in alunos:
    aluno.apresentar()