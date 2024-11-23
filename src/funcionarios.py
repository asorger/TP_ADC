class Funcionario:

    ultimo_id = 0
    def __init__(self, nome, cargo):
        Funcionario.ultimo_id += 1
        self.id = Funcionario.ultimo_id
        self.nome = nome
        self.cargo = cargo

    def __str__(self):
        return f"ID: {self.id}, Funcionário: {self.nome}, Cargo: {self.cargo}"

def cria_novo_funcionario():
    nome = input("Nome do funcionário: ")
    cargo = input("Cargo do funcionário: ")
    return Funcionario(nome, cargo)

def imprime_lista_de_funcionarios(funcionarios):
    print("Lista de Funcionários:")
    for funcionario in funcionarios:
        print(funcionario)