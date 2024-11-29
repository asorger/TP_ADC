import json

def guarda_as_listas_em_ficheiros(livros: list, leitores: list, emprestimos: list , funcionarios: list) -> None:
    """
    Salva listas de livros, leitores, empréstimos e funcionários em arquivos JSON.

    Esta função serializa objetos das listas fornecidas e os armazena nos 
    respectivos arquivos JSON: `livros.json`, `leitores.json`, `emprestimos.json` 
    e `funcionarios.json`.

    Parâmetros
    ----------
    livros : list of Livro
        Lista de objetos da classe `Livro` a serem salvos.
    leitores : list of Leitor
        Lista de objetos da classe `Leitor` a serem salvos.
    emprestimos : list of Emprestimo
        Lista de objetos da classe `Emprestimo` a serem salvos.
    funcionarios : list of Funcionario
        Lista de objetos da classe `Funcionario` a serem salvos.

    Returns
    -------
    None

    Exemplos
    --------
    >>> livros = [Livro("Dom Quixote", "Miguel de Cervantes", "1605")]
    >>> leitores = [Leitor("Ana", "123456789")]
    >>> emprestimos = [Emprestimo("123", "Dom Quixote", "2024-11-01")]
    >>> funcionarios = [Funcionario("João", "Bibliotecário")]
    >>> guarda_as_listas_em_ficheiros(livros, leitores, emprestimos, funcionarios)
    Dados salvos com sucesso!
    """
    with open('livros.json', 'w') as f:
        json.dump([livro.__dict__ for livro in livros], f)

    with open('leitores.json', 'w') as f:
        json.dump([leitor.__dict__ for leitor in leitores], f)

    with open('emprestimos.json', 'w') as f:
        json.dump([emprestimo.__dict__ for emprestimo in emprestimos], f)

    with open('funcionarios.json', 'w') as f:
        json.dump([funcionario.__dict__ for funcionario in funcionarios], f)

    print("Dados salvos com sucesso!")

def carrega_as_listas_dos_ficheiros():
    """
    Carrega listas de livros, leitores, empréstimos e funcionários a partir de arquivos JSON.

    Esta função lê os dados dos arquivos `livros.json`, `leitores.json`, 
    `emprestimos.json` e `funcionarios.json`, recriando as listas correspondentes 
    a partir das informações armazenadas. Caso algum arquivo não seja encontrado, 
    retorna uma lista vazia para aquele tipo de dado.

    Returns
    -------
    tuple
        Uma tupla contendo quatro listas:
        - livros : list of Livro
            Lista de objetos da classe `Livro` carregados do arquivo.
        - leitores : list of Leitor
            Lista de objetos da classe `Leitor` carregados do arquivo.
        - emprestimos : list of Emprestimo
            Lista de objetos da classe `Emprestimo` carregados do arquivo.
        - funcionarios : list of Funcionario
            Lista de objetos da classe `Funcionario` carregados do arquivo.

    Exemplos
    --------
    >>> livros, leitores, emprestimos, funcionarios = carrega_as_listas_dos_ficheiros()
    >>> print(len(livros))
    10  # Supondo que havia 10 livros armazenados.
    >>> print(len(leitores))
    5   # Supondo que havia 5 leitores armazenados.
    """
    try:
        with open('livros.json', 'r') as f:
            livros_data = json.load(f)
            livros = [Livro(**livro) for livro in livros_data]
    except FileNotFoundError:
        livros = []

    try:
        with open('leitores.json', 'r') as f:
            leitores_data = json.load(f)
            leitores = [Leitor(**leitor) for leitor in leitores_data]
    except FileNotFoundError:
        leitores = []

    try:
        with open('emprestimos.json', 'r') as f:
            emprestimos_data = json.load(f)
            emprestimos = [Emprestimo(**emprestimo) for emprestimo in emprestimos_data]
    except FileNotFoundError:
        emprestimos = []

    try:
        with open('funcionarios.json', 'r') as f:
            funcionarios_data = json.load(f)
            funcionarios = [Funcionario(**funcionario) for funcionario in funcionarios_data]
    except FileNotFoundError:
        funcionarios = []

    return livros, leitores, emprestimos, funcionarios
