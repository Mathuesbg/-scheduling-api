from datetime import datetime
import os


def name_is_valid(name):
    os.system('cls')
    if len(name) < 3:
        print("Nome muito curto, precisa ter pelo menos 3 letras.")
        return False

    if not all(c.isalpha() or c.isspace() for c in name):
        print("Nome só pode conter letras e espaços.")
        return False

    return True


def email_is_valid(email):
    os.system('cls')

    if "@" not in email or "." not in email:
        print("Email inválido. Precisa conter '@' e '.'")
        return False

    if email.count("@") != 1:
        print("Email inválido. Só pode ter um '@'")
        return False


    if email.startswith("@") or email.endswith("@"):
        print("Email inválido. Não pode começar ou terminar com '@'")
        return False

    return True


def date_is_valid(date):
    os.system('cls')

    try:
        _data = datetime.strptime(date, "%Y-%m-%d")

        if _data.date() < datetime.today().date():
            print("Não é possível agendar para uma data no passado!")
            return False

        return True

    except ValueError:
        print("Formato inválido! Use o formato YYYY-MM-DD, tipo: 2025-04-07.")
        return False
    

def index_is_valid(index, menu):
    os.system('cls')

    try:
        index = int(index)

        if index < 0 or index >= len(menu):
            print("Escolha um indice dentro do range!")
            return False
        
    except ValueError:
        print("Digite um indice valido!")
        return False

    return True


