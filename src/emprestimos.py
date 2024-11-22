from datetime import date
from io_terminal import imprime_lista, pergunta_id
import pickle

nome_ficheiro_lista_de_emprestimos = "lista_de_emprestimos.pk"

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

def salvar_lista_emprestimos(lista_de_emprestimos, nome_ficheiro):
    with open(nome_ficheiro, "wb") as file:
        pickle.dump(lista_de_emprestimos, file)

def carregar_lista_emprestimos(nome_ficheiro):
    try:
        with open(nome_ficheiro, "rb") as file:
            lista_de_emprestimos = pickle.load(file)
    except FileNotFoundError:
        lista_de_emprestimos = []
    return lista_de_emprestimos