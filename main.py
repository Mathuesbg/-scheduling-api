import os
from datetime import datetime
from api_consumer import Scheduling


schedule = Scheduling()


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


def get_valid_input(input_text, validator):

    while True:

        value = input(input_text).strip()

        if validator(value):
            return value



name = get_valid_input("Digite seu nome: ", name_is_valid)
email = get_valid_input("Digite seu email: ", email_is_valid)
date = get_valid_input("Digite a data em que deseja agendar (YYYY-MM-DD): ", date_is_valid)

slots = schedule.get_avaliable_slots(date)


if not slots : 
    print(f"Não há horários diponiveis para o dia {date}")

    date = get_valid_input("Digite a data em que deseja agendar (YYYY-MM-DD): ", date_is_valid)
    slots = schedule.get_avaliable_slots(date)

menu = schedule.get_slots_menu(slots)


print("-" * 50)

for slot in menu:
    
    time = menu[slot].split("T")[1].split(".")[0]
    print(f"({slot}) : {time}")


print("-" * 50)


    
while True:
    selected = int(input("Escolha um horario a partir do indice: "))
    os.system('cls')
    if selected < 0 or selected >= len(slots):
        print("Escolha um indice valido!")
        continue
    break

result = schedule.booking(selected, name, email)
print(result)
