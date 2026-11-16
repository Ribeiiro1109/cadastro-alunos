from banco import (
    criar_tabela,
    cadastrar_aluno,
    listar_alunos,
    buscar_aluno,
    atualizar_aluno,
    excluir_aluno,
)


def menu():
    print("\n=== CADASTRO DE ALUNOS ===")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Editar aluno")
    print("4 - Excluir aluno")
    print("0 - Sair")
    return input("Escolha uma opção: ")


def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto and not texto.isdigit():
            return texto
        print("Valor inválido! Digite um texto não vazio e que não seja só números.")


def ler_idade():
    while True:
        try:
            idade = int(input("Idade: "))
            if 0 < idade < 120:
                return idade
            print("Digite uma idade entre 1 e 119.")
        except ValueError:
            print("Idade inválida! Digite apenas números.")


def cadastrar():
    nome = ler_texto("Nome: ")
    idade = ler_idade()
    curso = ler_texto("Curso: ")
    cadastrar_aluno(nome, idade, curso)
    print("Aluno cadastrado com sucesso!")


def listar():
    alunos = listar_alunos()
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    for aluno in alunos:
        print(
            f"ID: {aluno[0]} | Nome: {aluno[1]} | Idade: {aluno[2]} | Curso: {aluno[3]}"
        )


def ler_id():
    while True:
        try:
            return int(input("ID do aluno: "))
        except ValueError:
            print("ID inválido! Digite apenas números.")


def editar():
    id_aluno = ler_id()
    aluno = buscar_aluno(id_aluno)
    if aluno is None:
        print("Aluno não encontrado.")
        return
    print(f"Editando: {aluno[1]} | {aluno[2]} anos | {aluno[3]}")
    nome = ler_texto("Novo nome: ")
    idade = ler_idade()
    curso = ler_texto("Novo curso: ")
    atualizar_aluno(id_aluno, nome, idade, curso)
    print("Aluno atualizado com sucesso!")


def excluir():
    id_aluno = ler_id()
    aluno = buscar_aluno(id_aluno)
    if aluno is None:
        print("Aluno não encontrado.")
        return
    confirmacao = input(f"Excluir {aluno[1]}? (s/n): ").strip().lower()
    if confirmacao == "s":
        excluir_aluno(id_aluno)
        print("Aluno excluído com sucesso!")
    else:
        print("Operação cancelada.")


def main():
    criar_tabela()
    while True:
        opcao = menu()
        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            editar()
        elif opcao == "4":
            excluir()
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
