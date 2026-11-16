# Cadastro de Alunos

Sistema de cadastro de alunos em linha de comando, feito em Python com banco de dados SQLite.

## Funcionalidades

- Cadastrar aluno (nome, idade e curso)
- Listar alunos
- Editar aluno
- Excluir aluno, com confirmação
- Validação dos dados digitados

## Tecnologias

- Python 3
- SQLite (biblioteca `sqlite3`, já inclusa no Python)

## Como executar

```bash
git clone https://github.com/Ribeiiro1109/cadastro-alunos.git
cd cadastro-alunos
python main.py
```

O banco `alunos.db` é criado automaticamente na primeira execução.

## Estrutura do projeto

```
cadastro-alunos/
├── banco.py   # acesso ao banco de dados (CRUD)
├── main.py    # menu e interação com o usuário
└── README.md
```

## O que aprendi

- Operações CRUD com SQL
- Consultas parametrizadas, que evitam SQL Injection
- Validação de entrada com try/except
- Separação de responsabilidades entre arquivos e funções
