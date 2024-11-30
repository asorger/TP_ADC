class Leitor:
    """
    Representa um leitor de biblioteca com nome, idade e email.

    Atributos
    ---------
    nome : str
        Nome do leitor.
    idade : int
        Idade do leitor.
    email : str
        Endereço de email do leitor.

    Exemplos
    --------
    Criando um novo leitor:

    >>> leitor = Leitor("Ana", 25, "ana@email.com")
    >>> print(leitor)
    Leitor: Ana, Idade: 25, Email: ana@email.com
    """

    def __init__(self, nome, idade, email):
        """
        Inicializa uma nova instância de `Leitor` sem um ID.

        Parâmetros
        ----------
        nome : str
            Nome do leitor.
        idade : int
            Idade do leitor.
        email : str
            Endereço de email do leitor.
        """
        self.nome = nome
        self.idade = idade
        self.email = email

    def __str__(self):
        """
        Retorna uma representação em formato de string do objeto `Leitor`.

        Retorna
        -------
        str
            Uma string contendo o nome, idade e email do leitor.
        """
        return f"Leitor: {self.nome}, Idade: {self.idade}, Email: {self.email}"



def cria_novo_leitor():
    """
    Cria uma nova instância de `Leitor` a partir de entradas do usuário.

    Retorna
    -------
    Leitor
        Um novo objeto `Leitor` com os dados fornecidos (nome, idade e email).

    Exemplos
    --------
    >>> leitor = cria_novo_leitor()
    Nome do leitor: João
    Idade do leitor: 22
    Email do leitor: joao@email.com
    >>> print(leitor)
    ID: 1, Leitor: João, Idade: 22, Email: joao@email.com
    """
    nome = input("Nome do leitor: ")
    idade = int(input("Idade do leitor: "))
    email = input("Email do leitor: ")
    return Leitor(nome, idade, email)


def imprime_lista_de_leitores(leitores):
    """
    Imprime os detalhes de todas as instâncias de `Leitor` em uma lista.

    Parâmetros
    ----------
    leitores : list of Leitor
        Uma lista de objetos `Leitor` a serem impressos.

    Exemplos
    --------
    >>> leitores = [Leitor("Maria", 35, "maria@email.com"), Leitor("José", 40, "jose@email.com")]
    >>> imprime_lista_de_leitores(leitores)
    Lista de Leitores:
    ID: 1, Leitor: Maria, Idade: 35, Email: maria@email.com
    ID: 2, Leitor: José, Idade: 40, Email: jose@email.com
    """
    print("Lista de Leitores:")
    for leitor in leitores:
        print(leitor)
