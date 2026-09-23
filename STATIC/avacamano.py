 import json

json_string = "{}"
dic = {"chave" : 'valor', "numero" : 10}
print(dic["numero"])

# \/\/\/\/\//\/\/\
# CRIEM A TURMA COM BASE NESSA BARRAIA

class Aluno:
    def __init__(self, nome, turma):
        self.nome = nome
        self.turma = turma

alunos = []
alunos.append(Aluno("Murilo Verdadeiro", "ProgWEB"))
alunos.append(Aluno("Muryllo Falso", "ProgWEB"))
alunos.append(Aluno("Gustovo", "ProgWEB"))
alunos.append(Aluno("Miguel", "ProgWEB"))
alunos.append(Aluno("Luis", "ProgWEB"))
alunos.append(Aluno("Maria", "ProgWEB"))
alunos.append(Aluno("Kauã", "ProgWEB"))
alunos.append(Aluno("Roberto", "ProgWEB"))
alunos.append(Aluno("Marcos", "ProgWEB"))

jsonS = [
    {
        "nome" : aluno.nome,
        "turma" : aluno.turma
        
    } for aluno in alunos
]

with open(file = "o.json", mode = 'w') as file:
    file.write(json.dumps(jsonS, indent = 4 ))
def writejson(jsonString):
    with open(file = "o.json", mode = 'w') as file:
        file.write(json.dumps(jsonString, indent = 4))
def loadJson():
    with open(file = "o.json", mode = 'r') as file:
     return  json.load(file)

print(loadJson())