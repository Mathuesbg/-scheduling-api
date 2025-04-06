import os
from datetime import datetime
from api_consumer import Scheduling


schedule = Scheduling()

while True:
    
    name = input("Digite seu nome: ").strip()
    os.system('cls')

    if len(name) < 3:
        print("Nome muito curto, precisa ter pelo menos 3 letras.")
        continue

    if not all(c.isalpha() or c.isspace() for c in name):
        print("Nome só pode conter letras e espaços.")
        continue

    break

while True:

    email = input("Digite seu email: ").strip()
    os.system('cls')

    if "@" not in email or "." not in email:
        print("Email inválido. Precisa conter '@' e '.'")
        continue

    if email.count("@") != 1:
        print("Email inválido. Só pode ter um '@'")
        continue

    if email.startswith("@") or email.endswith("@"):
        print("Email inválido. Não pode começar ou terminar com '@'")
        continue

    break

while True:
    date = input("Digite a data em que deseja agendar (YYYY-MM-DD): ").strip()
    os.system('cls')
    
    try:
        _data = datetime.strptime(date, "%Y-%m-%d")
        break
    
    except ValueError:
        print("Formato inválido! Use o formato YYYY-MM-DD, tipo: 2025-04-07.")


slots = schedule.get_avaliable_slots(date)
schedule.show_slots(slots)

while True:
    selected = int(input("Escolha um horario a partir do indice: "))
    os.system('cls')
    if selected < 0 or selected >= len(slots):
        print("Escolha um indice valido!")
        continue
    break

schedule.booking(selected, name, email)

