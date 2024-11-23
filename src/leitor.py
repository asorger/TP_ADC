class Leitor:

    ultimo_id = 0

    def __init__(id, self, nome, idade, email):
        Leitor.ultimo_id += 1
        self.id = id
        self.nome = nome
        self.idade = idade
        self.email = email


    def __str__(self):
        return f"ID: {self.id}, Leitor: {self.nome}, Idade: {self.idade}, Email: {self.email}"


def cria_novo_leitor():
    nome = input("Nome do leitor: ")
    idade = int(input("Idade do leitor: "))
    email = input("Email do leitor: ")
    return Leitor(nome, idade, email)


def imprime_lista_de_leitores(leitores):
    print("Lista de Leitores:")
    for leitor in leitores:
        print(leitor)