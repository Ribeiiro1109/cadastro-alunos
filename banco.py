import sqlite3


def conectar():
    return sqlite3.connect("alunos.db")


def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            curso TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()


def cadastrar_aluno(nome, idade, curso):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO alunos (nome, idade, curso) VALUES (?, ?, ?)", (nome, idade, curso)
    )
    conexao.commit()
    conexao.close()


def listar_alunos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, idade, curso FROM alunos")
    alunos = cursor.fetchall()
    conexao.close()
    return alunos


def buscar_aluno(id_aluno):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT id, nome, idade, curso FROM alunos WHERE id = ?", (id_aluno,)
    )
    aluno = cursor.fetchone()
    conexao.close()
    return aluno


def atualizar_aluno(id_aluno, nome, idade, curso):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE alunos SET nome = ?, idade = ?, curso = ? WHERE id = ?",
        (nome, idade, curso, id_aluno),
    )
    conexao.commit()
    conexao.close()


def excluir_aluno(id_aluno):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM alunos WHERE id = ?", (id_aluno,))
    conexao.commit()
    conexao.close()
