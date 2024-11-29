class Livro:
    """
    Classe que representa um livro com título, autor e ano de publicação.

    Atributos de instância
    -----------------------
    titulo : str
        Título do livro.
    autor : str
        Autor do livro.
    ano_publicacao : str
        Ano de publicação do livro.

    Métodos
    -------
    __str__()
        Retorna uma representação em string do livro.

    Exemplos
    --------
    >>> livro1 = Livro("Dom Quixote", "Miguel de Cervantes", "1605")
    >>> livro2 = Livro("Orgulho e Preconceito", "Jane Austen", "1813")
    >>> print(livro1)
    Livro: Dom Quixote, Autor: Miguel de Cervantes, Ano: 1605
    >>> print(livro2)
    Livro: Orgulho e Preconceito, Autor: Jane Austen, Ano: 1813
    """
    def __init__(self, titulo: str, autor: str, ano_publicacao: str):
        """
        Inicializa uma nova instância da classe Livro.

        Parâmetros
        ----------
        titulo : str
            Título do livro.
        autor : str
            Autor do livro.
        ano_publicacao : str
            Ano de publicação do livro.
        """
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def __str__(self):
        """
        Retorna uma string representando o livro.

        Returns
        -------
        str
            Representação do livro com título, autor e ano de publicação.
        """
        return f"Livro: {self.titulo}, Autor: {self.autor}, Ano: {self.ano_publicacao}"

def cria_novo_livro():
    """
    Cria um novo livro solicitando título, autor e ano de publicação ao usuário.

    Returns
    -------
    Livro
        Objeto `Livro` criado com os dados fornecidos pelo usuário.

    Exemplos
    --------
    >>> livro = cria_novo_livro()
    Título do livro: Dom Quixote
    Autor do livro: Miguel de Cervantes
    Ano de publicação do livro: 1605
    >>> print(livro)
    Livro: Dom Quixote, Autor: Miguel de Cervantes, Ano: 1605
    """
    titulo = input("Título do livro: ")
    autor = input("Autor do livro: ")
    ano_publicacao = int(input("Ano de publicação do livro: "))
    return Livro(titulo, autor, ano_publicacao)
