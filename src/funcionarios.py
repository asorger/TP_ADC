class Funcionario:
    """
    Classe que representa um funcionário com nome e cargo.
    
    Atributos
    ---------
    nome : str
        Nome do funcionário.
    cargo : str
        Cargo do funcionário.

    Métodos
    -------
    __str__()
        Retorna uma representação em string do funcionário.
    """

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
        self.nome = nome
        self.cargo = cargo

    def __str__(self):
        """
        Retorna uma string representando o funcionário.

        Returns
        -------
        str
            Representação do funcionário com nome e cargo.
        """
        return f"Funcionário: {self.nome}, Cargo: {self.cargo}"


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