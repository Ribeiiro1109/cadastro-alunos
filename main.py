from banco import criar_tabela, listar_alunos

criar_tabela()

alunos = listar_alunos()

for aluno in alunos:
    print(f"ID: {aluno[0]} | Nome: {aluno[1]} | Idade: {aluno[2]} | Curso: {aluno[3]}")
