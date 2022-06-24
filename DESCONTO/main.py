n = 1
contas = [[], [], []]
descontoTtl = 0
precoComDesconto = 0

while n == 1:
    preco = int(input("qual é o preço total da sua compra: "))

    if preco >= 350:
        descontoTtl += 0.1

        maisDesconto = preco - 350
        while maisDesconto >= 100:
            maisDesconto -= 100
            descontoTtl += 0.1

        print(descontoTtl)

    cadastrada = input('Você tem uma conta cadastrada: ')
    if cadastrada.upper() == "SIM":
        cpf = input("qual é o seu cpf: ")

        if cpf in contas[0]:
            print('bem vindo')

            usario = contas[0].index(cpf)
            descontoGuarda = contas[1][usario]
            todoCompra = contas[2][usario]

            typoDeDesconto = input(
                "Selecione alguma opção para desconto\n1 para desconto imediato\n2 para desconto guardado")

            while typoDeDesconto != "1" or typoDeDesconto != "2":
                print("Opção inválida!")
                typoDeDesconto = input(
                    "Selecione alguma opção para desconto\n1 para desconto imediato\n2 para desconto guardado")

            if typoDeDesconto == "2":
                precoComDesconto = preco - preco * \
                    (descontoTtl + descontoGuarda)
            elif typoDeDesconto == "1":
                precoComDesconto = preco - preco * descontoTtl

        else:
            print('Nao ta no conta')
    # Cadastra Uma CONTA
    else:
        querConta = input("você deseja criar uma conta")
        if querConta.upper() == "SIM":
            cpf = input("qual é o seu cpf: ")
            contas[0].append(cpf)
            contas[1].append(0)
            contas[1].append(0)

            typoDeDesconto = input(
                "Selecione alguma opção para desconto\n1 para desconto imediato\n2 para desconto guardado")
            print(type(typoDeDesconto))
            while typoDeDesconto != "1" and typoDeDesconto != "2":
                print("Opção inválida!")
                typoDeDesconto = input(
                    "Selecione alguma opção para desconto\n1 para desconto imediato\n2 para desconto guardado")

            if typoDeDesconto == "2":
                precoComDesconto = preco - preco * \
                    (descontoTtl + descontoGuarda)
            elif typoDeDesconto == "1":
                precoComDesconto = preco - preco * descontoTtl
        else:
            precoComDesconto = preco

    print('paga : ', precoComDesconto)
