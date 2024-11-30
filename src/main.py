from emprestimos import cria_novo_emprestimo, imprime_lista_de_emprestimos,Emprestimo
from funcionarios import cria_novo_funcionario, imprime_lista_de_funcionarios,Funcionario
from io_ficheiros import (carrega_as_listas_dos_ficheiros,
                          guarda_as_listas_em_ficheiros)
from leitores import cria_novo_leitor, imprime_lista_de_leitores,Leitor
from livros import cria_novo_livro, imprime_lista_de_livros,Livro

def menu():
    """
    Função que exibe um menu interativo para gerenciar uma biblioteca com funcionalidades de cadastro de livros,
    leitores, funcionários e empréstimos, além de permitir listar, guardar e carregar dados. O menu oferece opções
    para realizar operações como registrar novos itens, visualizar as listas e gerenciar os empréstimos.

    A função entra em um loop infinito exibindo um menu com opções de ações. O usuário pode escolher entre as
    seguintes opções: registrar novos leitores, livros ou funcionários, fazer novos empréstimos, listar os dados
    registrados e carregar ou salvar as listas de objetos.

    O menu continua executando até que o usuário escolha a opção de sair.

    Parameters
    ----------
    Nenhum parâmetro externo é passado para esta função. Ela manipula internamente as listas de livros, leitores,
    funcionários e empréstimos, e interage com outras funções para gerenciar esses dados.

    Returns
    -------
    Nenhum. A função não retorna valores, pois seu objetivo é proporcionar uma interface interativa com o usuário
    para a gestão da biblioteca.

    Operations Available in the Menu:
    ----------------------------------
    - `ne`: Novo Empréstimo
    - `nlv`: Novo Livro
    - `nlt`: Novo Leitor
    - `nf`: Novo Funcionário
    - `llv`: Listagem de Livros
    - `llt`: Listagem de Leitores
    - `lf`: Listagem de Funcionários
    - `le`: Listagem de Empréstimos
    - `g`: Guarda todos os dados em arquivos
    - `c`: Carrega todos os dados de arquivos
    - `x`: Sair

    Ações realizadas com base na escolha do usuário:
    -------------------------------------------------
    - `ne`: Cria um novo empréstimo, associando um leitor, um livro e um funcionário.
    - `nlv`: Permite a criação de um novo livro a ser adicionado ao catálogo.
    - `nlt`: Permite a criação de um novo leitor para o cadastro na biblioteca.
    - `nf`: Registra um novo funcionário, incluindo cargos e funções.
    - `llv`, `llt`, `lf`, `le`: Exibe as listas de livros, leitores, funcionários ou empréstimos, respectivamente.
    - `g`: Salva os dados atuais das listas em arquivos persistentes.
    - `c`: Carrega os dados previamente salvos de arquivos.

    Example
    --------
    >>> menu()
    (O menu será exibido e o usuário poderá interagir com as opções, realizando ações como registrar um novo livro,
    adicionar um leitor, fazer um empréstimo, etc. O processo continua até que o usuário selecione 'x' para sair.)

    Notes
    -----
    - O menu se repete indefinidamente até que o usuário selecione a opção para sair ('x').
    - Funções auxiliares como `guarda_as_listas_em_ficheiros`, `carrega_as_listas_dos_ficheiros`, `cria_novo_leitor`, 
      `cria_novo_livro`, `cria_novo_funcionario`, `cria_novo_emprestimo`, `imprime_lista_de_leitores`, 
      `imprime_lista_de_livros`, `imprime_lista_de_funcionarios`, `imprime_lista_de_emprestimos` são chamadas 
      dentro do menu para manipular os dados.
    """
    
    lista_de_livros = []
    lista_de_leitores = []
    lista_de_emprestimos = []
    lista_de_funcionarios = []

    leitor1 = Leitor(nome="João Silva", idade=30, email="joao.silva@email.com")
    leitor2 = Leitor(nome="Maria Oliveira", idade=25, email="maria.oliveira@email.com")

    livro1 = Livro(titulo="O Senhor dos Anéis", autor="J.R.R. Tolkien", ano_publicacao=1954)
    livro2 = Livro(titulo="1984", autor="George Orwell", ano_publicacao=1949)

    funcionario1 = Funcionario(nome="Carlos Pereira", cargo="Bibliotecário")
    funcionario2 = Funcionario(nome="Fernanda Costa", cargo="Assistente Administrativo")

    emprestimo1 = Emprestimo(leitor=leitor1, livro=livro1, funcionario=funcionario1, data_emprestimo="2024-11-01", data_devolucao="2024-12-01")
    emprestimo2 = Emprestimo(leitor=leitor2, livro=livro2, funcionario=funcionario2, data_emprestimo="2024-11-05", data_devolucao="2024-12-05")


    lista_de_livros.append(livro1)
    lista_de_livros.append(livro2)

    lista_de_leitores.append(leitor1)
    lista_de_leitores.append(leitor2)

    lista_de_funcionarios.append(funcionario1)
    lista_de_funcionarios.append(funcionario2)

    lista_de_emprestimos.append(emprestimo1)
    lista_de_emprestimos.append(emprestimo2)


    while True:
        print(""" 
        *********************************************************************
        :                       BIBLIOTECA TECA-TECA                        :
        *********************************************************************
        :                                                                   :
        : ne  - novo emprestimo      le  - listagem de emprestimos          :
        : nlv - novo livro           llv - listagem de livros               :
        : nlt - novo leitor          llt - listagem de leitores             :
        : ...                                                               :
        : nf  - novo funcionário     lf - listagem de funcionários          :
        : ...                                                               :
        : g - guarda tudo            c - carrega tudo                       :
        : x - sair                                                          :
        :                                                                   :
        *********************************************************************
        """)

        op = input("opcao?").lower()

        if op == "x":
            exit()

        elif op == "g":
            guarda_as_listas_em_ficheiros(lista_de_livros, lista_de_leitores, lista_de_emprestimos, lista_de_funcionarios)

        elif op == "c":
            lista_de_livros, lista_de_leitores, lista_de_emprestimos, lista_de_funcionarios = carrega_as_listas_dos_ficheiros()

        elif op == "nlt":
            novo_leitor = cria_novo_leitor()
            if novo_leitor is not None:
                lista_de_leitores.append(novo_leitor)

        elif op == "nlv":
            novo_livro = cria_novo_livro()
            if novo_livro is not None:
                lista_de_livros.append(novo_livro)

        elif op == "nf":
            novo_funcionario = cria_novo_funcionario()
            if novo_funcionario is not None:
                lista_de_funcionarios.append(novo_funcionario)

        elif op == "ne":
            if len(lista_de_leitores) == 0 or len(lista_de_livros) == 0 or len(lista_de_funcionarios) == 0:
                print("Não há leitores ou funcionarios ou livros registados...")
                continue

            novo_emprestimo = cria_novo_emprestimo(lista_de_leitores, lista_de_livros, lista_de_funcionarios)
            lista_de_emprestimos.append(novo_emprestimo)

        elif op == "llt":
            imprime_lista_de_leitores(lista_de_leitores)
            

        elif op == "llv":
            imprime_lista_de_livros(lista_de_livros)

        elif op == "lf":
            imprime_lista_de_funcionarios(lista_de_funcionarios)

        elif op == "le":
            imprime_lista_de_emprestimos(lista_de_emprestimos)

if __name__ == "__main__":
    
    menu()
