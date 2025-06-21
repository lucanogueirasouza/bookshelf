print (
    "=== PRATELEIRA DE LIVROS ==="
)

livros = []

def adicionar_Livro(): 
    global livros 

    livro = str(input(
        "Digite o nome do livro: "
    )).strip().capitalize()
    livros.append(livro)
    print (
        f"Livro: '{livro}', Adicionado com sucesso!"
    )
    
def remover_livro(): 
    global livros
    try: 
        indice_remover_livro = int(input(
            "Digite o indice do livro que deseja retirar: "
        ))
        print (
            f"Livro: '{livros[indice_remover_livro - 1]}', Removido com sucesso!"
        )
        livros.pop(indice_remover_livro - 1)

    except ValueError: 
        print (
            "Aceitamos apenas numeros neste local. "
        )
        return None 
    
def mostrar_livros(): 
    global livros
    for numero, livro in enumerate(livros): 
        print (
            f"{numero + 1}) {livro}"
        )

while True: 
    try: 
        escolha = int(input(
            "[1] - Adicionar Livro(s)\n" \
            "[2] - Remover Livro(s)\n" \
            "[3] - Mostrar Livro(s)\n" \
            "[4] - Sair\n" \
            "Escolha: "
        ))

        if escolha < 1 or escolha > 4: 
            print (
                "Escolha um valor de '1-4'. Tente Novamente."
            )
            continue

    except ValueError: 
        print (
            "Escolha um valor válido. "
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