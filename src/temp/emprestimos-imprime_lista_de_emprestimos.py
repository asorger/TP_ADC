def imprime_lista_de_emprestimos(lista_de_emprestimos):
    for emprestimo in lista_de_emprestimos:
        leitor_id = emprestimo["leitor"]
        livro_id = emprestimo["livro"]
        funcionario_id = emprestimo["funcionario"]
        data_emprestimo = emprestimo["data_emprestimo"]
        data_devolucao = emprestimo["data_devolucao"]
        
        print(f"Empréstimo: Leitor ID {leitor_id}, Livro ID {livro_id}, Funcionário ID {funcionario_id}")
        print(f"Data de Empréstimo: {data_emprestimo}")
        print(f"Data de Devolução: {data_devolucao}")
        print("-" * 50)