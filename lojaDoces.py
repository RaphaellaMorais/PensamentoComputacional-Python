
print("Loja de Doces")

def login():
    cadastro = input("Já possui cadastro? sim ou não: ")
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



login()

valor = 0
pedido = 0

def adicionar(valorProduto):
    global pedido, valor
    pedido += 1
    valor += valorProduto

while True:
    boloChocolate = 50.00
    docinhoSortidos = 40.00
    brigadeiro = 5.00
    beijinho = 5.00
    boloTradicional = 30.00

    print("==============MENU==============")
    opcoes = ['Bolo de Chocolate - R$ 50,00', 'Docinhos Sortidos - R$ 40,00', 'Brigadeiro - R$ 5,00', 'Beijinho - R$ 5,00', 'Bolo Tradicional - R$ 30,00', 'Finalizar pedido', 'Cancelar/Sair']
                
    print('Nossas Opções: ')
    for i in range (len(opcoes)):
        print((i),'-',opcoes[i])

    opcao = int(input("Digite o número da opção desejada: "))
    print(f'Opção escolhida foi: {opcoes[opcao]}')   

    if (opcao == 0): adicionar(boloChocolate)    

    elif (opcao == 1): adicionar(docinhoSortidos)               

    elif (opcao == 2): adicionar(brigadeiro)
        
    elif (opcao == 3): adicionar(beijinho)

    elif (opcao == 4): adicionar (boloTradicional)

    elif (opcao == 5):
        print("Total de pedidos: ", pedido)
        valorPagar = valor
        print("Total a pagar: R$", valorPagar)
        break     

    elif (opcao == 6):
        print("Cancelar/Sair. Até Logo!")
        pedidos = 0
        valorPagar = 0
        break

    else: 
        print("Erro! Digite uma opção válida!")

while True:
    print('==============PAGAMENTO==============')
    formas = ['Dinheiro', 'Cartão/Débito', 'Cancelar compra']
                                    
    print("Formas de Pagamento: ")
    for i in range (len(formas)):
        print((i),'-',formas[i])

    forma = int(input("Digite o número da opção desejada: "))
    print(f'Forma de pagamento escolhida: {formas[forma]}')

    if (forma == 0):
        pagamento = float(input("Digite o valor que deseja pagar: "))
        if(pagamento == valorPagar):
            print("Pagamento realizado com sucesso!")
            print("Volte Sempre!")
            break

        if(pagamento > valorPagar):
            troco = (pagamento - valorPagar)
            print("Seu troco é: R$ {:.2f}".format(troco))
            print("Volte Sempre!")
            break
        else:
            print("Pagamento não foi aprovado.")

    if (forma == 1):
        pagamento = float(input("Digite o valor que deseja pagar: "))
        if(pagamento == valorPagar):
            print("Pagamento Aprovado!")
            print("Volte Sempre!")
            break
        else:
            print("Pagamento não foi aprovado.")

    if (forma == 2):
        print("Compra cancelada! Volte Sempre!")
        break

    else:
        print("Erro! Digite uma opção válida!")
            