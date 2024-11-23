class Leitor:
    """
    Representa um leitor de biblioteca com um ID gerado automaticamente.

    Atributos
    ---------
    ultimo_id : int
        Controla o último ID atribuído a qualquer instância de `Leitor`.
    id : int
        Identificador único de cada instância de `Leitor`.
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
    ID: 1, Leitor: Ana, Idade: 25, Email: ana@email.com
    """

    ultimo_id = 0

    def __init__(self, nome, idade, email):
        """
        Inicializa uma nova instância de `Leitor` com um ID único.

        Parâmetros
        ----------
        nome : str
            Nome do leitor.
        idade : int
            Idade do leitor.
        email : str
            Endereço de email do leitor.
        """
        Leitor.ultimo_id += 1
        self.id = Leitor.ultimo_id
        self.nome = nome
        self.idade = idade
        self.email = email

    def __str__(self):
        """
        Retorna uma representação em formato de string do objeto `Leitor`.

        Retorna
        -------
        str
            Uma string contendo o ID, nome, idade e email do leitor.
        """
        return f"ID: {self.id}, Leitor: {self.nome}, Idade: {self.idade}, Email: {self.email}"


def cria_novo_leitor():
    """
    Cria uma nova instância de `Leitor` a partir de entradas do usuário.

    Retorna
    -------
    Leitor
        Um novo objeto `Leitor` com os dados fornecidos (nome, idade e email).

    Exemplos
    --------
    Supondo que o usuário insira os seguintes dados:
    Nome: João
    Idade: 22
    Email: joao@email.com

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
