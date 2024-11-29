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
