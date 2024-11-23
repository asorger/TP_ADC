class Emprestimo:
    """
    Classe que representa um empréstimo de livro em uma biblioteca.

    A classe armazena informações sobre o empréstimo de um livro por um leitor, incluindo os detalhes do livro,
    do funcionário responsável e as datas de empréstimo e devolução.

    Attributes
    ----------
    leitor : Leitor
        Objeto da classe Leitor que representa o usuário que fez o empréstimo.
    livro : Livro
        Objeto da classe Livro que representa o livro emprestado.
    funcionario : Funcionario
        Objeto da classe Funcionario que representa o funcionário que processou o empréstimo.
    data_emprestimo : str
        A data em que o empréstimo foi feito (formato: 'YYYY-MM-DD').
    data_devolucao : str
        A data em que o livro deve ser devolvido (formato: 'YYYY-MM-DD').

    Methods
    -------
    __str__():
        Retorna uma string formatada representando o empréstimo com informações do leitor, livro, funcionário e data de devolução.

    cria_novo_emprestimo(leitores, livros, funcionarios):
        Cria e retorna um novo empréstimo, permitindo que o usuário escolha o leitor, livro, funcionário e as datas de empréstimo e devolução.

    imprime_lista_de_emprestimos(emprestimos):
        Imprime uma lista de todos os empréstimos, mostrando suas informações formatadas.
    """

    def __init__(self, leitor, livro, funcionario, data_emprestimo, data_devolucao):
        """
        Constrói uma instância de Emprestimo.

        Parameters
        ----------
        leitor : Leitor
            Objeto da classe Leitor que representa o usuário que fez o empréstimo.
        livro : Livro
            Objeto da classe Livro que representa o livro emprestado.
        funcionario : Funcionario
            Objeto da classe Funcionario que representa o funcionário que processou o empréstimo.
        data_emprestimo : str
            A data em que o empréstimo foi feito (formato: 'YYYY-MM-DD').
        data_devolucao : str
            A data em que o livro deve ser devolvido (formato: 'YYYY-MM-DD').

        """
        self.leitor = leitor
        self.livro = livro
        self.funcionario = funcionario
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao

    def __str__(self):
        """
        Retorna uma string formatada representando o empréstimo.

        Returns
        -------
        str
            String que contém o nome do leitor, título do livro, nome do funcionário e a data de devolução.
        
        Example
        -------
        >>> emprestimo = Emprestimo(leitor, livro, funcionario, "2024-11-22", "2024-12-22")
        >>> print(emprestimo)
        'Empréstimo: João Silva - O Poder do Hábito | Funcionário: Maria Oliveira | Devolução: 2024-12-22'
        """
        return f"Empréstimo: {self.leitor.nome} - {self.livro.titulo} | Funcionário: {self.funcionario.nome} | Devolução: {self.data_devolucao}"

def cria_novo_emprestimo(leitores, livros, funcionarios):
    """
    Cria e retorna um novo empréstimo, permitindo que o usuário escolha o leitor, livro, funcionário e as datas de empréstimo e devolução.

    Parameters
    ----------
    leitores : list of Leitor
        Lista de objetos da classe Leitor, que representam os leitores disponíveis para o empréstimo.
    livros : list of Livro
        Lista de objetos da classe Livro, que representam os livros disponíveis para o empréstimo.
    funcionarios : list of Funcionario
        Lista de objetos da classe Funcionario, que representam os funcionários disponíveis para processar o empréstimo.

    Returns
    -------
    Emprestimo
        Uma nova instância da classe Emprestimo com as escolhas do usuário para o leitor, livro, funcionário e datas.
    
    Example
    -------
    >>> leitores = [leitor1, leitor2]
    >>> livros = [livro1, livro2]
    >>> funcionarios = [funcionario1, funcionario2]
    >>> emprestimo = Emprestimo.cria_novo_emprestimo(leitores, livros, funcionarios)
    'Empréstimo: João Silva - O Poder do Hábito | Funcionário: Maria Oliveira | Devolução: 2024-12-22'
    """
    print("Escolha um leitor:")
    for i, leitor in enumerate(leitores):
        print(f"{i + 1}. {leitor.nome}")
    leitor_index = int(input("Escolha o número do leitor: ")) - 1
    leitor = leitores[leitor_index]

    print("Escolha um livro:")
    for i, livro in enumerate(livros):
        print(f"{i + 1}. {livro.titulo}")
    livro_index = int(input("Escolha o número do livro: ")) - 1
    livro = livros[livro_index]

    print("Escolha um funcionário:")
    for i, funcionario in enumerate(funcionarios):
        print(f"{i + 1}. {funcionario.nome}")
    funcionario_index = int(input("Escolha o número do funcionário: ")) - 1
    funcionario = funcionarios[funcionario_index]

    data_emprestimo = input("Data do empréstimo (dd/mm/yyyy): ")
    data_devolucao = input("Data de devolução (dd/mm/yyyy): ")

    return Emprestimo(leitor, livro, funcionario, data_emprestimo, data_devolucao)


def imprime_lista_de_emprestimos(emprestimos):
    """
    Imprime uma lista de todos os empréstimos, mostrando suas informações formatadas.

    Parameters
    ----------
    emprestimos : list of Emprestimo
        Lista de objetos da classe Emprestimo que representam os empréstimos a serem exibidos.

    Returns
    -------
    None
        A função não retorna nada, apenas imprime a lista de empréstimos no console.

    Example
    -------
    >>> emprestimos = [emprestimo1, emprestimo2]
    >>> imprime_lista_de_emprestimos(emprestimos)
    Lista de Empréstimos:
    Empréstimo: João Silva - O Poder do Hábito | Funcionário: Maria Oliveira | Devolução: 2024-12-22
    Empréstimo: Ana Souza - 1984 | Funcionário: João Lima | Devolução: 2024-11-30
    """
    print("Lista de Empréstimos:")
    for emprestimo in emprestimos:
        print(emprestimo)
