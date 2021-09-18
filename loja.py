print("Loja de Doces")

cadastro = input("Já possui cadastro? " + "sim " + "ou " + "não" ":")

if (cadastro == "sim"):
    print("Quem bom ter você de volta!")
    nome_cadastrado = "raphaella"
    senha_cadastrada = "12345"
    
else:
    print("Vamos realizar seu cadastro?")
    nome_cadastrado = input("Digite seu nome para login: ")
    senha_cadastrada = input("Digite uma senha: ")

while True:
    print("Digite seu login e senha para acessar a loja.")
    login = input("Login: ")
    senha = input("Senha: ")                       
    if nome_cadastrado == login and senha_cadastrada == senha:
        print("Login realizado com sucesso!")
        break     
    else:
        print("Login ou Senha incorretos, digite novamente.")


valor = 0
pedidos = 0

while True:

    boloChocolate = 50.00
    docinhoSortidos = 40.00
    brigadeiro = 5.00
    beijinho = 5.00
    boloTradicional = 30.00

    print("==============MENU==============")
    print ("Nossas opções: ")
    print("1 - Bolo de Chocolate - R$ 50,00.")
    print("2 - Docinhos Sortidos - R$ 40,00.")
    print("3 - Brigadeiro - R$ 5,00.")
    print("4 - Beijinho - R$ 5,00.") 
    print("5 - Bolo Tradicional - R$ 30,00.") 
    print("6 - Finalizar pedido.")
    print("7 - Cancelar/Sair.")
    opc = int(input("Digite a opção desejada: "))

    if (opc == 1):
        print(f"Bolo de Chocolate R$ {boloChocolate}")
        pedidos +=1     
        valor += boloChocolate

    elif (opc == 2):
        print(f"Docinhos Sortidos R$ {docinhoSortidos}")        
        pedidos +=1
        valor += docinhoSortidos

    elif (opc == 3):
        print(f"Brigadeiro R$ {brigadeiro}")        
        pedidos +=1
        valor += brigadeiro

    elif (opc == 4):
        print(f"Beijinho R$ {beijinho}")        
        pedidos +=1
        valor += beijinho

    elif (opc == 5):
        print(f"Bolo Tradicional R$ {boloTradicional}")        
        pedidos +=1
        valor += boloTradicional 

    elif (opc == 6):
        print("Finalizar pedido.")
        print("Total de pedidos: ", pedidos)
        valorPagar = valor
        print("Total a pagar: R$", valorPagar)
        break

    elif (opc == 7):
        print("Cancelar/Sair. Até Logo!")
        pedidos = 0
        valorPagar = 0
        break
    else:
        print("Erro! Digite uma opção válida!")

while True:
    print("============PAGAMENTO=============")
    print("Formas de Pagamento: ")
    print("1 - Dinheiro")
    print("2 - Cartão/Débito")
    print("3 - Cancelar compra.")

    forma = int(input("Digite a forma de pagamento escolhida: "))

    if (forma == 1):
        print("Forma de pagamento escolhida: 1 - Dinheiro.")
        pagamento = float(input("Digite o valor que deseja pagar: "))
        if(pagamento == valorPagar):
            print("Pagamento realizado com sucesso!")
            break

        if(pagamento > valorPagar):
            troco = (pagamento - valorPagar)
            print("Seu troco é: R$ {:.2f}".format(troco))
            print("Volte Sempre!")
            break

        else:
            print("Pagamento não foi aprovado.")

    if (forma == 2):
        print("Forma de pagamento escolhida: 2 - Cartão/Débito.")
        pagamento = float(input("Digite o valor que deseja pagar: "))
        if(pagamento == valorPagar):
            print("Pagamento Aprovado!")
            print("Volte Sempre!")
            break
        else:
            print("Pagamento não foi aprovado.")

    if (forma == 3):
        print("Compra cancelada! Volte Sempre!")
        break

    else:
        print("Erro! Digite uma opção válida!")
        
