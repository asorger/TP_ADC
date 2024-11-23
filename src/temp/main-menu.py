def menu():
    """
    Função que exibe um menu interativo para gerenciar uma biblioteca com funcionalidades de cadastro de livros,
    leitores, funcionários e empréstimos, além de permitir listar, guardar e carregar dados.

    A função entra em um loop infinito exibindo um menu com opções de ações. O usuário pode escolher entre as
    seguintes opções: registrar novos leitores, livros ou funcionários, fazer novos empréstimos, listar os dados
    registrados e carregar ou salvar as listas de objetos.

    O menu continua executando até que o usuário escolha a opção de sair.

    This function does not return any value. It uses other functions to handle the actual data management.

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

    Parameters
    ----------
    None

    Returns
    -------
    None
        A função não retorna nada, pois o objetivo é exibir um menu interativo para o usuário.
        
    Examples
    --------
    >>> menu()
    (Exibe o menu e aguarda a interação do usuário. A função continua até o usuário escolher 'x' para sair.)
    
    Notes
    -----
    - O menu se repete indefinidamente até que o usuário selecione a opção para sair ('x').
    - Funções auxiliares como `guarda_as_listas_em_ficheiros`, `carrega_as_listas_dos_ficheiros`, `cria_novo_leitor`,
      `cria_novo_livro`, `cria_novo_funcionario`, `cria_novo_emprestimo`, `imprime_lista_de_leitores`, `imprime_lista_de_livros`,
      `imprime_lista_de_funcionarios`, `imprime_lista_de_emprestimos` e `pausa` são chamadas dentro do menu, mas não estão
      incluídas na implementação deste código.
    """
    
    lista_de_livros = []
    lista_de_leitores = []
    lista_de_emprestimos = []
    lista_de_funcionarios = []

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
            pausa()

        elif op == "llv":
            imprime_lista_de_livros(lista_de_livros)
            pausa()

        elif op == "lf":
            imprime_lista_de_funcionarios(lista_de_funcionarios)
            pausa()

        elif op == "le":
            imprime_lista_de_emprestimos(lista_de_emprestimos)
            pausa()

if __name__ == "__main__":
    menu()
