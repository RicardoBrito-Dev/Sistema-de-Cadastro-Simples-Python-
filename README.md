# Sistema de Cadastro Simples

Este é um sistema de cadastro de usuários simples desenvolvido em Python que utiliza SQLite para persistência de dados. O projeto opera através de uma interface de linha de comando (CLI), permitindo cadastrar, listar, atualizar e remover usuários.

## Funcionalidades

O sistema oferece as seguintes opções através de um menu interativo:

1.  **Cadastrar Usuário**: Adiciona um novo usuário informando nome, email e idade.
2.  **Listar Usuários**: Exibe todos os usuários cadastrados no banco de dados.
3.  **Atualizar Usuário**: Permite modificar os dados de um usuário existente através do seu ID.
4.  **Deletar Usuário**: Remove um usuário do sistema pelo seu ID.

## Pré-requisitos

- Python 3.x instalado.

## Como Executar

1.  Certifique-se de estar na pasta do projeto no seu terminal.
2.  Execute o arquivo principal:

    ```bash
    python main.py
    ```

3.  O banco de dados `app_data.db` será criado automaticamente na primeira execução se não existir.

## Estrutura do Projeto

- `main.py`: Arquivo principal contendo a lógica da interface do usuário e o loop do aplicativo.
- `database.py`: Módulo responsável pelas operações de banco de dados (SQLite).
- `app_data.db`: Arquivo do banco de dados SQLite (gerado automaticamente).
