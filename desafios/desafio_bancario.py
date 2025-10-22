# DESAFIO BANCÁRIO DIO - Menu Numérico e Estilizado

WITHDRAW_LIMIT = 3

users = {'11122233344': {'id': 0, 'name': 'Admin', 'birthDate': '01/01/1990', 'address': 'Rua A, 123', 'password': 'admin'},}
accounts = {'11122233344': 
            {'AGENCY': '0001', 'account_number': 0, 'balance': 0.0, 'statement': '', 'withdrawals_amount': 0, 'limit': 3000}}

def menu_main():
    print("""
    ========================================
    |      BEM-VINDO AO BANCO CISCO     |
    ========================================
    | [1] Login                           |
    | [2] Cadastrar Usuário               |
    | [3] Cadastrar Conta                 |
    | [4] Listar Contas                   |
    | [5] Sair                            |
    ========================================
    """)

    return input('Escolha uma opção: ')


def login(users_list):
    
    '''Realiza o login do usuário com base no CPF e senha fornecidos.'''

    input_cpf = input("Informe o CPF (somente números): ")
    input_password = input("Informe a senha: ")

    if input_cpf in users_list.keys():
        if users_list[input_cpf]['password'] == input_password:
            print(f'Login bem-sucedido! Bem-vindo, {users_list[input_cpf]["name"]}.')
            return users_list[input_cpf], accounts[input_cpf], True
    else:
        print('Falha no login! CPF ou senha inválidos.')
        return None, None, False

def withdraw(*, account, amount, WITHDRAWAL_LIMIT):
    if amount > account['balance']:
        print("Operação falhou! Você não tem saldo suficiente.")
        input("\nPressione Enter para continuar...")
        return account['balance'], account['statement'], False
    elif account['withdrawals_amount'] >= WITHDRAWAL_LIMIT:
        print("Operação falhou! A quantidade de saques excede o limite.")
        input("\nPressione Enter para continuar...")
        return account['balance'], account['statement'], False
    elif amount <= 0:
        print("Operação falhou! O amount informado é inválido.")
        input("\nPressione Enter para continuar...")
        return account['balance'], account['statement'], False
    elif amount > account['limit']:
        print("Operação falhou! O valor do saque excede o quantia de saque limite da conta.")
        input("\nPressione Enter para continuar...")
        return account['balance'], account['statement'], False
    
    account['balance'] -= amount
    account['withdrawals_amount'] += 1
    account['statement'] += f"Saque: R$ {amount:.2f}\n"
    print(f"Saque de R$ {amount:.2f} realizado com sucesso!")
    input("\nPressione Enter para continuar...")
    return account['balance'], account['statement'], True

def deposit(account, /):

    amount = float(input("Informe o valor do depósito: "))

    if amount > 0:
        account['balance'] += amount
        account['statement'] += f"Depósito: R$ {amount:.2f}\n"
        print(f"Depósito de R$ {amount:.2f} realizado com sucesso!")
        input("\nPressione Enter para continuar...")
    else:
        print("Operação falhou! O amount informado é inválido.")
        input("\nPressione Enter para continuar...")

    return account['balance'], account['statement']

def get_statement(account, /):
    print("\n========================================")
    print("|           EXTRATO BANCÁRIO           |")
    print("========================================")
    if not account['statement']:
        print("|  Não foram realizadas movimentações.  |")
    else:
        for linha in account['statement'].strip().split('\n'):
            print(f"|  {linha:<34}|")
    print(f"|  Saldo: R$ {account['balance']:.2f}{' ' * (19 - len(f'Saldo: R$ {account['balance']:.2f}'))}|")
    print("========================================\n")
    input("Pressione Enter para continuar...")

def register_user(name, birth_date, cpf, address, password):
    users[cpf] = {
        'name': name,
        'birth_date': birth_date,
        'address': address,
        'password': password
    }
    print("Usuário cadastrado com sucesso!")
    register_account(cpf)


def register_account(cpf):
    if cpf in accounts:
        print("Conta já cadastrada!")
    else:
        accounts[cpf] = {
            'AGENCY': '0001',
            'account_number': len(accounts) + 1,
            'balance': 0,
            'statement': '',
            'withdrawals_amount': 0,
            'limit': 1000
        }
        print("\nConta cadastrada com sucesso!")
        input("\nPressione Enter para continuar...")

    return

def get_accounts_list():
    for cpf, account in accounts.items():
        user = users[cpf]
        print(f"""
        ========================================
        Usuário: {user['name']}
        Agência: {account['AGENCY']}
        Conta: {account['account_number']}
        ========================================
        """)

    input("\nPressione Enter para continuar...")

def menu_account(user, account):
    while True:
        print(f"""
        ========================================
        BEM-VINDO À SUA CONTA: {user['name']}
        ========================================
        | [1] Depositar                       |
        | [2] Sacar                           |
        | [3] Extrato                         |
        | [4] Sair                            |
        ========================================
        """)

        op = input('Escolha uma opção: ')

        if op == "1":
            deposit(account)

        elif op == "2":
            print("\n=== SAQUE ===")

            withdraw(account=account,
                amount=float(input("Informe o valor do saque: ")),
                WITHDRAWAL_LIMIT=WITHDRAW_LIMIT
            )
        elif op == "3":
            get_statement(account)
        elif op == "4":
            print(f"Saindo do usuário. Obrigado por usar o Banco {user['name']}.")
            input("\nPressione Enter para continuar...")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            input("\nPressione Enter para continuar...")

def main():
    while True:
        op = menu_main()

        if op == "1":
            user_in, account_in, is_user_found = login(users)
            input("\nPressione Enter para continuar...")

            if is_user_found:
                menu_account(user_in, account_in)
        elif op == "2":
            register_user(
                name=input("Informe o nome completo: "),
                birth_date=input("Informe a data de nascimento (DD/MM/AAAA): "),
                cpf=input("Informe o CPF (apenas números): "),
                address=input("Informe o endereço: "),
                password=input("Informe a senha para a conta: ")
            )
            input("\nPressione Enter para continuar...")
        elif op == "3":
            register_user(
                name=input("Informe o nome completo: "),
                birth_date=input("Informe a data de nascimento (DD/MM/AAAA): "),
                cpf=input("Informe o CPF (apenas números): "),
                address=input("Informe o endereço: "),
                password=input("Informe a senha para a conta: ")
            )
        elif op == "4":
            get_accounts_list()
        elif op == "5":
            print("Obrigado por usar o Banco Cisco. Até logo!")
            input("\nPressione Enter para continuar...")
            break

main()