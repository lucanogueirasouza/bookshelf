print(
    "=== PRATELEIRA DE LIVROS ==="
)

livros = []

def adicionar_Livro():
    global livros

    nome = str(input(
        "Digite o nome do livro: "
        )).strip().capitalize()
    
    autor = str(input(
        "Digite o nome do autor do livro: "
        )).strip().capitalize()
    
    ano = int(input(
        "Digite o ano de lançamento do livro: "
        ))

    livro = {
        "Nome": nome,
        "Autor": autor,
        "Ano": ano,
    }

    livros.append(livro)

    print(
        f"Livro: '{livro['Nome']}', Adicionado com sucesso!"
        )

def remover_livro():
    global livros
    try:
        indice_remover_livro = int(input(
            "Digite o índice do livro que deseja retirar: "
            ))
        
        livro_removido = livros.pop(indice_remover_livro - 1)

        print(
            f"Livro: '{livro_removido['Nome']}', Removido com sucesso!"
            )
        
    except (ValueError, IndexError):
        print(
            "Valor inválido."
            )

def mostrar_livros():
    global livros
    if not livros:
        print(
            "Nenhum livro adicionado ainda."
            )
        return None

    for numero, livro in enumerate(livros):
        print(
            f"{numero + 1}) {livro['Nome']} | Autor: {livro['Autor']} | Ano: {livro['Ano']}"
            )

while True:
    try:
        escolha = int(input(
            "[1] - Adicionar Livro(s)\n"
            "[2] - Remover Livro(s)\n"
            "[3] - Mostrar Livro(s)\n"
            "[4] - Sair\n"
            "Escolha: "
        ))

        if escolha < 1 or escolha > 4:
            print("Escolha um valor de '1-4'. Tente novamente.")
            continue

    except ValueError:
        print(
            "Escolha um valor válido."
            )
        continue

    if escolha == 1:
        adicionar_Livro()
    elif escolha == 2:
        remover_livro()
    elif escolha == 3:
        mostrar_livros()
    elif escolha == 4:
        break
