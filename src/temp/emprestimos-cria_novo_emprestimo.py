from datetime import date

def pergunta_id(questao, lista, mostra_lista=False):
    if mostra_lista:
        print(questao)
        for item in lista:
            print(f"{item['id']}: {item['nome']}")
    id_escolhido = input("Digite o ID desejado: ")
    return int(id_escolhido)

def cria_novo_emprestimo(lista_de_leitores, lista_de_livros, lista_de_funcionarios):
    id_leitor = pergunta_id(questao="Qual o id do leitor?", lista=lista_de_leitores, mostra_lista=True)
    id_livro = pergunta_id(questao="Qual o id do livro?", lista=lista_de_livros, mostra_lista=True)
    id_funcionario = pergunta_id(questao="Qual o id do funcionário?", lista=lista_de_funcionarios, mostra_lista=True)
    data_devolucao = input("Qual a data de devolução do livro? (Formato: YYYY-MM-DD): ")
    try:
        data_devolucao = date.fromisoformat(data_devolucao)
    except ValueError:
        print("Data inválida. Usando a data atual como data de devolução.")
        data_devolucao = date.today()
    
    emprestimo = {
        "leitor": id_leitor,
        "livro": id_livro,
        "funcionario": id_funcionario,
        "data_emprestimo": date.today(),
        "data_devolucao": data_devolucao
    }

    return emprestimo