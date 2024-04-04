import getpass

def get_senha():
    while True:
        try:
            user = input("Usuário -> ")
            password = getpass.getpass("Senha -> ")
            if user != password:
                return (user, password)
            else:
                print("O usuario e a senha não podem ser iguais.")
                continue
        except ValueError as e:
            return e

user, password = get_senha()

