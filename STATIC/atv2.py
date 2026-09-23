class Aluno:        #cria uma clase chamda aluno
    def __init__(self, nome, curso):
        self.nome = nome
        self.curso = curso
aluno1 = Aluno("Muryllo", "Criador de Páginas na Web")   #objeto
print(aluno1.nome)
print(aluno1.curso)
def apresentar(self):
    print(f"Olá! Meu nome é {self.nome} e faço o curso de {self.curso}.")