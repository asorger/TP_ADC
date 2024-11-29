# Biblioteca Teca-Teca

Este projeto é uma aplicação em Python para gerenciar uma biblioteca, permitindo o cadastro e a listagem de livros, leitores, funcionários e empréstimos. O programa também permite salvar e carregar os dados de arquivos.

## Tabela de conteúdos
- [Biblioteca Teca-Teca](#biblioteca-teca-teca)
  - [Tabela de conteúdos](#tabela-de-conteúdos)
  - [Funcionalidades](#funcionalidades)
  - [Estrutura do Projeto](#estrutura-do-projeto)
  - [Como executar](#como-executar)
  - [Exemplos de uso](#exemplos-de-uso)
    - [Cadastre de um novo livro](#cadastre-de-um-novo-livro)
    - [Listagem de leitores](#listagem-de-leitores)
  - [Melhorias futuras](#melhorias-futuras)


## Funcionalidades

- **Cadastro**:
  - Novo livro
  - Novo leitor
  - Novo funcionário
  - Novo empréstimo (vinculado a leitores, livros e funcionários já cadastrados)

- **Listagem**:
  - Listagem de livros
  - Listagem de leitores
  - Listagem de funcionários
  - Listagem de empréstimos

- **Gerenciamento de Arquivos**:
  - Salvar dados em arquivos
  - Carregar dados de arquivos

- **Outras Funcionalidades**:
  - Menu interativo
  - Saída do programa

## Estrutura do Projeto

```plaintext
src/
├── main.py           # Arquivo principal que contém o menu interativo
├── emprestimos.py    # Funções relacionadas aos empréstimos
├── funcionarios.py   # Funções relacionadas aos funcionários
├── io_ficheiros.py   # Funções para salvar e carregar dados de arquivos
├── leitores.py       # Funções relacionadas aos leitores
└── livros.py         # Funções relacionadas aos livros
```

## Como executar

1. Certifique-se de que você tem o Python 3 instalado na sua máquina.
2. Clone este repositório ou baixe os arquivos.
3. Instale os requirments necessários para o funcionamento do programa com o seguinte comando:
   ```bash
   pip install -r requirements.txt
   ```
4. Navegue até o dirétorio do projeto no terminal
5. Execute o programa com o seguinte comando:
    
    ```bash
    python main.py
    ```
6. Siga as instruções no menu para gerenciar a biblioteca.

>[!CAUTION]
> Python 3.8 ou superior é necessário para o funcionamento do programa.
## Exemplos de uso

### Cadastre de um novo livro

1. Selecione a opção `nlv` no menu.
2. Siga as instruções para inserir os dados no livro.
3. O livro será adicionado à lista e estará disponível para empréstimos.
   
### Listagem de leitores

1. Selecione a opção `llt` no menu.
2. A lista de leitores registrados será exibida no terminal.

>[!NOTE]
> - O programa utiliza listas em memória para gerenciar os dados.
> - Ao sair do programa sem salvar (`g`), os dados não serão mantidos.
> - Para garantir a presitência dos dados, utilize as opções de salvar (`g`) e carregar (`c`).

## Melhorias futuras

- Implementar uma interface gráfica.
- Adicionar suporte para uma base de dados para maior robustez.
- Melhorar a validação de dados no momento do cadastro.

>[!IMPORTANT]
> Estas funcionalidades e melhorias ainda não se encontram desenvolvidas nesta versão inicial do programa.