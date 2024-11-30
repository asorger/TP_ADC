import json
import os
from leitores import Leitor
from emprestimos import Emprestimo
from livros import Livro
from funcionarios import Funcionario

def guarda_as_listas_em_ficheiros(livros: list, leitores: list, emprestimos: list , funcionarios: list) -> None:
    """
    Salva listas de livros, leitores, empréstimos e funcionários em arquivos JSON.

    Esta função serializa objetos das listas fornecidas e os armazena nos 
    respectivos arquivos JSON: `livros.json`, `leitores.json`, `emprestimos.json` 
    e `funcionarios.json` que se encontram dentro da pasta `save`.
    Se a pasta `save` não existir, será criada.

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
    if not os.path.exists('save'):
        os.makedirs('save')


    with open('save/livros.json', 'w') as f:
        json.dump([livro.__dict__ for livro in livros], f)

    with open('save/leitores.json', 'w') as f:
        json.dump([leitor.__dict__ for leitor in leitores], f)

    with open('save/emprestimos.json', 'w') as f:
        json.dump([emprestimo.to_dict() for emprestimo in emprestimos], f)

    with open('save/funcionarios.json', 'w') as f:
        json.dump([funcionario.__dict__ for funcionario in funcionarios], f)

    print("Dados salvos com sucesso!")

import json

def carrega_as_listas_dos_ficheiros():
    """
    Carrega listas de livros, leitores, empréstimos e funcionários a partir de arquivos JSON.
    """
    try:
        with open('save/livros.json', 'r') as f:
            livros_data = json.load(f)
            livros = [Livro(**livro) for livro in livros_data]
    except FileNotFoundError:
        livros = []

    try:
        with open('save/leitores.json', 'r') as f:
            leitores_data = json.load(f)
            leitores = []
            ultimo_id_leitor = 0  # Controle manual de IDs
            for leitor_data in leitores_data:
                ultimo_id_leitor += 1  # Incrementa o ID manualmente
                leitor = Leitor(leitor_data["nome"], leitor_data["idade"], leitor_data["email"])
                leitores.append(leitor)
    except FileNotFoundError:
        leitores = []

    try:
        with open('save/emprestimos.json', 'r') as f:
            emprestimos_data = json.load(f)
            emprestimos = []
            for emprestimo_data in emprestimos_data:
                # Ajuste: não passamos o 'id' para o construtor de Funcionario
                leitor = Leitor(emprestimo_data['leitor']['nome'], emprestimo_data['leitor']['idade'], emprestimo_data['leitor']['email'])
                livro = Livro(**emprestimo_data['livro'])
                # Ajuste: Cria o Funcionario com nome e cargo, sem passar o 'id'
                funcionario = Funcionario(emprestimo_data['funcionario']['nome'], emprestimo_data['funcionario']['cargo'])
                emprestimos.append(Emprestimo(leitor, livro, funcionario, emprestimo_data['data_emprestimo'], emprestimo_data['data_devolucao']))
    except FileNotFoundError:
        emprestimos = []

    try:
        with open('save/funcionarios.json', 'r') as f:
            funcionarios_data = json.load(f)
            funcionarios = []
            ultimo_id_funcionario = 0  
            for funcionario_data in funcionarios_data:
                ultimo_id_funcionario += 1 
                funcionario = Funcionario(funcionario_data["nome"], funcionario_data["cargo"])
                funcionarios.append(funcionario)
    except FileNotFoundError:
        funcionarios = []

    return livros, leitores, emprestimos, funcionarios
