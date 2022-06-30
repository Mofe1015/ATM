repeat = True
contas = [[], [], []]

while repeat == True:
    descontoTtl = 0
    precoComDesconto = 0

    preco = int(input("qual é o preço total da sua compra: "))

    if preco >= 350:
        descontoTtl += 0.01

        maisDesconto = preco - 350
        while maisDesconto >= 100 and descontoTtl <= 0.25:
            maisDesconto -= 100
            descontoTtl += 0.01

    print('Voce ganha', int(descontoTtl*100), "%" "de desconto")

    cadastrada = input('Você tem uma conta cadastrada: ')
    if cadastrada.upper() == "SIM":
        cpf = input("qual é o seu cpf: ")

        while cpf not in contas[0]:
            print('\nNao ta no conta')
            cpf = input(
                "\n\nCPF inválido \ntente novamente \nqual é o seu cpf: ")

        if cpf in contas[0]:
            print('Bem Vindo')

            usario = contas[0].index(cpf)

            if contas[2][usario] == 3:
                print("Você tem um desconto automático de 1%")
                preco = preco - preco * 0.01
                contas[2][usario] = 0
            elif descontoTtl > 0:
                contas[2][usario] += 1

            typoDeDesconto = input(
                "Selecione alguma opção para desconto\n1 para desconto imediato\n2 para usar novo deconto com desconto guardado\n3 para guadar esse desconto:\n")

            while typoDeDesconto != "1" and typoDeDesconto != "2" and typoDeDesconto != "3":
                print("Opção inválida!")
                typoDeDesconto = input(
                    "Selecione alguma opção para desconto\n1 para desconto imediato\n2 para usar novo deconto com desconto guardado\n3 para guadar esse desconto:\n")

            if typoDeDesconto == "2":
                tudoDesconto = descontoTtl+contas[1][usario]
                precoComDesconto = preco - (preco*tudoDesconto)
                contas[1][usario] = 0
            elif typoDeDesconto == "1":
                precoComDesconto = preco - preco * descontoTtl
            elif typoDeDesconto == "3":
                precoComDesconto = preco
                contas[1][usario] += descontoTtl

            print("Seu desconto total é", contas[1][usario]*100, "%")

    # Cadastra Uma CONTA
    else:
        querConta = input("você deseja criar uma conta: ")
        if querConta.upper() == "SIM":
            cpf = input("qual é o seu cpf: ")
            contas[0].append(cpf)
            usario = contas[0].index(cpf)

            if descontoTtl > 0:
                typoDeDesconto = input(
                    "\n\nSelecione alguma opção para desconto\n1 para usar desconto imediato\n2 para guadar esse desconto: ")

                while typoDeDesconto != "1" and typoDeDesconto != "2":
                    print("Opção inválida!")
                    typoDeDesconto = input(
                        "Selecione alguma opção para desconto\n1 para desconto imediato\n2 para guadar esse desconto: ")

                if typoDeDesconto == "2":
                    precoComDesconto = preco
                    contas[1].append(descontoTtl)
                    contas[2].append(1)
                elif typoDeDesconto == "1":
                    precoComDesconto = preco - preco * descontoTtl

                print("Your total discount is", contas[1][usario]*100, "%")
            else:
                precoComDesconto = preco
                contas[1].append(0)
                contas[2].append(0)
        else:
            precoComDesconto = preco - preco * descontoTtl

    print('\npaga : ', precoComDesconto)
