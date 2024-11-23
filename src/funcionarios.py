class Funcionario:
    """
    Classe que representa um funcionário com ID, nome e cargo.

    Atributos de classe
    -------------------
    ultimo_id : int
        Mantém o último ID gerado para os funcionários.

    Atributos de instância
    -----------------------
    id : int
        ID único do funcionário.
    nome : str
        Nome do funcionário.
    cargo : str
        Cargo do funcionário.

    Métodos
    -------
    __str__()
        Retorna uma representação em string do funcionário.

    Exemplos
    --------
    >>> funcionario1 = Funcionario("João", "Gerente")
    >>> funcionario2 = Funcionario("Ana", "Analista")
    >>> print(funcionario1)
    ID: 1, Funcionário: João, Cargo: Gerente
    >>> print(funcionario2)
    ID: 2, Funcionário: Ana, Cargo: Analista
    """

    ultimo_id = 0

    def __init__(self, nome, cargo):
        """
        Inicializa uma nova instância de Funcionario.

        Parâmetros
        ----------
        nome : str
            Nome do funcionário.
        cargo : str
            Cargo do funcionário.
        """
        Funcionario.ultimo_id += 1
        self.id = Funcionario.ultimo_id
        self.nome = nome
        self.cargo = cargo

    def __str__(self):
        """
        Retorna uma string representando o funcionário.

        Returns
        -------
        str
            Representação do funcionário com ID, nome e cargo.
        """
        return f"ID: {self.id}, Funcionário: {self.nome}, Cargo: {self.cargo}"

def cria_novo_funcionario():
    """
    Cria um novo funcionário solicitando nome e cargo ao usuário.

    Returns
    -------
    Funcionario
        Objeto `Funcionario` criado com os dados fornecidos pelo usuário.

    Exemplos
    --------
    >>> funcionario = cria_novo_funcionario()
    Nome do funcionário: João
    Cargo do funcionário: Gerente
    >>> print(funcionario)
    ID: 1, Funcionário: João, Cargo: Gerente
    """
    nome = input("Nome do funcionário: ")
    cargo = input("Cargo do funcionário: ")
    return Funcionario(nome, cargo)


def imprime_lista_de_funcionarios(funcionarios):
    """
    Imprime a lista de funcionários fornecida.

    Parâmetros
    ----------
    funcionarios : list of Funcionario
        Lista contendo objetos da classe `Funcionario`.

    Returns
    -------
    None

    Exemplos
    --------
    >>> funcionarios = [Funcionario("João", "Gerente"), Funcionario("Ana", "Analista")]
    >>> imprime_lista_de_funcionarios(funcionarios)
    Lista de Funcionários:
    ID: 1, Funcionário: João, Cargo: Gerente
    ID: 2, Funcionário: Ana, Cargo: Analista
    """
    print("Lista de Funcionários:")
    for funcionario in funcionarios:
        print(funcionario)